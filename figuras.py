from abc import ABC, abstractmethod
import math
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


# Implementação da figura retângulo.
class Retangulo(Figura):
    def _desenhar(self, canvas, previsualizacao=False):
        return canvas.create_rectangle(
            self.x_inicial,
            self.y_inicial,
            self.x_final,
            self.y_final,
            **self._opcoes_desenho(previsualizacao),
        )

# Implementação da figura oval.
class Oval(Figura):
    def _desenhar(self, canvas, previsualizacao=False):
        return canvas.create_oval(
            self.x_inicial,
            self.y_inicial,
            self.x_final,
            self.y_final,
            **self._opcoes_desenho(previsualizacao),
        )

# Classe responsável por desenhar círculos.
# Diferente do oval, ela garante que largura e altura tenham o mesmo tamanho.
class Circulo(Figura):

    # Ajusta as coordenadas para formar sempre um círculo perfeito.
    def _coordenadas_ajustadas(self):
        lado = min(abs(self.x_final - self.x_inicial), abs(self.y_final - self.y_inicial))

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
        x_inicial, y_inicial, x_final, y_final = self._coordenadas_ajustadas()

        return canvas.create_oval(
            x_inicial,
            y_inicial,
            x_final,
            y_final,
            **self._opcoes_desenho(previsualizacao),
        )


# Classe responsável pelo desenho de polígonos regulares.
# Por padrão, cria um pentágono (5 lados), mas esse valor pode ser alterado.
class PoligonoRegular(Figura):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento, lados=5):
        super().__init__(x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento)
        self.lados = lados

    # Calcula todos os vértices do polígono utilizando funções trigonométricas.
    def _calcular_pontos(self):
        centro_x = (self.x_inicial + self.x_final) / 2
        centro_y = (self.y_inicial + self.y_final) / 2
        raio = min(abs(self.x_final - self.x_inicial), abs(self.y_final - self.y_inicial)) / 2
        angulo_inicial = -math.pi / 2

        pontos = []

        # Calcula cada vértice de acordo com a quantidade de lados.
        for indice in range(self.lados):
            angulo = angulo_inicial + (2 * math.pi * indice / self.lados)
            pontos.extend([
                round(centro_x + raio * math.cos(angulo)),
                round(centro_y + raio * math.sin(angulo)),
            ])

        return pontos

    def _desenhar(self, canvas, previsualizacao=False):
        return canvas.create_polygon(
            *self._calcular_pontos(),
            **self._opcoes_desenho(previsualizacao),
        )


# Classe utilizada para desenhar linhas à mão livre.
# Ela armazena todos os pontos percorridos pelo mouse.
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
    
class Linha(Figura):

    def _desenhar(self, canvas, previsualizacao=False):

        opcoes = {
            "fill": self.cor_borda,
            "width": 2
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
     
class Rabisco(MaoLivre):
    pass