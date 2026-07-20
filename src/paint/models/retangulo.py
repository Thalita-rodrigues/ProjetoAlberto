from .figuras import Figura

class Retangulo(Figura):

    def _desenhar(self, canvas, previsualizacao=False):
        return canvas.create_rectangle(
            self.x_inicial,
            self.y_inicial,
            self.x_final,
            self.y_final,
            **self._opcoes_desenho(previsualizacao),
        )