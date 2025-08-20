# pip install pytest-cov

def verificar_aprovacao(notas: float) -> str:
    
    # Validando se a lista é vazia
    # if notas == 0:
    #     raise ValueError("Não é permitido uma lista vazia")
  
    # Validando se todos os elementos da lista são numeros (int e float)
    if not isinstance(notas, (int, float)):
        raise TypeError("Não é permitido uma string na lista")
        
        # Validando os limites da nota 
    if notas > 10:
        raise ValueError("Limite da nota [0, 10]")
        
    if notas < 0:
        raise ValueError("Limite da nota [0, 10]")

        # Validando as aprovações
    if notas >= 7.0:
        return "APROVADO"
        
    if notas < 6.9 and notas > 5.0:
        return "RECUPERAÇÃO"
        
    if notas < 4.9:
        return "REPROVADO"