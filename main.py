from random import randint
import time

blackjack_graphic = """      
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/ 
                      """

input("Press the enter key to start")

print(
    """88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                 """
)
print(
    """
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|

"""
)
win = 0
lose = 0
tie = 0
win_rate = 0
while True:
    yes_no_3_ace = 0
    yes_no_4_ace = 0
    card_addition = 0
    turn_over = 1
    player_bust = 1
    dealer_card3_check = 1
    user_input_2 = 1
    stop = 1
    aces = 0
    ace_d = 0
    card_1 = randint(1, 14)
    type_1 = randint(1, 4)
    while True:
        card_2 = randint(1, 14)
        type_2 = randint(1, 4)
        if card_2 == card_1 and type_2 == type_1:
            pass
        else:
            break
    while True:
        card_3 = randint(1, 14)
        type_3 = (1, 4)
        if card_3 == card_2 or card_3 == card_1:
            if type_3 == type_2 or type_3 == type_1:
                pass
            else:
                break
        else:
            break
    while True:
        card_4 = randint(1, 14)
        type_4 = randint(1, 4)
        if card_4 == card_1 and type_4 == type_1:
            pass
        else:
            if card_4 == card_2 and type_4 == type_2:
                pass
            else:
                if card_4 == card_3 and type_4 == type_3:
                    pass
                else:
                    if card_4 == card_3 and type_4 == type_3:
                        pass
                    else:
                        break
    aces = 0
    if card_1 == 14:
        print_1 = "ace"
        aces = 1
        card_1 -= 3
    elif card_1 == 13:
        print_1 = "king"
        card_1 = 10
    elif card_1 == 12:
        print_1 = "queen"
        card_1 = 10
    elif card_1 == 11:
        print_1 = "jack"
        card_1 = 10
    else:
        print_1 = "Number"

    if card_2 == 14:
        print_2 = "ace"
        card_2 = 11
        aces += 1
    elif card_2 == 13:
        print_2 = "king"
        card_2 = 10
    elif card_2 == 12:
        print_2 = "queen"
        card_2 = 10
    elif card_2 == 11:
        print_2 = "jack"
        card_2 = 10
    else:
        print_2 = "Number"
        card_2 = card_2

    if card_3 == 14:
        print_3 = "ace"
        yes_no_3_ace += 1 
        card_3 = 11
    elif card_3 == 13:
        print_3 = "king"
        card_3 = 10
    elif card_3 == 12:
        print_3 = "queen"
        card_3 = 10
    elif card_3 == 11:
        print_3 = "jack"
        card_3 = 10
    else:
        print_3 = "Number"

    if card_4 == 14:
        print_4 = "ace"
        yes_no_4_ace += 1
        aces += 1
        card_4 = 11
    elif card_4 == 13:
        print_4 = "king"
        card_4 = 10
    elif card_4 == 12:
        print_4 = "queen"
        card_4 = 10
    elif card_4 == 11:
        print_4 = "jack"
        card_4 = 10
    else:
        print_4 = "Number"

    print(f"Your first number is {card_1} which is a {print_1}")
    print(f"and your second number is {card_2} which is a {print_2}")

    if card_1 + card_2 == 21:
        print(blackjack_graphic)
        blackjack = 2
    card_addition = int(card_1) + int(card_2)

    while True:
        user_input = input("Do you stand? Enter (1) for yes and (2) for no: ")
        if str(user_input) == "1" or str(user_input) == "2":
            if int(user_input) == 2:
                print(f"and your third number is {card_3} which is a {print_3}")
                if yes_no_3_ace == 2:
                    aces += 1
                user_input = 2
                card_addition += card_3
            break
        else:
            print("Invalid input, please try again")
    while True:
        if user_input == 2:
            user_input_2 = input(
                """                     
                                      .------.
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \  / | /\  |( )  |  I  A|
                   |  \/ A|/  \ |_x_) |------'
                   `-----+'\  / | Y  A|
                         |  \/ A|-----'    
                         `------'
                Type (1) to Stand, (2) for Hit
                          : """
            )
        if str(user_input_2) == "1" or str(user_input_2) == "2":
            if str(user_input_2) == "2":
                card_addition += card_4
                if yes_no_4_ace == 2:
                    aces += 1
                print(f"Your fourth card was a {print_4} which is worth {card_4}")
            break

    while aces > 0:
        using_aces_input = input(
            f"""
            You have {aces} extra aces. Your current score is {card_addition}. 
            Type (11) if you want to use it as an eleven and (1) if you want to use it as a one.
            """
        )
        if str(using_aces_input) == "11" or str(using_aces_input == "1"):
            aces -= 1
            if str(using_aces_input) == "1":
                card_addition -= 10
        else:
            print("Invalid, please try again")

    if card_addition == 21:
        print(blackjack_graphic)
    elif card_addition > 21:
        card_addition = 0
    input("Press enter to continue to dealers turn")
    time.sleep(0.2)
    print("            _____")
    time.sleep(0.1)
    print("           |\ ~ /|")
    time.sleep(0.1)
    print("           |}}:{{|")
    time.sleep(0.1)
    print("           |}}:{{|  _____")
    time.sleep(0.1)
    print("           |}}:{{| |Joker|")
    time.sleep(0.1)
    print("           |/_~_\| |==%, |")
    time.sleep(0.1)
    print("                   | \/>\|")
    time.sleep(0.1)
    print("                   | _>^^|           _____")
    time.sleep(0.1)

    print("         _____     |/_\/_|    _____ |6    |")
    time.sleep(0.1)

    print("        |2    | _____        |5    || ^ ^ |")
    time.sleep(0.1)

    print("        |  ^  ||3    | _____ | ^ ^ || ^ ^ | _____")
    time.sleep(0.1)

    print("        |     || ^ ^ ||4    ||  ^  || ^ ^ ||7    |")
    time.sleep(0.1)

    print("        |  ^  ||     || ^ ^ || ^ ^ ||____9|| ^ ^ | _____")
    time.sleep(0.1)

    print("        |____Z||  ^  ||     ||____S|       |^ ^ ^||8    | _____")
    time.sleep(0.1)

    print("               |____E|| ^ ^ |              | ^ ^ ||^ ^ ^||9    |")
    time.sleep(0.1)

    print("                      |____h|              |____L|| ^ ^ ||^ ^ ^|")
    time.sleep(0.1)

    print("                                  _____           |^ ^ ^||^ ^ ^|")
    time.sleep(0.1)

    print("                          _____  |K  WW|          |____8||^ ^ ^|")
    time.sleep(0.1)

    print("                  _____  |Q  ww| | ^ {)|                 |____6|")
    time.sleep(0.1)

    print("           _____ |J  ww| | ^ {(| |(.)%%| _____")
    time.sleep(0.1)

    print("          |10 ^ || ^ {)| |(.)%%| | |%%%||A .  |")
    time.sleep(0.1)

    print("          |^ ^ ^||(.)% | | |%%%| |_%%%>|| /.\ |")
    time.sleep(0.1)

    print("          |^ ^ ^|| | % | |_%%%O|        |(_._)|")
    time.sleep(0.1)

    print("          |^ ^ ^||__%%[|                |  |  |")
    time.sleep(0.1)

    print("          |___0I|                       |____V|")
    time.sleep(0.1)

    time.sleep(0.1)
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")

    print("Dealers turn. The first card is...")

    dealer_draw_1d = randint(1, 14)
    dealer_draw_2d = randint(1, 14)
    dealer_draw_3d = randint(1, 14)


    if dealer_draw_1d == 14:
        card_1d = 11
        name_1d = "ace"
        card_type_1d = randint(1, 4)
    elif dealer_draw_1d == 13:
        card_1d = 10
        name_1d = "King"
        card_type_1d = randint(1, 4)
    elif dealer_draw_1d == 12:
        card_1d = 10
        name_1d = "Queen"
        card_type_1d = randint(1, 4)
    elif dealer_draw_1d == 11:
        card_1d = 10
        name_1d = "Jack"
        card_type_1d = randint(1, 4)
    else:
        card_1d = dealer_draw_1d
        name_1d = str(dealer_draw_1d)
        card_type_1d = randint(1, 4)

    if dealer_draw_2d == 14:
        card_2d = 11
        name_2d = "ace"
        card_type_2d = randint(1, 4)
    elif dealer_draw_2d == 13:
        card_2d = 10
        name_2d = "King"
        card_type_2d = randint(1, 4)
    elif dealer_draw_2d == 12:
        card_2d = 10
        name_2d = "Queen"
        card_type_2d = randint(1, 4)
    elif dealer_draw_2d == 11:
        card_2d = 10
        name_2d = "Jack"
        card_type_2d = randint(1, 4)
    else:
        card_2d = dealer_draw_2d
        name_2d = str(dealer_draw_2d)
        card_type_2d = randint(1, 4)

    if dealer_draw_3d == 14:
        card_3d = 11
        name_3d = "ace"
        card_type_3d = randint(1, 4)
    elif dealer_draw_3d == 13:
        card_3d = 10
        name_3d = "King"
        card_type_3d = randint(1, 4)
    elif dealer_draw_3d == 12:
        card_3d = 10
        name_3d = "Queen"
        card_type_3d = randint(1, 4)
    elif dealer_draw_3d == 11:
        card_3d = 10
        name_3d = "Jack"
        card_type_3d = randint(1, 4)
    else:
        card_3d = dealer_draw_3d
        name_3d = str(dealer_draw_3d)
        card_type_3d = randint(1, 4)
    if dealer_draw_3d == 14:
        card_3d = 11
        name_3d = "ace"
        card_type_3d = randint(1, 4)
    elif dealer_draw_3d == 13:
        card_3d = 10
        name_3d = "King"
        card_type_3d = randint(1, 4)
    elif dealer_draw_3d == 12:
        card_3d = 10
        name_3d = "Queen"
        card_type_3d = randint(1, 4)
    elif dealer_draw_3d == 11:
        card_3d = 10
        name_3d = "Jack"
        card_type_3d = randint(1, 4)
    else:
        card_3d = dealer_draw_3d
        name_3d = str(dealer_draw_3d)
        card_type_3d = randint(1, 4)

    print(card_1d)
    time.sleep(1)  # Sleep for 1 seconds
    print("Next card is") and time.sleep(0.5) and print(".") and time.sleep(
        0.3
    ) and print(".") and time.sleep(0.1) and print(".")
    print(
        """     -^-_  _
  / [_][_]_:_
 /|  _||_  v
  | /    \ |
=/=\\____//=\=
    """
    )

    ace_d = 0
    if card_2d == 11:
        ace_d += 1
    if card_1d == 11:
        ace_d += 1
    dealer_score = card_1d + card_2d
    time.sleep(1)
    time.sleep(0.2)
    print(card_2d)
    if card_1d + card_2d == 21:
        print(blackjack_graphic)
    elif card_1d + card_2d < 21:
        if dealer_score < card_addition:
            print("The dealer chooses to hit")
            time.sleep(0.2)
            print(f"The dealer gets {card_3d}")
            card_3_confirmed = 2
            if card_3 == 11:
                ace_d += 1
            if ace_d == 0:
                dealer_score += card_3
            elif ace_d >= 1:
                if dealer_score <= 21:
                    if dealer_score == 21:
                        print("blackjack")
                        if blackjack == 2:
                            print("Tie game")
                    else:
                        if dealer_score > 21 and ace_d >= 1:
                            while ace_d > 0 and dealer_score > 21:
                                dealer_score -= 10
                                ace_d -= 1
                                print("Ace used as 1")

    if card_addition > 21:
        card_addition = 0
    if dealer_score > 21:
        dealer_score = 0
    if dealer_score < card_addition and dealer_score > 0:
        while True:
            card_4d = randint(1, 14)
            type_4d = randint(1, 4)

            if card_4d == 14:
                print_4d = "ace"
                ace_d += 1
                card_4d = 11
            elif card_4d == 13:
                print_4d = "king"
                card_4d = 10
            elif card_4d == 12:
                print_4d = "queen"
                card_4d = 10
            elif card_4d == 11:
                print_4d = "jack"
                card_4d = 10
            else:
                print_4d = "Number"
            if type_4d == card_type_1d and print_4d == name_1d:
                pass
            else:
                if type_4d == card_type_2d and print_4d == name_2d:
                    pass
                else:
                    if type_4d == card_type_3d and print_4d == name_3d:
                        pass
                    else:
                        card_4_confirmed = 2
                        break
        dealer_score += card_4d
        if aces >= 1:
            while aces >= 1:
                if dealer_score > 21:
                    dealer_score -= 10
                aces -= 1
    if dealer_score > 21:
        if card_4_confirmed == 2:
            dealer_score -= card_4d
        elif card_3_confirmed == 2:
            dealer_score -= card_3d

    if dealer_score > card_addition:
        print(f"Dealer wins with {dealer_score} vs {card_addition}")
        win += 0
        lose += 1
        tie += 0
    elif dealer_score < card_addition:
        print(f"You win with {card_addition} vs his {dealer_score}")
        win += 1
        lose += 0
        tie += 0
    elif dealer_score == card_addition:
        print(
            f"Tie game, in the event of a tie the dealer wins. {card_addition} vs {dealer_score}"
        )
        win += 0
        lose += 0
        tie += 1
    else:
        print(
            f"ERROR! Scores are: player {card_addition} vs dealer {dealer_score}"
        )
    denomenator = win + lose + tie
    win_rate = float(win / denomenator)
    lose_rate = float(lose / denomenator)
    tie_rate = float(tie / denomenator)

    time.sleep(2)
    print("5")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("""
    
    
    
    
    """)
    time.sleep(0.5)
    print("""
    
    
    
    """)
    stats = input("Would you like your stats? ")
    if stats == "Yes" or stats == "mhm" or stats == "yeah" or stats == "yes":    
        print(
        f"""
    Your win percent is {win_rate} your lose percentage is {lose_rate} and your tieing percentage is {tie_rate}
    Your have won {win} games, lost {lose} and tied {tie}    
    """
        )
        time.sleep(5)
        print(f"{win} games won")
        time.sleep(1)
        print(f"{lose} games lost")
        time.sleep(1)
        print(f"{tie} games tied")
        time.sleep(1)
        input("press enter to continue")
    print(
        """     
     .-~~-.
    {      }
 .-~-.    .-~-.
{              }
 `.__.'||`.__.'
       ||
      '--`


     /\
   .'  `.
  '      `.
<          >
 `.      .'
   `.  .'
     \/


       /\
     .'  `.
    '      `.
 .'          `.
{              }
 ~-...-||-...-~
       ||
      '--`


 .-~~~-__-~~~-.
{              }
 `.          .'
   `.      .'
     `.  .'
       \/   
"""
    )
