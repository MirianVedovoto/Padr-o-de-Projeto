# 1. Interface Produto (Transporte)
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

# 2. Produtos Concretos
class Truck(Transport):
    def deliver(self) -> str:
        return "Entrega por terra usando um Caminhão."

class Ship(Transport):
    def deliver(self) -> str:
        return "Entrega por mar usando um Navio porta-containers."

# 3. Criador Abstrato (Logistics)
class Logistics(ABC):
    
    @abstractmethod
    def create_transport(self) -> Transport:
        """O Factory Method: Subclasses decidem qual produto instanciar."""
        pass

    def plan_delivery(self) -> str:
        """Lógica de negócio que usa o Produto.
        Esta lógica é independente da classe concreta do Produto."""
        transport = self.create_transport()
        result = f"Logística: Preparando a entrega.\n"
        result += f"Logística: O transporte escolhido fará a entrega: {transport.deliver()}"
        return result

# 4. Criadores Concretos
class RoadLogistics(Logistics):
    # Implementa o método fábrica para criar um Truck
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    # Implementa o método fábrica para criar um Ship
    def create_transport(self) -> Transport:
        return Ship()

# CLIENTE (Uso)
def client_code(creator: Logistics):
    """O código cliente trabalha com o Criador Abstrato (Logistics)."""
    print(client_code) # Simula o cliente usando o serviço
    print(creator.plan_delivery())

if __name__ == "__main__":
    print("--- Cenário 1: Logística Terrestre ---")
    road_logistics = RoadLogistics()
    client_code(road_logistics)

    print("\n--- Cenário 2: Logística Marítima ---")
    sea_logistics = SeaLogistics()
    client_code(sea_logistics)