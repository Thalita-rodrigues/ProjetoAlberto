from .ferramenta import Ferramenta
from models import Linha


class FerramentaLinha(Ferramenta):

    def clique(self, evento):
        self.controlador.x_inicial = evento.x
        self.controlador.y_inicial = evento.y

    def arrastar(self, evento):
        self.controlador._limpar_previa()

        figura = Linha(
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

        figura = Linha(
            self.controlador.x_inicial,
            self.controlador.y_inicial,
            evento.x,
            evento.y,
            self.controlador.obter_cor_borda(),
            self.controlador.obter_cor_preenchimento(),
        )

        if self.controlador.ultima_linha is not None:
            self.controlador.desenho.remover_figura(
                self.controlador.ultima_linha
            )

        self.controlador.ultima_linha = figura

        self.controlador.desenho.adicionar_figura(figura)

        self.controlador._redesenhar_tudo()