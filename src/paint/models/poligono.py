from .figuras import Figura

class Poligono(Figura):

    def __init__(self, pontos, cor_borda, cor_preenchimento):
        super().__init__(0, 0, 0, 0,
                         cor_borda, cor_preenchimento)

        self.pontos = pontos

    def _coordenadas(self):

        coordenadas = []

        for x, y in self.pontos:
            coordenadas.extend([x, y])

        return coordenadas

    def _desenhar(self, canvas, previsualizacao=False):

        return canvas.create_polygon(
            *self._coordenadas(),
            **self._opcoes_desenho(previsualizacao)
        )