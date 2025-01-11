"""Arquivo de teste do schema de dados."""

import pytest
from pydantic import ValidationError
from scr.schema import ContratoFuncionario

def test_validar_contrato():
    dados_validos = {
        "id": 1,
        "nome": "John Doe",
        "cargo": "Developer",
        "salario": 5000.0,
        "data_contratacao": "2022-01-01,
        "email": "Hs2dC@example.com",
        "telefone": "123456789",
        "endereco": "123 Main St, Anytown, USA",
        "cep": "12345-678",
        "cidade": "Anytown",
        "estado": "US",
        "pais": "United States",
        "departamento": "IT",
    }
    
    funcionario = ContratoFuncionario(**dados_validos)
    
    assert funcionario.id == dados_validos["id"]
    assert funcionario.nome == dados_validos["nome"]
    assert funcionario.cargo == dados_validos["cargo"]
    assert funcionario.salario == dados_validos["salario"]
    assert funcionario.data_contratacao == dados_validos["data_contratacao"]
    assert funcionario.email == dados_validos["email"]
    assert funcionario.telefone == dados_validos["telefone"]
    assert funcionario.endereco == dados_validos["endereco"]
    assert funcionario.cep == dados_validos["cep"]
    assert funcionario.cidade == dados_validos["cidade"]
    assert funcionario.estado == dados_validos["estado"]
    assert funcionario.pais == dados_validos["pais"]
    assert funcionario.departamento == dados_validos["departamento"]