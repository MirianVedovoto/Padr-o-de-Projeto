# Padrao-de-Projeto
Padrões de Projeto: Command, Factory Method e Adapter (Python)

Este repositório contém a implementação em Python de três padrões de projeto clássicos: um Comportamental (Command), um Criacional (Factory Method) e um Estrutural (Adapter). A base conceitual para os padrões segue o catálogo do Refactoring Guru (https://refactoring.guru/pt-br/design-patterns) e a literatura de referência.

AVISO DE DIREITOS AUTORAIS: O material conceitual, a classificação e as estruturas dos padrões são referenciados ao catálogo do Refactoring Guru e à literatura de Engenharia de Software.

Ferramenta de Geração (LLM) Utilizada: Este conteúdo e os exemplos de código foram gerados com o Google Gemini.


--------------------------------------------------------------------------------
1. Padrão Comportamental: Command (Comando)
Propósito
O Command (Comando) é um padrão de projeto comportamental que tem como objetivo transformar um pedido (uma operação) em um objeto independente. Esse objeto contém toda a informação necessária para a execução do pedido.
Problema que Resolve
O Command resolve o problema do acoplamento forte entre a camada que inicia uma operação (o Remetente ou GUI) e a camada que executa a operação (o Destinatário ou lógica de negócio). Sem este padrão, o código da GUI se torna dependente do código da lógica de negócio, que é mais volátil. Além disso, se a mesma operação (como Copiar/Colar) precisa ser invocada a partir de diversos locais (botões, menus, atalhos), o código tende a ser duplicado ou mal organizado.
Solução
A solução proposta pelo padrão é extrair todos os detalhes de um pedido (o objeto a ser chamado, o nome do método, argumentos) e encapsulá-los em uma classe comando separada. O objeto remetente armazena uma referência para o objeto comando e o aciona, sem precisar saber qual objeto de lógica de negócio irá receber ou processar o pedido. O comando, então, delega o trabalho ao Destinatário, usando os parâmetros que foram pré-configurados.
O padrão permite:
1. Desacoplamento entre as classes que invocam e as classes que realizam a operação.
2. Parametrizar objetos com diferentes pedidos.
3. Suportar operações reversíveis (Undo/Redo), salvando o estado da aplicação antes da execução do comando.
Estrutura (Diagrama UML Conceitual)
A estrutura do Command envolve quatro componentes principais:
1. Interface Comando: Declara o método de execução (ex: execute()).
2. Comando Concreto: Armazena a referência para um Destinatário e os parâmetros.
3. Remetente (Invoker): Inicia o pedido e armazena a referência para o Comando.
4. Destinatário (Receiver): Contém a lógica de negócio real.
classDiagram
    direction LR
    class Command {
        <<interface>>
        +execute()
    }
    class ConcreteCommandA {
        -receiver : Receiver
        +execute()
    }
    class Receiver {
        +action()
    }
    class Invoker {
        -command : Command
        +setCommand(command)
        +invoke()
    }
    
    Client --> Invoker
    Client --> Receiver
    Client --> Command
    
    Invoker --> Command : usa
    
    ConcreteCommandA ..|> Command : implementa
    
    ConcreteCommandA o--> Receiver : armazena
    ConcreteCommandA -> Receiver : delega
Exemplo de Código (Python: Editor de Texto)
Este exemplo simula botões (Remetentes) que acionam comandos para manipular um editor de texto (Destinatário).
Arquivo: command/command_editor.py
from abc import ABC, abstractmethod



--------------------------------------------------------------------------------
2. Padrão Criacional: Factory Method (Método Fábrica)
Propósito
O Factory Method é um padrão criacional que define uma interface para a criação de um objeto, mas delega às subclasses a responsabilidade de decidir qual classe instanciar.
Problema que Resolve
O padrão é usado quando o código está acoplado a classes concretas específicas dos objetos que cria, geralmente usando o operador new. Essa inflexibilidade viola o Princípio Aberto/Fechado (OCP), pois a adição de um novo tipo de produto (ex: de Caminhão para Navio) requer modificações em todo o código cliente que usa a construção direta.
Solução
A solução é substituir as chamadas diretas ao construtor por uma chamada a um método fábrica especial. Este método fábrica é declarado na classe Criadora (geralmente abstrata) e sobrescrito nas Criadoras Concretas. Cada Criador Concreto implementa o método fábrica para produzir um Produto Concreto diferente.
Dessa forma, o código cliente manipula apenas a interface abstrata do Produto, e o sistema se torna extensível: para adicionar um novo produto, basta criar uma nova subclasse Criadora e um novo Produto Concreto, sem alterar o código existente.
Estrutura (Diagrama UML Conceitual)
A estrutura do Factory Method:
1. Produto (Product): Interface que declara operações comuns.
2. Produtos Concretos (Concrete Product): Implementações do Produto.
3. Criador (Creator): Classe abstrata que declara o factoryMethod(), cujo tipo de retorno é a Interface Produto.
4. Criador Concreto (Concrete Creator): Subclasse que implementa o factoryMethod() para retornar um Produto Concreto específico.
classDiagram
    direction LR
    class Product {
        <<interface>>
        +operation()
    }
    class ConcreteProductA
    class ConcreteProductB
    
    Product <|-- ConcreteProductA
    Product <|-- ConcreteProductB
    
    class Creator {
        +anOperation()
        +factoryMethod(): Product
    }
    class ConcreteCreatorA {
        +factoryMethod(): Product
    }
    
    Creator <|-- ConcreteCreatorA
    
    ConcreteCreatorA ..> ConcreteProductA : cria
    
    Creator -> Product : usa
Exemplo de Código (Python: Logística de Transporte)
O exemplo simula um sistema de logística (Criador) que deve ser capaz de criar diferentes meios de transporte (Produto).
Arquivo: factory_method/factory_logistics.py
from abc import ABC, abstractmethod


--------------------------------------------------------------------------------
3. Padrão Estrutural: Adapter (Adaptador)
Propósito
O Adapter (Adaptador ou Wrapper) é um padrão estrutural que permite que objetos com interfaces incompatíveis colaborem entre si.
Problema que Resolve
O problema surge quando se tem uma classe útil e existente (o Serviço ou Adaptee), mas a sua interface (os nomes e a ordem dos seus métodos) não é compatível com o restante do código cliente (o Target). Não é possível ou desejável modificar a classe de serviço (seja porque é código legado, de terceiros, ou afetaria outras dependências).
Um exemplo é uma aplicação que trabalha com dados em XML, mas precisa integrar uma biblioteca de terceiros que só aceita dados em JSON.
Solução
A solução é introduzir uma classe intermediária, o Adaptador. O Adaptador implementa a Interface do Cliente (aquela esperada pelo código existente) enquanto encobre (armazena uma referência) ao objeto do Serviço incompatível. Quando o cliente chama um método do Adaptador, o Adaptador traduz a chamada para o formato e ordem que o Serviço espera.
O Adaptador funciona como um tradutor universal, fazendo com que o objeto cliente não precise mudar sua lógica para se adequar ao objeto incompatível. Uma analogia real é o adaptador de tomada, que permite que um plugue incompatível funcione em uma tomada diferente.
Estrutura (Diagrama UML Conceitual - Adaptador de Objeto)
A implementação de Adaptador de Objeto é a mais comum e usa composição (o Adaptador encobre o Serviço).
1. Interface do Cliente (Target): Interface que o código cliente espera usar.
2. Cliente: Classe que usa o sistema através da Interface do Cliente.
3. Serviço (Adaptee): A classe útil, mas com interface incompatível.
4. Adaptador: Implementa a Interface do Cliente e armazena uma referência ao Serviço, traduzindo as chamadas.
classDiagram
    direction LR
    class Client
    class ClientInterface {
        <<interface>>
        +request()
    }
    class Adapter {
        +request()
        -service : Service
    }
    class Service {
        +specificRequest()
    }

    Client --> ClientInterface : usa
    Adapter ..|> ClientInterface : implementa
    Adapter o--> Service : armazena
    Adapter -> Service : traduz e chama
Exemplo de Código (Python: Pinos e Buracos)
Este exemplo é baseado na analogia clássica de adaptar Pinos Quadrados (Serviço) para caberem em Buracos Redondos (Interface do Cliente).
Arquivo: adapter/adapter_pegs.py
import math

