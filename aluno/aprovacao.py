# pip install pytest-cov

def verificar_aprovacao(notas: list[float]) -> float:

    # Validando se há uma lista
    if not isinstance(notas, list):
        raise TypeError("Nota invalida")
    
    # Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Não é permitido uma lista vazia")

  
    for nota in notas:  
        # Validando se todos os elementos da lista são numeros (int e float)
        if not isinstance(nota, (int, float)):
            raise TypeError("Não é permitido uma string na lista")
        
        # Validando os limites da nota 
        if nota > 10:
            raise ValueError("Limite da nota [0, 10]")
        
        if nota < 0:
            raise ValueError("Limite da nota [0, 10]")

        # Validando as aprovações
        if nota >= 7.0:
            return "APROVADO"
        
        if nota < 6.9 and nota > 5.0:
            return "RECUPERAÇÃO"
        
        if nota < 4.9:
            return "REPROVADO"

