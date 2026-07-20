class ControladorDesenho:
    def __init__(self, canvas, desenho, obter_cor_borda, obter_cor_preenchimento):
        self.canvas = canvas
        self.desenho = desenho
        self.obter_cor_borda = obter_cor_borda
        self.obter_cor_preenchimento = obter_cor_preenchimento

        self.ferramenta_atual = None
        self.preview = None

    def selecionar_ferramenta(self, ferramenta_instancia):
        if hasattr(self.ferramenta_atual, 'cancelar'):
            self.ferramenta_atual.cancelar(self)
        self.ferramenta_atual = ferramenta_instancia

    def clique(self, evento):
        if self.ferramenta_atual:
            self.ferramenta_atual.clique(self, evento)

    def arrastar(self, evento):
        if self.ferramenta_atual:
            self.ferramenta_atual.arrastar(self, evento)

    def soltar(self, evento):
        if self.ferramenta_atual:
            self.ferramenta_atual.soltar(self, evento)

    def finalizar_poligono(self, evento=None):
        if hasattr(self.ferramenta_atual, 'finalizar'):
            self.ferramenta_atual.finalizar(self, evento)

    def limpar_previa(self):
        if self.preview is not None:
            self.canvas.delete(self.preview)
            self.preview = None

    def redesenhar_tudo(self):
        self.canvas.delete("all")
        for figura in self.desenho.obter_figuras():
            figura.desenhar(self.canvas)

    def limpar_canvas(self):
        self.desenho.limpar()
        self.canvas.delete("all")
        self.limpar_previa()
        if hasattr(self.ferramenta_atual, 'cancelar'):
            self.ferramenta_atual.cancelar(self)