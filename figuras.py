from abc import ABC, abstractmethod
import math


class Figura(ABC):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento):
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.x_final = x_final
        self.y_final = y_final
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def _opcoes_desenho(self, previsualizacao=False):
        opcoes = {
            "outline": self.cor_borda,
            "fill": self.cor_preenchimento,
        }

        if previsualizacao:
            opcoes["stipple"] = "gray50"
            opcoes["dash"] = (4, 2)

        return opcoes

    def desenhar(self, canvas):
        return self._desenhar(canvas, previsualizacao=False)

    def desenhar_previsualizacao(self, canvas):
        return self._desenhar(canvas, previsualizacao=True)

    @abstractmethod
    def _desenhar(self, canvas, previsualizacao=False):
        raise NotImplementedError


class Retangulo(Figura):
    def _desenhar(self, canvas, previsualizacao=False):
        return canvas.create_rectangle(
            self.x_inicial,
            self.y_inicial,
            self.x_final,
            self.y_final,
            **self._opcoes_desenho(previsualizacao),
        )


class Oval(Figura):
    def _desenhar(self, canvas, previsualizacao=False):
        return canvas.create_oval(
            self.x_inicial,
            self.y_inicial,
            self.x_final,
            self.y_final,
            **self._opcoes_desenho(previsualizacao),
        )


class Circulo(Figura):
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


class PoligonoRegular(Figura):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento, lados=5):
        super().__init__(x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento)
        self.lados = lados

    def _calcular_pontos(self):
        centro_x = (self.x_inicial + self.x_final) / 2
        centro_y = (self.y_inicial + self.y_final) / 2
        raio = min(abs(self.x_final - self.x_inicial), abs(self.y_final - self.y_inicial)) / 2
        angulo_inicial = -math.pi / 2

        pontos = []
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


class MaoLivre(Figura):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento):
        super().__init__(x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento)
        self.pontos = [(x_inicial, y_inicial), (x_final, y_final)]

    def adicionar_ponto(self, x, y):
        self.x_final = x
        self.y_final = y
        self.pontos.append((x, y))

    def _coordenadas(self):
        coordenadas = []
        for x, y in self.pontos:
            coordenadas.extend([x, y])
        return coordenadas

    def _desenhar(self, canvas, previsualizacao=False):
        if len(self.pontos) < 2:
            return None

        opcoes = {
            "fill": self.cor_borda,
            "width": 2,
            "smooth": True,
            "splinesteps": 12,
            "capstyle": "round",
            "joinstyle": "round",
        }

        if previsualizacao:
            opcoes["dash"] = (4, 2)

        return canvas.create_line(
            *self._coordenadas(),
            **opcoes,
        )