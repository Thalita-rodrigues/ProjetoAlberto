class Desenho:
    def __init__(self):
        self.figuras = []

    def adicionar_figura(self, figura):
        self.figuras.append(figura)

    def remover_figura(self, figura):
        if figura in self.figuras:
            self.figuras.remove(figura)

    def limpar(self):
        self.figuras.clear()

    def desenhar(self, canvas):
        for figura in self.figuras:
            figura.desenhar(canvas)