def calcular_media(notas:list[float]) -> float:
    """Calcula a média de uma lista de notas
    
    Parâmetros:
    notas (list[float]): Lista de notas a seres calculadas
    
    Retorna:
    float: A média das notas, arredondada para uma casa decimal"""

    # verificando se é uma lista (pelo not)
    if not isinstance(notas, list):
        raise TypeError("Não é uma lista")

    # validando se a lista é vazia
    if len (notas) == 0:
        raise ValueError("Não é permitido uma lista vazia")
    
    # verificando se é uma lista (pelo not)
    if not isinstance(notas, list):
        raise TypeError("Não é uma lista")
    
    for nota in notas:
        if not isinstance(nota, (int, float)):
            raise ValueError("Nota inválida")
        
        if nota > 10:
            raise ValueError("A nota deve ser entre 0 e 10")
        
        if nota < 0:
            raise ValueError("A nota deve ser entre 0 e 10")
    
    # validando se a lista ta com um str
    # if len (notas) == "ola":
    #     raise TypeError("Nota inválida")
    
    # pega a lista de notas, calcula a media e arredonda 
    media = sum(notas)/len(notas)
    return round(media, 1)