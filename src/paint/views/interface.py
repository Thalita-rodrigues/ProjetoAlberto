import tkinter as tk

from controller.eventos import ControladorDesenho
from models.cores import escolher_cor_borda, escolher_cor_preenchimento

janela = None
canvas = None
controlador = None

# Ferramenta selecionada ao iniciar o programa.
ferramenta = "retangulo"

# Cores padrão utilizadas nos desenhos.
cor_borda = "black"
cor_preenchimento = "white"


# As funções abaixo apenas alteram a ferramenta ativa
# e informam essa mudança ao controlador.
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

def selecionar_linha():
    global ferramenta
    ferramenta = "linha"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_rabisco():
    global ferramenta
    ferramenta = "rabisco"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)

# Atualiza a cor da borda escolhida pelo usuário.
def mudar_borda():
    global cor_borda
    cor_borda = escolher_cor_borda()


# Atualiza a cor de preenchimento escolhida pelo usuário.
def mudar_preenchimento():
    global cor_preenchimento
    cor_preenchimento = escolher_cor_preenchimento()


# Responsável por criar toda a interface gráfica do programa.
def iniciar():
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
    controlador = ControladorDesenho(
        canvas,
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

    # Mantém a interface em execução até o usuário fechá-la.
    janela.mainloop()