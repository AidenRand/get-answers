import random


def get_answer():
    """Return a string depending on what
    the randomly generated number was"""

    number = random.randint(1, 20)

    match number:
        case 1:
            print("\nIt is certain\n")

        case 2:
            print("\nIt is decidedly so\n")

        case 3:
            print("\nWithout a doubt\n")

        case 4:
            print("\nYes definitely\n")

        case 5:
            print("\nYou may rely on it\n")

        case 6:
            print("\nAs I see it, yes\n")

        case 7:
            print("\nMost likely\n")

        case 8:
            print("\nOutlook good\n")

        case 9:
            print("\nYes\n")

        case 10:
            print("\nSigns point to yes\n")

        case 11:
            print("\nReply hazy, try again\n")

        case 12:
            print("\nAsk again later\n")

        case 13:
            print("\nBetter not tell you now\n")

        case 14:
            print("\nCannot predict right now\n")

        case 15:
            print("\nConcentrate and ask again\n")

        case 16:
            print("\nDo not count on it\n")

        case 17:
            print("\nMy reply is no\n")

        case 18:
            print("\nMy sources say no\n")

        case 19:
            print("\nOutlook not so goodn\n")

        case 20:
            print("\nVery doubtful\n")


def get_user_input():
    """Get input from the user and exexute
    get_answer function if input is a string"""

    user_input = input("\nAsk what you wish: ")

    if user_input.isnumeric():
        print("\nyou did not give an answer\n")
    else:
        get_answer()


get_user_input()
