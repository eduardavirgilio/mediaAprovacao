import pytest
from aluno.aprovacao import verificar_aprovacao

@pytest.mark.parametrize("entrada, situacao_esperada",
                         [
                             ([8.0], "APROVADO"),
                             ([6.5], "RECUPERAÇÃO"),
                             ([4.0], "REPROVADO")
                         ])

def test_calcular_aprovacao_parametrizados(entrada, situacao_esperada):
    resultado = verificar_aprovacao(entrada)

    assert resultado == situacao_esperada