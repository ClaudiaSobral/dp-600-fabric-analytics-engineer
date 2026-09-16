# Prepare AI-ready analytics data in Microsoft Fabric

Este repositório documenta meu progresso no Learning Path da Microsoft Learn:

Este learning paths contém 3 módulos que, juntos, preparam para o exame DP-600: Fabric Analytics Engineer:

1. [Prepare semantic models for AI in Power BI and Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/fabric-prepare-semantic-layer/)
 
**Resumo do módulo**: o Copilot pode auxiliar fazendo *queries* quando perguntado em linguagem natural. Para isso, ele faz uma *model reduction*, selecionando apenas os campos que considera importante para responder a uma pergunta.

Ainda assim, é preciso que o schema da gold layer (no schema Medallion, temos as camadas bronze, silver e golden) tenha um design claro para não criar ambiguidades para a IA. Ou seja, é importante diferencias colunas como "CidadeCliente" e "CidadeLoja", fornecendo o contexto certo para a IA.

Ainda podemos ocultar campos técnicos, como chaves primárias, para facilitar essa consulta.

Para obter um bom desempenho do Copilot, podemos fornecer um schema IA, auxiliado por regras de negócio nas instruções, além de atrelar um visual a esse tipo de consulta frequente. Tudo isso deve ser testado.

Ontologia: o FabricIQ pode ser útil para criar uma ontologia quando temos times diferentes com definições iguais dos termos. A ontologia cria tipos de entidade, tipos de relacionamento e propriedades de coluna a partir de modelos semânticos - tudo isso deve ser revisado. O modelo deve ser estável para criar uma ontologia. O modelo deve estar habilitado no modo DirectLake.

Validação da IA: a testagem pode ser feita fazendo perguntas típicas de tomada de decisão. É importante fazer a mesma pergunta de várias formas para o Copilot e avaliar a consistência. Quando o Copilot erra, pode-se verificar o processo da IA através de "como o Copilot chegou nessa decisão". Assim, é possível verificar o que deu errado e corrigir. Alguns fixes comuns podem ser: adicionar regras de negócio na IA, remover campos técnicos do modelo semântico IA, adicionar um sinônimo a uma frase que a IA não conhece, melhorar nomes e descrições dos campos analisados etc. É importante documentar o que a IA não cobre, para que o time não pense que a IA é uma fonte ilimitada de verdade.

2. [Understand Microsoft Fabric IQ fundamentals](https://learn.microsoft.com/en-us/training/modules/understand-fabric-iq-fundamentals/)

**Resumo do módulo**:
