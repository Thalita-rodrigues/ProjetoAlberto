from .figuras import Figura

class Circulo(Figura):

    def _coordenadas_ajustadas(self):
        lado = min(
            abs(self.x_final - self.x_inicial),
            abs(self.y_final - self.y_inicial)
        )

        if self.x_final < self.x_inicial:
            x_final = self.x_inicial - lado
        else:
            x_final = self.x_inicial + lado

        if self.y_final < self.y_inicial:
            y_final = self.y_inicial - lado
        else:
            y_final = self.y_inicial + lado

        return self.x_inicial, self.y_inicial, x_final, y_final

    def _desenhar(self, canvas, previsualizacao=False):

        x1, y1, x2, y2 = self._coordenadas_ajustadas()

        return canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            **self._opcoes_desenho(previsualizacao),
        )