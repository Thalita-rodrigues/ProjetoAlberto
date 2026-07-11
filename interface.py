# janela,canvas e toolbar
import tkinter as tk

from eventos import clique, arrastar, soltar
from cores import escolher_cor_borda, escolher_cor_preenchimento

janela = None
canvas = None

ferramenta = "retangulo"

cor_borda = "black"
cor_preenchimento = "white"


def selecionar_retangulo():
    global ferramenta
    ferramenta = "retangulo"


def selecionar_oval():
    global ferramenta
    ferramenta = "oval"


def selecionar_circulo():
    global ferramenta
    ferramenta = "circulo"


def mudar_borda():
    global cor_borda
    cor_borda = escolher_cor_borda()


def mudar_preenchimento():
    global cor_preenchimento
    cor_preenchimento = escolher_cor_preenchimento()


def iniciar():
    global janela
    global canvas

    janela = tk.Tk()
    janela.title("Paint Imperativo")

    largura = 900
    altura = 600
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    barra = tk.Frame(janela)
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
        "relief": "ridge"
    }

    tk.Button(barra, text="Retângulo", command=selecionar_retangulo, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Oval", command=selecionar_oval, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Círculo", command=selecionar_circulo, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Cor da borda", command=mudar_borda, **estilo_botao).pack(side="left")

    tk.Button(barra, text="Cor preenchimento", command=mudar_preenchimento, **estilo_botao).pack(side="left")

    canvas = tk.Canvas(janela, bg="white")
    canvas.pack(fill="both", expand=True)

    canvas.bind("<Button-1>", clique)
    canvas.bind("<B1-Motion>", arrastar)
    canvas.bind("<ButtonRelease-1>", soltar)

    janela.mainloop() 