from figuras import Circulo
from figuras import Oval
from figuras import MaoLivre
from figuras import PoligonoRegular
from figuras import Retangulo


class ControladorDesenho:
    def __init__(self, canvas, obter_cor_borda, obter_cor_preenchimento):
        self.canvas = canvas
        self.obter_cor_borda = obter_cor_borda
        self.obter_cor_preenchimento = obter_cor_preenchimento
        self.ferramenta = "retangulo"
        self.x_inicial = 0
        self.y_inicial = 0
        self.preview = None
        self.figura_mao_livre = None

    def selecionar_ferramenta(self, ferramenta):
        self.ferramenta = ferramenta

    def clique(self, evento):
        self.x_inicial = evento.x
        self.y_inicial = evento.y

        if self.ferramenta == "mao_livre":
            cor_borda = self.obter_cor_borda()
            cor_preenchimento = self.obter_cor_preenchimento()
            self.figura_mao_livre = MaoLivre(
                evento.x,
                evento.y,
                evento.x,
                evento.y,
                cor_borda,
                cor_preenchimento,
            )
            self._limpar_previa()

    def arrastar(self, evento):
        if self.ferramenta == "mao_livre":
            if self.figura_mao_livre is None:
                self.clique(evento)

            self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)
            self._limpar_previa()
            self.preview = self.figura_mao_livre.desenhar_previsualizacao(self.canvas)
            return

        self._limpar_previa()
        figura = self._criar_figura(evento.x, evento.y)
        self.preview = figura.desenhar_previsualizacao(self.canvas)

    def soltar(self, evento):
        if self.ferramenta == "mao_livre":
            if self.figura_mao_livre is not None:
                self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)
                self._limpar_previa()
                self.figura_mao_livre.desenhar(self.canvas)
                self.figura_mao_livre = None
            return

        self._limpar_previa()
        figura = self._criar_figura(evento.x, evento.y)
        figura.desenhar(self.canvas)

    def _limpar_previa(self):
        if self.preview is not None:
            self.canvas.delete(self.preview)
            self.preview = None

    def _criar_figura(self, x_final, y_final):
        cor_borda = self.obter_cor_borda()
        cor_preenchimento = self.obter_cor_preenchimento()

        if self.ferramenta == "retangulo":
            return Retangulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta == "oval":
            return Oval(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta == "circulo":
            return Circulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta == "poligono":
            return PoligonoRegular(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta == "mao_livre":
            return MaoLivre(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        return Retangulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)
