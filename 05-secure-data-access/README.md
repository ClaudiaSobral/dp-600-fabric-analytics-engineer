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

2. 🔴 [Secure a Microsoft Fabric data warehouse](https://learn.microsoft.com/en-us/training/modules/secure-data-warehouse-in-microsoft-fabric/)

3. 🔴 [Govern analytics data in Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/fabric-govern-analytics-data/)