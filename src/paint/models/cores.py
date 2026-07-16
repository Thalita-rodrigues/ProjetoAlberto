from tkinter.colorchooser import askcolor


class GerenciadorCores:
    """Classe responsável por selecionar as cores utilizadas nas figuras."""

    @staticmethod
    def escolher_cor_borda():
        """Retorna a cor da borda escolhida pelo usuário."""
        cor = askcolor()[1]

        if cor is None:
            return "black"

        return cor

    @staticmethod
    def escolher_cor_preenchimento():
        """Retorna a cor de preenchimento escolhida pelo usuário."""
        cor = askcolor()[1]

        if cor is None:
            return "white"

        return cor