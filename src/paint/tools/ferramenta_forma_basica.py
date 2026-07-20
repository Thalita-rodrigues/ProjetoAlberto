from tools.ferramenta import Ferramenta

class FerramentaFormaBasica(Ferramenta):
    def __init__(self, classe_modelo):
        self.classe_modelo = classe_modelo
        self.x_inicial = 0
        self.y_inicial = 0

    def clique(self, controlador, evento):
        self.x_inicial = evento.x
        self.y_inicial = evento.y
        controlador.limpar_previa()

    def arrastar(self, controlador, evento):
        controlador.limpar_previa()
        figura = self.classe_modelo(
            self.x_inicial, self.y_inicial, evento.x, evento.y, 
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.preview = figura.desenhar_previsualizacao(controlador.canvas)

    def soltar(self, controlador, evento):
        controlador.limpar_previa()
        figura = self.classe_modelo(
            self.x_inicial, self.y_inicial, evento.x, evento.y, 
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.desenho.adicionar_figura(figura)
        controlador.redesenhar_tudo()