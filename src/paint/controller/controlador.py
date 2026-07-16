from models.figuras import Circulo
from models.figuras import Linha
from models.figuras import MaoLivre
from models.figuras import Oval
from models.figuras import PoligonoRegular
from models.figuras import Rabisco
from models.figuras import Retangulo


class ControladorDesenho:
	def __init__(self, canvas, desenho, obter_cor_borda, obter_cor_preenchimento):
		self.canvas = canvas
		self.desenho = desenho
		self.obter_cor_borda = obter_cor_borda
		self.obter_cor_preenchimento = obter_cor_preenchimento

		self.ferramenta = "retangulo"
		self.x_inicial = 0
		self.y_inicial = 0
		self.preview = None
		self.figura_mao_livre = None
		self.ultima_linha = None
		self.pontos_poligono = []
		self.preview_poligono = None

	def selecionar_ferramenta(self, ferramenta):
		self.ferramenta = ferramenta

	def clique(self, evento):
		self.x_inicial = evento.x
		self.y_inicial = evento.y

		if self.ferramenta == "poligono":
			self.adicionar_vertice(evento.x, evento.y)
			return

		if self.ferramenta in ("mao_livre", "rabisco"):
			cor_borda = self.obter_cor_borda()
			cor_preenchimento = self.obter_cor_preenchimento()

			classe = MaoLivre if self.ferramenta == "mao_livre" else Rabisco
			self.figura_mao_livre = classe(
				evento.x,
				evento.y,
				evento.x,
				evento.y,
				cor_borda,
				cor_preenchimento,
		)

			self._limpar_previa()
		
	def adicionar_vertice(self, x, y):
		self.pontos_poligono.append((x, y))
		if self.preview_poligono is not None:
			self.canvas.delete(self.preview_poligono)

		if len(self.pontos_poligono) > 1:

			coordenadas = []

			for px, py in self.pontos_poligono:
				coordenadas.extend([px, py])

			self.preview_poligono = self.canvas.create_line(
				*coordenadas,
				fill=self.obter_cor_borda(),
				width=2
			)

	def finalizar_poligono(self, evento):
		if self.ferramenta != "poligono":
			return

		if len(self.pontos_poligono) >= 3:
			cor_borda = self.obter_cor_borda()
			cor_preenchimento = self.obter_cor_preenchimento()
    		
			novo_poligono = PoligonoRegular(
                pontos=list(self.pontos_poligono),
                cor_borda=cor_borda,
                cor_preenchimento=cor_preenchimento
            )

            
			self.desenho.adicionar_figura(novo_poligono)
        
        
		if self.preview_poligono is not None:
			self.canvas.delete(self.preview_poligono)
			self.preview_poligono = None
            
		self.pontos_poligono.clear()
		self._redesenhar_tudo()

	def arrastar(self, evento):
		if self.ferramenta in ("mao_livre", "rabisco"):
			if self.figura_mao_livre is None:
				self.clique(evento)

			self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)
			self._limpar_previa()
			self.preview = self.figura_mao_livre.desenhar_previsualizacao(self.canvas)
			return

		self._limpar_previa()
		figura = self._criar_figura(evento.x, evento.y)
		self.preview = figura.desenhar_previsualizacao(self.canvas)

	def soltar(self, evento):
		if self.ferramenta in ("mao_livre", "rabisco"):
			if self.figura_mao_livre is not None:
				self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)
				self._limpar_previa()
				self.desenho.adicionar_figura(self.figura_mao_livre)
				self.figura_mao_livre = None
				self._redesenhar_tudo()
			return

		self._limpar_previa()
		figura = self._criar_figura(evento.x, evento.y)

		if self.ferramenta == "linha":
			if self.ultima_linha is not None:
				self.desenho.remover_figura(self.ultima_linha)

			self.ultima_linha = figura
			self.desenho.adicionar_figura(figura)
			self._redesenhar_tudo()
			return

		self.desenho.adicionar_figura(figura)
		self._redesenhar_tudo()

	def _limpar_previa(self):
		if self.preview is not None:
			self.canvas.delete(self.preview)
			self.preview = None
	def limpar_canvas(self):
		self.desenho.limpar()
		self.canvas.delete("all")
  
		self.preview = None
		self.figura_mao_livre = None
		self.ultima_linha = None
		self.pontos_poligono.clear()
  
		if self.preview_poligono is not None:
			self.canvas.delete(self.preview_poligono)
			self.preview_poligono = None
  
	def _redesenhar_tudo(self):
		self.canvas.delete("all")
		self.desenho.desenhar(self.canvas)
	def _criar_figura(self, x_final, y_final):
		cor_borda = self.obter_cor_borda()
		cor_preenchimento = self.obter_cor_preenchimento()

		if self.ferramenta == "retangulo":
			return Retangulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

		if self.ferramenta == "oval":
			return Oval(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

		if self.ferramenta == "circulo":
			return Circulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

		if self.ferramenta in ("mao_livre", "rabisco"):
			classe = MaoLivre if self.ferramenta == "mao_livre" else Rabisco

			return classe(
                self.x_inicial,
                self.y_inicial,
                x_final,
                y_final,
                cor_borda,
                cor_preenchimento,
            )

		if self.ferramenta == "linha":
			return Linha(
                self.x_inicial,
                self.y_inicial,
                x_final,
                y_final,
                cor_borda,
                cor_preenchimento,
            )

		return Retangulo(self.x_inicial, self.y_inicial, x_final, y_final, cor_borda, cor_preenchimento)