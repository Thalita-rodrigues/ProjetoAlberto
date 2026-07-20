from .figuras import Figura

class Linha(Figura):

    def _desenhar(self, canvas, previsualizacao=False):

        opcoes = {
            "fill": self.cor_borda,
            "width": 2,
        }

        if previsualizacao:
            opcoes["dash"] = (4, 2)

        return canvas.create_line(
            self.x_inicial,
            self.y_inicial,
            self.x_final,
            self.y_final,
            **opcoes
        )