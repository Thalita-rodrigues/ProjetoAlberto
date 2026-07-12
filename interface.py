import tkinter as tk

from eventos import ControladorDesenho
from cores import escolher_cor_borda, escolher_cor_preenchimento

janela = None
canvas = None
controlador = None

ferramenta = "retangulo"

cor_borda = "black"
cor_preenchimento = "white"


def selecionar_retangulo():
    global ferramenta
    ferramenta = "retangulo"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_oval():
    global ferramenta
    ferramenta = "oval"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_circulo():
    global ferramenta
    ferramenta = "circulo"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_poligono():
    global ferramenta
    ferramenta = "poligono"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_mao_livre():
    global ferramenta
    ferramenta = "mao_livre"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def mudar_borda():
    global cor_borda
    cor_borda = escolher_cor_borda()


def mudar_preenchimento():
    global cor_preenchimento
    cor_preenchimento = escolher_cor_preenchimento()


def iniciar():
    global janela
    global canvas
    global controlador

    janela = tk.Tk()
    janela.title("Paint OO")

    largura = 900
    altura = 600
    # Centraliza a janela na tela.
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    barra = tk.Frame(janela)
    barra.pack(fill="x")

    # Estilo único aplicado em todos os botões da barra.
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

    tk.Button(barra, text="Retângulo", command=selecionar_retangulo, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Oval", command=selecionar_oval, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Círculo", command=selecionar_circulo, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Polígono", command=selecionar_poligono, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Mão livre", command=selecionar_mao_livre, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Cor da borda", command=mudar_borda, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Cor preenchimento", command=mudar_preenchimento, **estilo_botao).pack(side="left")

    canvas = tk.Canvas(janela, bg="white")
    canvas.pack(fill="both", expand=True)

    controlador = ControladorDesenho(
        canvas,
        lambda: cor_borda,
        lambda: cor_preenchimento,
    )
    controlador.selecionar_ferramenta(ferramenta)

    # Liga os eventos do mouse para desenhar no canvas.
    canvas.bind("<Button-1>", controlador.clique)
    canvas.bind("<B1-Motion>", controlador.arrastar)
    canvas.bind("<ButtonRelease-1>", controlador.soltar)

    janela.mainloop()