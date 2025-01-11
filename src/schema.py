"""Schema de dados para contrato de funcionário."""

from pydantic import BaseModel

class ContratoFuncionario(BaseModel):
    """Classe responsável por representar o contrato de funcionário."""
    id: int
    nome: str
    cargo: str
    salario: float
    data_contratacao: str
    email: str
    telefone: str
    endereco: str
    cep: str
    cidade: str
    estado: str
    pais: str
    departamento: str
    
    