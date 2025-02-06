import random 

print('Bienvenidos al juego de piedra, papel y tijera <<<\n')
result = {
    'piedra': {'tijera': 1, 'papel':0},
    'papel': {'piedra': 1, 'tijera':0},
    'tijera': {'papel': 1, 'piedra': 0}
}

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_options = input('>>>Piedra, papel o tijera => ').lower()

    if not user_options in options:
        print('Opción invalida')
        return None, None
    computer_options = random.choice(options)
    print('La opción del usuario es => ', user_options)
    print('La opción del PC es => ', computer_options)

def check_rules(user_options, computer_options, user_wins, computer_wins):
    if user_options == computer_options:
        print("Hay un empate!\n")
    else:
        ganador = result[user_options][computer_options]
        if ganador:
            print('{} gana a {}'.format(user_options,computer_options))
            print('¡Usuario gana!\n')
            user_wins += 1
        else:
            print('{} gana a {}'.format(user_options,computer_options))
            print('¡Gana el PC\n')
            computer_wins += 1

    return user_wins,computer_wins

def check_winner(user_wins, computer_wins):

    print(f'''
          Computer wins: {computer_wins}
          User wins: {user_wins}
          ''')
    
    if user_wins == 3:
        print('El ganador es User')
        exit()

    if computer_wins == 3:
        print('El ganador es PC')
        exit()

def run_game():

    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print('***' * 10)
        print('round', rounds)
        print('***' * 10)

        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)
    
run_game()