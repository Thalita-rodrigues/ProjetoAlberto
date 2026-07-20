from models import Poligono # Importe conforme o nome exato no seu models
from tools.ferramenta import Ferramenta

class FerramentaPoligono(Ferramenta):
    def __init__(self):
        self.pontos = []
        self.preview_poligono = None

    def clique(self, controlador, evento):
        self.pontos.append((evento.x, evento.y))
        
        if self.preview_poligono is not None:
            controlador.canvas.delete(self.preview_poligono)

        if len(self.pontos) > 1:
            coordenadas = []
            for px, py in self.pontos:
                coordenadas.extend([px, py])

            self.preview_poligono = controlador.canvas.create_line(
                *coordenadas,
                fill=controlador.obter_cor_borda(),
                width=2
            )

    def arrastar(self, controlador, evento):
        pass # Não faz nada ao arrastar

    def soltar(self, controlador, evento):
        pass # Não faz nada ao soltar

    def finalizar(self, controlador, evento=None):
        if len(self.pontos) >= 3:
            novo_poligono = Poligono(
                pontos=list(self.pontos),
                cor_borda=controlador.obter_cor_borda(),
                cor_preenchimento=controlador.obter_cor_preenchimento()
            )
            controlador.desenho.adicionar_figura(novo_poligono)
        
        self.cancelar(controlador)
        controlador.redesenhar_tudo()

    def cancelar(self, controlador):
        if self.preview_poligono is not None:
            controlador.canvas.delete(self.preview_poligono)
            self.preview_poligono = None
        self.pontos.clear()