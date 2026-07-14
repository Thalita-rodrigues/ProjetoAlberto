from models.figuras import Circulo
from models.figuras import Oval
from models.figuras import PoligonoRegular
from models.figuras import Retangulo
from models.figuras import MaoLivre
from models.figuras import Linha
from models.figuras import Rabisco


class ControladorDesenho:
    def __init__(self, canvas, obter_cor_borda, obter_cor_preenchimento):
        self.canvas = canvas
        self.obter_cor_borda = obter_cor_borda
        self.obter_cor_preenchimento = obter_cor_preenchimento

        # Ferramenta selecionada inicialmente
        self.ferramenta = "retangulo"

        # Armazena o ponto onde o usuário iniciou o desenho
        self.x_inicial = 0
        self.y_inicial = 0

        # Guarda a figura exibida apenas durante a pré-visualização
        self.preview = None

        # Utilizado para controlar o desenho à mão livre
        self.figura_mao_livre = None

        # Guarda a última linha desenhada
        self.ultima_linha = None

    def selecionar_ferramenta(self, ferramenta):
        self.ferramenta = ferramenta

    def clique(self, evento):
        # Salva a posição inicial do mouse
        self.x_inicial = evento.x
        self.y_inicial = evento.y

        if self.ferramenta in ("mao_livre", "rabisco"):

            cor_borda = self.obter_cor_borda()
            cor_preenchimento = self.obter_cor_preenchimento()

            if self.ferramenta == "mao_livre":
                classe = MaoLivre
            else:
                classe = Rabisco

            self.figura_mao_livre = classe(
                evento.x,
                evento.y,
                evento.x,
                evento.y,
                cor_borda,
                cor_preenchimento,
    )

            self._limpar_previa()


    def arrastar(self, evento):
        # Atualiza continuamente o desenho enquanto o mouse é arrastado
        if self.ferramenta in ("mao_livre","rabisco"):
            if self.figura_mao_livre is None:
                self.clique(evento)

            self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)

            self._limpar_previa()
            self.preview = self.figura_mao_livre.desenhar_previsualizacao(self.canvas)
            return

        # Remove a prévia anterior e desenha uma nova
        self._limpar_previa()
        figura = self._criar_figura(evento.x, evento.y)
        self.preview = figura.desenhar_previsualizacao(self.canvas)

    def soltar(self, evento):
        # Ao soltar o mouse, finaliza o desenho
        if self.ferramenta in ("mao_livre","rabisco"):
            if self.figura_mao_livre is not None:
                self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)

                self._limpar_previa()
                self.figura_mao_livre.desenhar(self.canvas)
                self.figura_mao_livre = None
            return

        self._limpar_previa()
        figura = self._criar_figura(evento.x, evento.y)

        if self.ferramenta == "linha":
            # Remove a linha anterior
            if self.ultima_linha is not None:
                    self.canvas.delete(self.ultima_linha)
             # Desenha a nova linha e guarda seu ID
            self.ultima_linha = figura.desenhar(self.canvas)

        else:
                figura.desenhar(self.canvas)

    def _limpar_previa(self):
        # Remove a figura temporária da tela
        if self.preview is not None:
            self.canvas.delete(self.preview)
            self.preview = None

    def _criar_figura(self, x_final, y_final):
        # Obtém as cores escolhidas pelo usuário
        cor_borda = self.obter_cor_borda()
        cor_preenchimento = self.obter_cor_preenchimento()

        # Cria a figura correspondente à ferramenta selecionada
        if self.ferramenta == "retangulo":
            return Retangulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta == "oval":
            return Oval(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta == "circulo":
            return Circulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta == "poligono":
            return PoligonoRegular(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if self.ferramenta in ("mao_livre", "rabisco"):

            classe = MaoLivre if self.ferramenta == "mao_livre" else Rabisco

            return classe(
                self.x_inicial,
                self.y_inicial,
                x_final,
                y_final,
                cor_borda,
                cor_preenchimento,
    )
        if self.ferramenta == "linha":
            return Linha(
            self.x_inicial,
            self.y_inicial,
            x_final,
            y_final,
            cor_borda,
            cor_preenchimento
    )
        
        # Caso nenhuma ferramenta seja reconhecida, desenha um retângulo
        return Retangulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)