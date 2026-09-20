# Secure and govern analytics data in Microsoft Fabric
Este learning path contém 3 módulos que, juntos, preparam para o exame DP-600: Fabric Analytics Engineer:

1. 🟢 [Secure data access in Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/secure-data-access-in-fabric/) 

- Objetivos do módulo:
    - Descrever modelos de segurança no Microsoft Fabric e suas camadas de acesso;
    - Configurar papéis (roles) de workspaces e permissões de itens
    - Aplicar permissões granulares usando papéis de segurança T-SQL e permissões de itens

## Três níveis de acesso

1. Autenticação com ID Microsoft Entra: checa se o usuário pode autenticar
2. Acesso ao Fabric: checa se usuário tem acesso ao Fabric
3. Segurança de dados: avalia se o usuário pode fazer determinada ação com uma tabela ou arquivo

A terceira camada tem quatro controles de acesso primários, do mais amplo para o mais específico:
- Papéis de workspace: dão acesso ao lakehouse inteiro. São quatro tipos de permissão - Admin, Member, Contributor e Viewer

Tipo de permissão | Ver | Criar | Modificar | Compartilhar | Administrar itens | Administrar permissões
--------- | :---------: | :------: | :------: | :------: | :------: | :------: 
Admin | ✅ | ✅ | ✅ | ✅ | ✅ | ✅
Member | ✅ | ✅ | ✅ | ✅ | ✅ | ❌
Contributor | ✅ | ✅ | ✅ | ❌ | ❌ | ❌
Viewer | ✅ | ❌ | ❌ | ❌ | ❌ | ❌


- Permissões de itens
- Permissões granulares ou de computação
- Segurança OneLake

2. 🟡 [Secure a Microsoft Fabric data warehouse](https://learn.microsoft.com/en-us/training/modules/secure-data-warehouse-in-microsoft-fabric/)

- Objetivos do módulo:
    - Aprender a como aplicar segunrança em workspaces de uma data warehouse

- Camadas de segurança
    - Papéis de workspace: Admin, member, contributor e viewer são a primeira linha de segurança a acesso aos itens de um workspace
    - Permissões de itens: você pode permitir acesso apenas a warehouse de interesse para consumo downstream sem precisar conceder acesso a tudo
    - Proteção de dados: T-SQL fornece a possibilidade de conceder acesso granular extremamente focado a nível de linha, coluna e objeto (esse é o foco principal do módulo)
    - Auditar logs: SQL audit logs capturam a atividade dos usuários, incluindo logins, queries e mudanças de permissão. Isso pode ser feito através do Microsoft Purview e do PowerShell. Auditar é essencial para compliance
    - Encriptação: todo warehouse é encriptado em repouso utilizando chaves gerenciadas pela Microsoft. Para maior controle, usar CMK (chaves gerenciadas pelo cliente) com o Azure Key Vault.

3. 🔴 [Govern analytics data in Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/fabric-govern-analytics-data/)