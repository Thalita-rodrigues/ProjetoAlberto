import tkinter as tk
from tkinter import messagebox

from controller.controlador import ControladorDesenho
from models.cores import GerenciadorCores
from models.desenho import Desenho

# Importando os Modelos
from models import Retangulo, Oval, Circulo, Linha, MaoLivre, Rabisco

# Importando as Ferramentas (Estados)
from tools.ferramenta_forma_basica import FerramentaFormaBasica
from tools.ferramenta_maolivre import FerramentaMaoLivre
from tools.ferramenta_poligono import FerramentaPoligono


class InterfaceGrafica:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Paint Padrão State")

        largura = 900
        altura = 600

        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        pos_x = (largura_tela - largura) // 2
        pos_y = (altura_tela - altura) // 2

        self.janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

        self.desenho = Desenho()
        self.cor_borda = "black"
        self.cor_preenchimento = "white"

        self.canvas = None
        self.controlador = None

    def criar_widgets(self):
        barra = tk.Frame(self.janela)
        barra.pack(fill="x")

        estilo_botao = {
            "bg": "#ff69b4",
            "fg": "white",
            "activebackground": "#ff85c1",
            "activeforeground": "white",
            "highlightthickness": 2,
            "highlightbackground": "#ff1493",
            "highlightcolor": "#ff1493",
            "bd": 2,
            "relief": "ridge",
        }

        # Mapeamento de botões usando lambdas para instanciar os estados corretamente
        ferramentas = [
            ("Retângulo", lambda: FerramentaFormaBasica(Retangulo)),
            ("Oval", lambda: FerramentaFormaBasica(Oval)),
            ("Círculo", lambda: FerramentaFormaBasica(Circulo)),
            ("Linha", lambda: FerramentaFormaBasica(Linha)),
            ("Polígono", lambda: FerramentaPoligono()),
            ("Mão livre", lambda: FerramentaMaoLivre(MaoLivre)),
            ("Rabisco", lambda: FerramentaMaoLivre(Rabisco)),
        ]

        for texto, funcao_criadora in ferramentas:
            tk.Button(
                barra, 
                text=texto,
                command=lambda f=funcao_criadora: self.selecionar_ferramenta(f()),
                **estilo_botao
            ).pack(side="left")

        tk.Button(barra, text="Cor da borda", command=self.mudar_borda, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Cor preenchimento", command=self.mudar_preenchimento, **estilo_botao).pack(side="left")
        tk.Button(barra, text="?", width=3, command=self.ajuda_poligono, bg="#87CEFA", fg="black", font=("Arial", 10, "bold")).pack(side="right", padx=5)
        tk.Button(barra, text="Limpar", command=self.limpar_canvas, **estilo_botao).pack(side="left")

        self.canvas = tk.Canvas(self.janela, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.controlador = ControladorDesenho(
            self.canvas,
            self.desenho,
            lambda: self.cor_borda,
            lambda: self.cor_preenchimento,
        )

        # Inicia com a ferramenta Retângulo por padrão
        self.controlador.selecionar_ferramenta(FerramentaFormaBasica(Retangulo))

        self.canvas.bind("<Button-1>", self.controlador.clique)
        self.canvas.bind("<B1-Motion>", self.controlador.arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.controlador.soltar)
        self.canvas.bind("<Double-Button-1>", self.controlador.finalizar_poligono)

    def ajuda_poligono(self):
        messagebox.showinfo(
            "Como desenhar um polígono",
            "1. Selecione a ferramenta Polígono.\n\n"
            "2. Clique para adicionar cada vértice.\n\n"
            "3. Após criar pelo menos três vértices,\n"
            "clique duas vezes no ponto de fim \n"
            "desejado para fechar o polígono."
        )

    def selecionar_ferramenta(self, nova_ferramenta):
        if self.controlador:
            self.controlador.selecionar_ferramenta(nova_ferramenta)
    
    def limpar_canvas(self):
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente apagar todos os desenhos?")
        if resposta and self.controlador is not None:   
            self.controlador.limpar_canvas()

    def mudar_borda(self):
        self.cor_borda = GerenciadorCores.escolher_cor_borda()

    def mudar_preenchimento(self):
        self.cor_preenchimento = GerenciadorCores.escolher_cor_preenchimento()

    def executar(self):
        self.criar_widgets()
        self.janela.mainloop()

def iniciar():
    interface = InterfaceGrafica()
    interface.executar()