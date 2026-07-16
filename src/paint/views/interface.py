import tkinter as tk

from controller.controlador import ControladorDesenho
from models.cores import escolher_cor_borda, escolher_cor_preenchimento
from models.desenho import Desenho
<<<<<<< HEAD
janela = None
canvas = None
controlador = None

# Ferramenta selecionada ao iniciar o programa.
ferramenta = "retangulo"

# Cores padrão utilizadas nos desenhos.
cor_borda = "black"
cor_preenchimento = "white"
=======
>>>>>>> 6ed329f39d415fc1a59ca5bba8866317f92f0821


class InterfaceGrafica:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Paint MVC")

        largura = 900
        altura = 600
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        pos_x = (largura_tela - largura) // 2
        pos_y = (altura_tela - altura) // 2
        self.janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

        self.desenho = Desenho()
        self.ferramenta = "retangulo"
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

        tk.Button(barra, text="Retângulo", command=self.selecionar_retangulo, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Oval", command=self.selecionar_oval, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Círculo", command=self.selecionar_circulo, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Polígono", command=self.selecionar_poligono, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Mão livre", command=self.selecionar_mao_livre, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Linha", command=self.selecionar_linha, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Rabisco", command=self.selecionar_rabisco, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Cor da borda", command=self.mudar_borda, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Cor preenchimento", command=self.mudar_preenchimento, **estilo_botao).pack(side="left")

        self.canvas = tk.Canvas(self.janela, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.controlador = ControladorDesenho(
            self.canvas,
            self.desenho,
            lambda: self.cor_borda,
            lambda: self.cor_preenchimento,
        )
        self.controlador.selecionar_ferramenta(self.ferramenta)

        self.canvas.bind("<Button-1>", self.controlador.clique)
        self.canvas.bind("<B1-Motion>", self.controlador.arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.controlador.soltar)

    def selecionar_retangulo(self):
        self.ferramenta = "retangulo"
        if self.controlador is not None:
            self.controlador.selecionar_ferramenta(self.ferramenta)

    def selecionar_oval(self):
        self.ferramenta = "oval"
        if self.controlador is not None:
            self.controlador.selecionar_ferramenta(self.ferramenta)

    def selecionar_circulo(self):
        self.ferramenta = "circulo"
        if self.controlador is not None:
            self.controlador.selecionar_ferramenta(self.ferramenta)

    def selecionar_poligono(self):
        self.ferramenta = "poligono"
        if self.controlador is not None:
            self.controlador.selecionar_ferramenta(self.ferramenta)

    def selecionar_mao_livre(self):
        self.ferramenta = "mao_livre"
        if self.controlador is not None:
            self.controlador.selecionar_ferramenta(self.ferramenta)

    def selecionar_linha(self):
        self.ferramenta = "linha"
        if self.controlador is not None:
            self.controlador.selecionar_ferramenta(self.ferramenta)

    def selecionar_rabisco(self):
        self.ferramenta = "rabisco"
        if self.controlador is not None:
            self.controlador.selecionar_ferramenta(self.ferramenta)

    def mudar_borda(self):
        self.cor_borda = escolher_cor_borda()

    def mudar_preenchimento(self):
        self.cor_preenchimento = escolher_cor_preenchimento()

    def executar(self):
        self.criar_widgets()
        self.janela.mainloop()


def iniciar():
<<<<<<< HEAD
    global janela
    global canvas
    global controlador

    janela = tk.Tk()
    janela.title("Paint OO")

    largura = 900
    altura = 600

    # Calcula a posição para abrir a janela centralizada na tela.
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    # Barra superior onde ficam os botões do programa.
    barra = tk.Frame(janela)
    barra.pack(fill="x")

    # Define um único estilo para todos os botões,
    # evitando repetir as mesmas configurações.
    estilo_botao = {
        "bg": "#ff69b4",
        "fg": "white",
        "activebackground": "#ff85c1",
        "activeforeground": "white",
        "highlightthickness": 2,
        "highlightbackground": "#ff1493",
        "highlightcolor": "#ff1493",
        "bd": 2,
        "relief": "ridge"
    }

    # Botões responsáveis por selecionar cada ferramenta de desenho.
    tk.Button(barra, text="Retângulo", command=selecionar_retangulo, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Oval", command=selecionar_oval, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Círculo", command=selecionar_circulo, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Polígono", command=selecionar_poligono, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Mão livre", command=selecionar_mao_livre, **estilo_botao).pack(side="left")
    
    tk.Button(barra, text="Linha", command=selecionar_linha, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Rabisco", command=selecionar_rabisco, **estilo_botao).pack(side="left")

    # Botões para alterar as cores da borda e do preenchimento.
    tk.Button(barra, text="Cor da borda", command=mudar_borda, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Cor preenchimento", command=mudar_preenchimento, **estilo_botao).pack(side="left")

    # Área onde as figuras serão desenhadas.
    canvas = tk.Canvas(janela, bg="white")
    canvas.pack(fill="both", expand=True)

    # Cria o controlador responsável por gerenciar os desenhos.
    instancia_desenho= Desenho()
    controlador = ControladorDesenho(
        canvas,
        instancia_desenho,
        lambda: cor_borda,
        lambda: cor_preenchimento,
    )

    controlador.selecionar_ferramenta(ferramenta)

    # Associa os eventos do mouse às funções do controlador.
    # Clique: inicia o desenho.
    # Arrastar: exibe a pré-visualização.
    # Soltar: finaliza a figura.
    canvas.bind("<Button-1>", controlador.clique)
    canvas.bind("<B1-Motion>", controlador.arrastar)
    canvas.bind("<ButtonRelease-1>", controlador.soltar)
    canvas.bind("<Double-Button-1>", controlador.finalizar_poligono)
    # Mantém a interface em execução até o usuário fechá-la.
    janela.mainloop()
=======
    InterfaceGrafica().executar()
>>>>>>> 6ed329f39d415fc1a59ca5bba8866317f92f0821
