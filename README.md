# Projeto de Programação A - 2026.1

Projeto de desenho em Python com Tkinter, inspirado em apps como Google Drawings e LibreOffice Draw.

## Objetivo
Construir uma aplicação gráfica para desenhar formas em um canvas, evoluindo o projeto ao longo de entregas com refatorações e aplicação de padrões.

## Tecnologias
- Python 3
- Tkinter
- Git e GitHub para versionamento e trabalho em equipe

## Estrutura atual do projeto
- main.py: ponto de entrada da aplicação.
- interface.py: cria a janela, barra de botões, canvas e liga o controlador de desenho.
- eventos.py: concentra o controlador OO que trata clique, arraste e soltura do mouse.
- figuras.py: classe base Figura e subclasses para retângulo, oval, círculo, polígono e mão livre.
- desenho.py: funções legadas de desenho mantidas no histórico do projeto.
- cores.py: seleção de cor da borda e de preenchimento com paleta do sistema.

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