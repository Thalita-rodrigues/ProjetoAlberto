from abc import ABC, abstractmethod

# Classe base para todas as figuras do programa.
# Ela reúne os atributos e métodos que todas as figuras possuem em comum.
class Figura(ABC):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento):
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.x_final = x_final
        self.y_final = y_final
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    # Define as opções de desenho utilizadas pelo Tkinter.
    # Se for uma pré-visualização, aplica um efeito pontilhado para indicar
    # que a figura ainda não foi finalizada.
    def _opcoes_desenho(self, previsualizacao=False):
        opcoes = {
            "outline": self.cor_borda,
            "fill": self.cor_preenchimento,
        }

        if previsualizacao:
            opcoes["stipple"] = "gray50"
            opcoes["dash"] = (4, 2)

        return opcoes

    # Desenha a figura definitiva no canvas.
    def desenhar(self, canvas):
        return self._desenhar(canvas, previsualizacao=False)

    # Exibe uma prévia da figura enquanto o usuário arrasta o mouse.
    def desenhar_previsualizacao(self, canvas):
        return self._desenhar(canvas, previsualizacao=True)

    # Cada tipo de figura implementa sua própria forma de desenho.
    @abstractmethod
    def _desenhar(self, canvas, previsualizacao=False):
        raise NotImplementedError
