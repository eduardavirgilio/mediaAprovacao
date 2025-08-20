import pytest
from escola.aluno import calcular_media

# lista vazia -------------------------------------
def test_calcular_media_lista_vazia():
    #definindo a entrada
    entrada = []

    #executando a função e esperando erro
    with pytest.raises(ValueError, match="Não é permitido uma lista vazia"):
        calcular_media(entrada)

# nao é uma lista -------------------------------------
def test_calcular_media_enviando_string():
    #definindo a entrada
    entrada = "ola"

    #executando a função e esperando erro
    with pytest.raises(TypeError, match="Não é uma lista"):
        calcular_media(entrada)

def test_calcular_media_enviando_string_dentro_da_lista():
    #definindo a entrada
    entrada = [(3, 8), 20]

    #executando a função e esperando erro
    with pytest.raises(ValueError, match="Nota inválida"):
        calcular_media(entrada)

def test_calcular_media_enviando_nota_maior_que_dez():
    #definindo a entrada
    entrada = [11]

    #executando a função e esperando erro
    with pytest.raises(ValueError, match="A nota deve ser entre 0 e 10"):
        calcular_media(entrada)

def test_calcular_media_enviando_nota_menor_que_zero():
    #definindo a entrada
    entrada = [-11]

    #executando a função e esperando erro
    with pytest.raises(ValueError, match="A nota deve ser entre 0 e 10"):
        calcular_media(entrada)