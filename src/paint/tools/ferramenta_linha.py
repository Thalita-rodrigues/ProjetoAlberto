from .ferramenta import Ferramenta
from models import Linha


class FerramentaLinha(Ferramenta):
    ultima_linha = None

    def __init__(self):
        self.x_inicial = 0
        self.y_inicial = 0

    def clique(self, controlador, evento):
        self.x_inicial = evento.x
        self.y_inicial = evento.y

    def arrastar(self, controlador, evento):
        # Removido o underline daqui
        controlador.limpar_previa()

        figura = Linha(
            self.x_inicial,
            self.y_inicial,
            evento.x,
            evento.y,
            controlador.obter_cor_borda(),
            controlador.obter_cor_preenchimento(),
        )

        controlador.preview = figura.desenhar_previsualizacao(
            controlador.canvas
        )

    def soltar(self, controlador, evento):
        # Removido o underline daqui
        controlador.limpar_previa()

        figura = Linha(
            self.x_inicial,
            self.y_inicial,
            evento.x,
            evento.y,
            controlador.obter_cor_borda(),
            controlador.obter_cor_preenchimento(),
        )

        if FerramentaLinha.ultima_linha is not None:
            try:
                controlador.desenho.remover_figura(FerramentaLinha.ultima_linha)
            except ValueError:
                pass 

        FerramentaLinha.ultima_linha = figura
        controlador.desenho.adicionar_figura(figura)
        
        # Removido o underline daqui também
        controlador.redesenhar_tudo()