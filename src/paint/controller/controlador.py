import pickle

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
            
    def salvar_desenho(self, caminho_arquivo):
        """Serializa a lista de figuras e salva em um arquivo."""
        try:
            with open(caminho_arquivo, 'wb') as arquivo:
                # Salva a lista de figuras do modelo
                pickle.dump(self.desenho.obter_figuras(), arquivo)
            return True, "Desenho salvo com sucesso!"
        except Exception as e:
            return False, f"Erro ao salvar: {str(e)}"

    def carregar_desenho(self, caminho_arquivo):
        """Lê o arquivo, desserializa as figuras e joga para a tela."""
        try:
            with open(caminho_arquivo, 'rb') as arquivo:
                figuras_salvas = pickle.load(arquivo)
            
            # Limpa o canvas e o modelo atual
            self.limpar_canvas()
            
            # Adiciona as figuras carregadas ao modelo
            for figura in figuras_salvas:
                self.desenho.adicionar_figura(figura)
                
            # Manda desenhar tudo de novo
            self.redesenhar_tudo()
            return True, "Desenho carregado com sucesso!"
        except Exception as e:
            return False, f"Erro ao carregar: {str(e)}"

    def limpar_canvas(self):
        self.desenho.limpar()
        self.canvas.delete("all")
        self.limpar_previa()
        if hasattr(self.ferramenta_atual, 'cancelar'):
            self.ferramenta_atual.cancelar(self)
        try:
            from tools.ferramenta_linha import FerramentaLinha
            FerramentaLinha.ultima_linha = None
        except ImportError:
            pass