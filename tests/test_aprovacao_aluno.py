import pytest
from aluno.aprovacao import verificar_aprovacao


def test_string_lista():
    # Definindo a entrada
    entrada = "ola"

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="Não é permitido uma string na lista"):
        verificar_aprovacao(entrada) 

def test_num_negativo():
    # Definindo a entrada
    entrada = -10.0

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="Limite da nota \[0, 10\]"):
        verificar_aprovacao(entrada) 

def test_num_maiordeDez():
    # Definindo a entrada
    entrada = 11.0

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="Limite da nota \[0, 10\]"):
        verificar_aprovacao(entrada) 