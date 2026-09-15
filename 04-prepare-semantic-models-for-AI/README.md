# Prepare AI-ready analytics data in Microsoft Fabric

Este repositório documenta meu progresso no Learning Path da Microsoft Learn:

Este learning paths contém 3 módulos que, juntos, preparam para o exame DP-600: Fabric Analytics Engineer:

1. [Prepare semantic models for AI in Power BI and Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/fabric-prepare-semantic-layer/)
**Resumo do módulo**: o Copilot pode auxiliar fazendo *queries* quando perguntado em linguagem natural. Para isso, ele faz uma *model reduction*, selecionando apenas os campos que considera importante para responder a uma pergunta.
Ainda assim, é preciso que o schema da gold layer (no schema Medallion, temos as camadas bronze, silver e golden) tenha um design claro para não criar ambiguidades para a IA. Ou seja, é importante diferencias colunas como "CidadeCliente" e "CidadeLoja", fornecendo o contexto certo para a IA.
Ainda podemos ocultar campos técnicos, como chaves primárias, para facilitar essa consulta.

3. 
