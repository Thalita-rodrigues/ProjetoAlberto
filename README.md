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
- interface.py: cria a janela, barra de botões, canvas e conecta eventos do mouse.
- eventos.py: trata clique, arraste e soltura do mouse, incluindo pré-visualização das figuras.
- desenho.py: funções responsáveis por desenhar retângulo, oval e círculo no canvas.
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

```bash
python main.py
```

## Entrega 2 - OO.1 (visão geral)
Próxima fase prevista para migrar a solução imperativa para orientação a objetos.

Planejamento geral:
- Criar hierarquia de classes para figuras.
- Reorganizar o código para uso dessas classes.
- Incluir novos tipos de desenho, como polígonos.
- Melhorar separação em módulos.

## Entrega 3 - OO.MVC.1 (visão geral)
Etapa focada em organizar a aplicação com padrão MVC.

Planejamento geral:
- Definir classes de modelo para representar dados e figuras.
- Definir camadas de visão para interface.
- Definir controladores para lógica de interação.
- Estruturar melhor pastas e responsabilidades do projeto.

## Entrega 4 - OO.State.1 (planejada)
Etapa futura para reduzir condicionais no controle usando padrão State, além de suporte a salvar e abrir desenhos.