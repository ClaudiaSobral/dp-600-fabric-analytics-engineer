# Laboratório - Discover and connect to data in OneLake

## Objetivos

- Criar um lakehouse contendo dados de venda
- Criar shortcuts para acesso entre workspaces
- Fazer *queries* por SQL endpoints
- Explorar modelos semânticos

1. Criei um workspace
2. Lakehouse
3. Subi um arquivo .csv no lakehouse
4. Carreguei ele em tabela
5. Criei um shortcut para acessar dados de outro lakehouse sem criar uma cópia
6. Fiz uma consulta em ao endpoint do lakehouse com T-SQL
7. Criei um modelo semântico
8. Fiz uma visualização com o modelo semântico

## O que aprendi

- O registro de transações pode ser recuperado no arquivo _delta_log
- Aprendi a diferença de um workspace para um lakehouse: workspaces contêm lakehouses como se fossem pequenos bancos de dados dentro de um ambiente.
- Aprendi a fazer e identificar um shortcut
- Todo lakehouse apresenta um endpoint de acesso com T-SQL read-only

## Dificuldades e como resolvi

- Tive dificuldade em localizar as instruções com as mudanças de interface do tutorial para o Microsoft Fabric atual, mas li com cuidado e encontrei as instruções pelo nome