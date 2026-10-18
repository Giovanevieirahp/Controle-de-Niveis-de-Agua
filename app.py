from colorama import Fore, Style
Reservatorio_cheio = float(input("Insira a capacidade do resevatorio(L)"))
Reservatorio_Atual = float(input("Insira o nivel atual do reservatorio(L)"))
Reservatorio_relativo = Reservatorio_Atual/ Reservatorio_cheio

if Reservatorio_relativo > 1:
    print(Fore.RED + "ERRO!")
    print("Verifique os valores e tente Novamente")
elif Reservatorio_relativo > 0.95:
    print(Fore.RED + "Nivel de Agua Muito Alto!")
elif Reservatorio_relativo > 0.6:
    print(Fore.YELLOW + "Nivel de Agua alto")
elif Reservatorio_relativo > 0.4:
    print(Fore.GREEN + "Nivel de Agua Medio")
elif Reservatorio_relativo > 0.05:
    print(Fore.BLUE + "Nivel de Agua baixo")
elif Reservatorio_relativo >= 0:
    print(Fore.CYAN + "Nivel de Agua Muito Baixo")
else:
    print(Fore.RED + "ERRO!")
    print("Verifique os valores e tente Novamente")

print(Style.RESET_ALL)