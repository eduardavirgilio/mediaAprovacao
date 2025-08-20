from aluno.aluno import calcular_media
from aluno.aprovacao import verificar_aprovacao

def verificar_aprovacao(notas: list[float]) -> float:

    media = calcular_media(notas)

    aprovacao = verificar_aprovacao(media)

    return aprovacao
    