import random

user_points = 0
computer_points = 0
options = ["r", "t", "p"]

while True:
    user_choice = input("Escolha R/P/T ou Q para sair: ").lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        print("Opção inválida!")
        continue

    computer_choice = random.randint(0, 2)
    computer_option = options[computer_choice]

    print(f"O computador escolheu: {computer_option}")

    if user_choice == computer_option:
        print("Empate!")
    elif (user_choice == "r" and computer_option == "t") or \
         (user_choice == "p" and computer_option == "r") or \
         (user_choice == "t" and computer_option == "p"):
        print("Você ganhou!")
        user_points += 1
    else:
        print("Você perdeu!")
        computer_points += 1

print("-" * 20)
print(f"Sua pontuação: {user_points}")
print(f"Pontuação do computador: {computer_points}")

if computer_points > user_points:
    print("Você perdeu!")
elif computer_points == user_points:
    print("Empate!")
else:
    print("Você venceu!")

print("Adeus!")