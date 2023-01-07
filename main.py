import random


def get_answer():
    """Return a string depending on what
    the randomly generated number was"""

    number = random.randint(1, 20)

    match number:
        case 1:
            print("It is certain")

        case 2:
            print("It is decidedly so")

        case 3:
            print("Without a doubt")

        case 4:
            print("Yes definitely")

        case 5:
            print("You may rely on it")

        case 6:
            print("As I see it, yes")

        case 7:
            print("Most likely")

        case 8:
            print("Outlook good")

        case 9:
            print("Yes")

        case 10:
            print("Signs point to yes")

        case 11:
            print("Reply hazy, try again")

        case 12:
            print("Ask again later")

        case 13:
            print("Better not tell you now")

        case 14:
            print("Cannot predict right now")

        case 15:
            print("Concentrate and ask again")

        case 16:
            print("Do not count on it")

        case 17:
            print("My reply is no")

        case 18:
            print("My sources say no")

        case 19:
            print("Outlook not so good")

        case 20:
            print("Very doubtful")


def get_user_input():
    """Get input from the user and exexute
    get_answer function if input is a string"""

    user_input = input('Ask what you wish: ')
    
    if user_input.isnumeric():
        print('you did not give an answer')
    else: 
        get_answer()        
get_user_input()