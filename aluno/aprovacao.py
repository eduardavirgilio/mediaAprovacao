def verificar_aprovacao_unica(media: float) -> str:
    # Valida se a entrada é um número (int ou float)
    if not isinstance(media, (int, float)):
        raise TypeError("A média deve ser um número (inteiro ou float).")

    # Valida os limites da média
    if not 0 <= media <= 10:
        raise ValueError("A média deve estar entre 0 e 10.")

    # Verifica a aprovação
    if media >= 7.0:
        return "APROVADO"
    elif media >= 5.0:  # O critério original (nota < 6.9 and nota > 5.0) é problemático. Esta é uma versão mais robusta.
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"