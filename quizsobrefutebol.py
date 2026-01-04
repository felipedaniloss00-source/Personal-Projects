print("Seja bem-vindo ao quiz n1!")
answer_user = input("Voce deseja começar o quiz? (Sim/Não)")

if answer_user != "Sim":
    quit()

score = 0

print("Começando")
print("Qual time mais vezes venceu a Champions League? \n (A) Real Madrid \n (B) Barcelona \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("\033[32mACERTOU!\033[0m")
    score = score + 1
else:
    print("\033[31mErrou!\033[0m")

print("Qual destes jogadores mais venceu a Champion League? \n (A) Modric \n (B) CR7 \n (C) Messi \n")
answer_2 = input("Resposta: ")

if answer_2 == "A":
    print("\033[32mACERTOU!\033[0m")
    score = score + 1
else:
    print("\033[31mErrou!\033[0m")

print("Qual seleção tem mais copas do mundo? \n (A) Alemanha \n (B) França \n (C) Brasil \n")
answer_3 = input("Resposta: ")

if answer_3 == "C":
    print("\033[32mACERTOU!\033[0m")
    score = score + 1
else:
    print("\033[31mErrou!\033[0m")

print("Qual o jogador com mais copas do mundo conquistadas? \n (A) Neuer \n (B) Pelé \n (C) Maradona \n")
answer_4 = input("Resposta: ")

if answer_4 == "B":
    print("\033[32mACERTOU!\033[0m")
    score = score + 1
else:
    print("\033[31mErrou!\033[0m")

print(f"Fim do Quiz... Pontuação: {score}/4")

input("\nPressione Enter para sair...")
