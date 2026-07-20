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

    
    def mover(self, evento):
        if self.ferramenta_atual and hasattr(self.ferramenta_atual, 'mover'):
            self.ferramenta_atual.mover(self, evento)

    def duplo_clique(self, evento):
        if self.ferramenta_atual and hasattr(self.ferramenta_atual, 'duplo_clique'):
            self.ferramenta_atual.duplo_clique(self, evento)
   

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
        
        try:
            with open(caminho_arquivo, 'wb') as arquivo:
                pickle.dump(self.desenho.obter_figuras(), arquivo)
            return True, 
        except Exception as e:
            return False, f"Erro ao salvar: {str(e)}"

    def carregar_desenho(self, caminho_arquivo):
      
        try:
            with open(caminho_arquivo, 'rb') as arquivo:
                figuras_salvas = pickle.load(arquivo)
            
            self.limpar_canvas()
            
            for figura in figuras_salvas:
                self.desenho.adicionar_figura(figura)
                
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