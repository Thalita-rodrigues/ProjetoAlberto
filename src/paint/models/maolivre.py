from .figuras import Figura

class MaoLivre(Figura):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento):
        super().__init__(x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento)
        self.pontos = [(x_inicial, y_inicial), (x_final, y_final)]

    # Adiciona um novo ponto conforme o usuário movimenta o mouse.
    def adicionar_ponto(self, x, y):
        self.x_final = x
        self.y_final = y
        self.pontos.append((x, y))

    # Converte a lista de tuplas em uma sequência de coordenadas
    # no formato esperado pelo método create_line do Tkinter.
    def _coordenadas(self):
        coordenadas = []
        for x, y in self.pontos:
            coordenadas.extend([x, y])
        return coordenadas

    def _desenhar(self, canvas, previsualizacao=False):
        # Evita desenhar uma linha com menos de dois pontos.
        if len(self.pontos) < 2:
            return None

        # Configurações para deixar o traço mais suave.
        opcoes = {
            "fill": self.cor_borda,
            "width": 2,
            "smooth": True,
            "splinesteps": 12,
            "capstyle": "round",
            "joinstyle": "round",
        }

        # Durante a pré-visualização, exibe a linha pontilhada.
        if previsualizacao:
            opcoes["dash"] = (4, 2)

        return canvas.create_line(
            *self._coordenadas(),
            **opcoes,
        )