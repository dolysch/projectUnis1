def converter_idade(dias_totais):

    anos = dias_totais // 365
    dias_restantes = dias_totais % 365
    meses = dias_restantes // 30
    dias = dias_restantes % 30

    return anos, meses, dias

dias_totais = int(input("Digite a idade em dias: "))

anos, meses, dias = converter_idade(dias_totais)

print(f"A idade é {anos} anos, {meses} meses e {dias} dias.")
