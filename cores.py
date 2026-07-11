def escolher_cor_borda():
    """Abre a paleta de cores para o contorno e retorna a cor em formato hexadecimal.
    Se a seleção for cancelada, retorna 'black' como cor padrão.
    """
    # askcolor() retorna (rgb, hex). Usamos [1] para extrair apenas a string hexadecimal.
    cor = askcolor()[1]
    # Trata o caso onde o usuário fecha a janela ou clica em Cancelar
    if cor is None:
        return "black"

    return cor


def escolher_cor_preenchimento():
    """Abre a paleta de cores para o preenchimento e retorna a cor em formato hexadecimal.
    Se a seleção for cancelada, retorna 'white' como cor padrão.
    """
    # Abre o seletor de cores do sistema para o preenchimento da figura
    cor = askcolor()[1]
    # Trata o caso de cancelamento definindo a cor padrão como branco

    if cor is None:
        return "white"

    return cor
