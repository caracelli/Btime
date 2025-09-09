from dataclasses import dataclass

@dataclass
class Moeda:
    rank: int
    simbolo: str
    nome: str
    preco: float
    valor_mercado: float
    variacao_24h: float
    volume_24h: float
