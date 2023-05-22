'''Construir um algoritmo que solicite o código do cargo do funcionário e mostre o nome do cargo,
o salário atual e qual será o novo salário do funcionário, de acordo com o quadro abaixo.

    ################################################################################
    #  Código   #      Descrição         #  Salário atual  #  Percentual de aumento#
    ################################################################################
    #    1       #  Analista de Sistemas #    8.000,00     #         20%           #
    #    2       #  Programador          #    10.000,00    #         30%           #
    #    3       #  Gerente de Redes     #    15.000,00    #         15%           #
    #    4       #  Gerente de TI        #    20.000,00    #         30%           #
    #################################################################################
'''

print("Selecione uma das Opções\n"
      "1 - Analista de Sistemas\n"
      "2 - Programador\n"
      "3 - Gerente de Redes\n"
      "4 - Gerente de TI")
Analista_de_Sistemas = float(8000.00)
Programador = float(10000.00)
Gerente_de_Redes = float(15000.00)
Gerente_de_TI = float(20000.00)
codigo = int(input("Informe o código do cargo: "))
match codigo:
    case 1:
        novo_salario = Analista_de_Sistemas + (Analista_de_Sistemas * 20/100)
        print("Analista de Sistemas\n"
              "Salario Atual R$ 8.000\n"
              f"Novo Salário R$ {novo_salario:.2f}")
    case 2:
        novo_salario = Programador + (Programador * 30 / 100)
        print("Programador\n"
              "Salario Atual R$ 10.000\n"
              f"Novo Salário R$ {novo_salario:.2f}")
    case 3:
        novo_salario = Gerente_de_Redes + (Gerente_de_Redes * 15 /100)
        print("Gerente de Redes\n"
              "Salario Atual R$ 15000\n"
              f"Novo Salário R$ {novo_salario:.2f}")
    case 4:
        novo_salario = Gerente_de_TI + (Gerente_de_TI * 30 / 100)
        print("Gerente de TI\n"
             "Salario Atual R$ 20.000\n"
             f"Novo Salário R$ {novo_salario:.2f}")

    case _:
        print("Saindo...")
