from desenho import desenhar_retangulo
from desenho import desenhar_oval
from desenho import desenhar_circulo
import interface

x_inicial = 0
y_inicial = 0

preview = None


def clique(evento):
    global x_inicial
    global y_inicial

    # Guarda o ponto inicial do desenho.
    x_inicial = evento.x
    y_inicial = evento.y


def arrastar(evento):
    global preview

    # Remove a prévia anterior antes de desenhar a nova.
    if preview is not None:
        interface.canvas.delete(preview)

    if interface.ferramenta == "retangulo":
        preview = interface.canvas.create_rectangle(
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            outline=interface.cor_borda,
            fill=interface.cor_preenchimento,
            stipple="gray50",
            dash=(4, 2)
        )

    elif interface.ferramenta == "oval":
        preview = interface.canvas.create_oval(
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            outline=interface.cor_borda,
            fill=interface.cor_preenchimento,
            stipple="gray50",
            dash=(4, 2)
        )

    elif interface.ferramenta == "circulo":
        # Mantém largura e altura iguais para formar um círculo.
        raio = min(abs(evento.x - x_inicial), abs(evento.y - y_inicial))

        if evento.x < x_inicial:
            x_final = x_inicial - raio
        else:
            x_final = x_inicial + raio

        if evento.y < y_inicial:
            y_final = y_inicial - raio
        else:
            y_final = y_inicial + raio

        preview = interface.canvas.create_oval(
            x_inicial,
            y_inicial,
            x_final,
            y_final,
            outline=interface.cor_borda,
            fill=interface.cor_preenchimento,
            stipple="gray50",
            dash=(4, 2)
        )


def soltar(evento):
    global preview

    # Limpa a prévia e desenha a forma final.
    if preview is not None:
        interface.canvas.delete(preview)
        preview = None

    if interface.ferramenta == "retangulo":
        desenhar_retangulo(
            interface.canvas,
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            interface.cor_borda,
            interface.cor_preenchimento
        )

    elif interface.ferramenta == "oval":
        desenhar_oval(
            interface.canvas,
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            interface.cor_borda,
            interface.cor_preenchimento
        )

    elif interface.ferramenta == "circulo":
        desenhar_circulo(
            interface.canvas,
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            interface.cor_borda,
            interface.cor_preenchimento
        )