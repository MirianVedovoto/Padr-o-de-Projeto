# 2. Interface do Cliente (Target): O que o cliente espera
class RoundPeg:
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

# 3. Cliente: O Buraco Redondo só aceita pinos RoundPeg
class RoundHole:
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def fits(self, peg: RoundPeg) -> bool:
        """Verifica se o pino (RoundPeg) cabe no buraco."""
        return self.get_radius() >= peg.get_radius()

# 1. Serviço (Adaptee): A interface incompatível
class SquarePeg:
    def __init__(self, width: float):
        self.width = width

    def get_width(self) -> float:
        return self.width

# 4. Adaptador: Implementa a interface RoundPeg e encobre SquarePeg
class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg):
        # O adaptador encobre o objeto SquarePeg
        self.peg = peg
        # RoundPeg precisa de um construtor, mas passamos um valor fictício (0)
        super().__init__(0) 
    
    def get_radius(self) -> float:
        """
        Calcula o raio mínimo necessário para o pino quadrado caber (metade da diagonal).
        Isso é a TRADUÇÃO/ADAPTAÇÃO da interface.
        """
        # Fórmula: Largura * sqrt(2) / 2
        result = self.peg.get_width() * math.sqrt(2) / 2
        return result

# CLIENTE (Uso)
if __name__ == "__main__":
    hole = RoundHole(5.0) # Buraco de Raio 5
    
    # Testando com um pino redondo compatível
    rpeg = RoundPeg(5.0)
    print(f"Pino Redondo (Raio 5) cabe? {hole.fits(rpeg)}")
    # Output: True

    # Criando pinos quadrados incompatíveis
    small_sq_peg = SquarePeg(7.0) # Diagonal/2: 4.95
    large_sq_peg = SquarePeg(10.0) # Diagonal/2: 7.07
    
    # O cliente não pode usar o pino quadrado diretamente: hole.fits(small_sq_peg) - ERRO
    
    # Usando o Adaptador
    small_sq_peg_adapter = SquarePegAdapter(small_sq_peg)
    large_sq_peg_adapter = SquarePegAdapter(large_sq_peg)
    
    # Agora o Cliente (RoundHole) interage com o Adaptador, pensando que é um RoundPeg
    print(f"Pino Quadrado 7.0 (Raio adaptado: {small_sq_peg_adapter.get_radius():.2f}) cabe? {hole.fits(small_sq_peg_adapter)}")
    # Output: True (4.95 <= 5.0)
    
    print(f"Pino Quadrado 10.0 (Raio adaptado: {large_sq_peg_adapter.get_radius():.2f}) cabe? {hole.fits(large_sq_peg_adapter)}")
    # Output: False (7.07 > 5.0)