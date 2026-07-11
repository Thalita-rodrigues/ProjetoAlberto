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
    janela.geometry("900x600")

    barra = tk.Frame(janela)
    barra.pack(fill="x")

    tk.Button(barra, text="Retângulo", command=selecionar_retangulo).pack(side="left")

    tk.Button(barra, text="Oval", command=selecionar_oval).pack(side="left")

    tk.Button(barra, text="Círculo", command=selecionar_circulo).pack(side="left")

    tk.Button(barra, text="Cor da borda", command=mudar_borda).pack(side="left")

    tk.Button(barra, text="Cor preenchimento", command=mudar_preenchimento).pack(side="left")

    canvas = tk.Canvas(janela, bg="white")
    canvas.pack(fill="both", expand=True)

    canvas.bind("<Button-1>", clique)
    canvas.bind("<B1-Motion>", arrastar)
    canvas.bind("<ButtonRelease-1>", soltar)

    janela.mainloop() 