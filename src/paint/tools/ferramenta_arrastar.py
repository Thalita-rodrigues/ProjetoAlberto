from .ferramenta import Ferramenta


class FerramentaArrastar(Ferramenta):

    def __init__(self, controlador, classe_figura):
        super().__init__(controlador)
        self.classe_figura = classe_figura

    def clique(self, evento):
        self.controlador.x_inicial = evento.x
        self.controlador.y_inicial = evento.y

    def arrastar(self, evento):
        self.controlador._limpar_previa()

        figura = self.classe_figura(
            self.controlador.x_inicial,
            self.controlador.y_inicial,
            evento.x,
            evento.y,
            self.controlador.obter_cor_borda(),
            self.controlador.obter_cor_preenchimento(),
        )

        self.controlador.preview = figura.desenhar_previsualizacao(
            self.controlador.canvas
        )

    def soltar(self, evento):
        self.controlador._limpar_previa()

        figura = self.classe_figura(
            self.controlador.x_inicial,
            self.controlador.y_inicial,
            evento.x,
            evento.y,
            self.controlador.obter_cor_borda(),
            self.controlador.obter_cor_preenchimento(),
        )

        self.controlador.desenho.adicionar_figura(figura)
        self.controlador._redesenhar_tudo()