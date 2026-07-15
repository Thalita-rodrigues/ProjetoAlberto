# Projeto de Programação A - 2026.1

Projeto de desenho em Python com Tkinter, inspirado em apps como Google Drawings e LibreOffice Draw.

## Objetivo
Construir uma aplicação gráfica para desenhar formas em um canvas, evoluindo o projeto ao longo de entregas com refatorações e aplicação de padrões.

## Tecnologias
- Python 3
- Tkinter
- Git e GitHub para versionamento e trabalho em equipe

## Estrutura ATUAL do projeto
O projeto está organizado seguindo o padrão Model-View-Controller (MVC), separando a lógica da aplicação em três camadas principais:

### models/
Responsável pelas regras de negócio e representação dos dados da aplicação.

- figuras.py → Define as classes das figuras geométricas (Retângulo, Oval, Círculo, Linha, Rabisco, etc.).
- desenho.py → Gerencia os desenhos criados no canvas.
- cores.py → Gerencia as cores de borda e preenchimento utilizadas pelas figuras.

### views/
Responsável pela interface gráfica da aplicação.

- interface.py → Cria a janela principal, o canvas e os componentes visuais.

### controller/
Responsável por intermediar a comunicação entre a interface e o modelo.

- eventos.py → Trata os eventos do mouse e executa as ações de desenho.
- controlador.py → Gerencia a lógica das ferramentas disponíveis e coordena a interação entre View e Model.

## Entrega 1 - imperativa.1
Nesta etapa, o foco foi a versão imperativa funcional do paint.

Funcionalidades implementadas:
- Desenho de retângulos.
- Desenho de ovais.
- Desenho de círculos.
- Escolha de cor da borda para cada desenho.
- Escolha de cor de preenchimento para cada desenho.
- Pré-visualização da figura durante o arraste.

Aspectos de interface já aplicados:
- Janela centralizada na tela.
- Barra de ferramentas com botões de seleção de forma e cores.

### Como executar
1. Abra a pasta do projeto no terminal.
2. Execute:

bash
python main.py


## Entrega 2 - OO.1
Refatoração concluída para uma abordagem orientada a objetos.

Funcionalidades implementadas nesta entrega:
- Hierarquia de classes com Figura como classe base.
- Subclasses para retângulo, oval, círculo, polígono regular e mão livre.
- Controlador OO para pré-visualização e desenho final no canvas.
- Separação das figuras em módulo próprio.
- Novos tipos de desenho: polígono e mão livre.
- Adicionamos linhas e rabiscos

Organização resultante:
- As figuras sabem desenhar a própria prévia e a versão final.
- A interface monta a janela e delega a interação ao controlador.
- O fluxo de desenho deixou de depender de condicionais espalhadas em vários pontos.

## Entrega 3 - OO.MVC.1 (visão geral)
Etapa focada em organizar a aplicação com padrão MVC.

Planejamento geral:
- Definir classes de modelo para representar dados e figuras.
- Definir camadas de visão para interface.
- Definir controladores para lógica de interação.
- Estruturar melhor pastas e responsabilidades do projeto.

## Entrega 4 - OO.State.1 (planejada)
Etapa futura para reduzir condicionais no controle usando padrão State, além de suporte a salvar e abrir desenhos.