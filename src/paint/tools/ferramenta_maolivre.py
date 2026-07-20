from tools.ferramenta import Ferramenta

class FerramentaMaoLivre(Ferramenta):
    def __init__(self, classe_modelo):
        self.classe_modelo = classe_modelo
        self.figura = None

    def clique(self, controlador, evento):
        self.figura = self.classe_modelo(
            evento.x, evento.y, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.limpar_previa()

    def arrastar(self, controlador, evento):
        if not self.figura:
            self.clique(controlador, evento)

        self.figura.adicionar_ponto(evento.x, evento.y)
        controlador.limpar_previa()
        controlador.preview = self.figura.desenhar_previsualizacao(controlador.canvas)

    def soltar(self, controlador, evento):
        if self.figura:
            self.figura.adicionar_ponto(evento.x, evento.y)
            controlador.limpar_previa()
            controlador.desenho.adicionar_figura(self.figura)
            self.figura = None
            controlador.redesenhar_tudo()