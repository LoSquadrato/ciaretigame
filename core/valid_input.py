
from core.costants import MAX_NAME_LENGHT

def valid_input_card(hand, legit_cards):  
    while True:
        try:
            pos = int(input('enter the number refered to the card you choose\n'))
        except ValueError:
            print('Sorry wrong digit')
            continue
        if is_legit(pos - 1, hand, legit_cards):
            if conf_input('Are you sure?\n y/N'):
                break
            continue
        else:
            print('Sorry this is not a valid answer')
            continue
    return hand[pos - 1]
       
        
def valid_input_name():
    while True:
        try:
            name = str(input('What\'s your name?\n'))
        except ValueError:
            print('Sorry wrong digit')
            continue
        if len(name) < MAX_NAME_LENGHT:
            if conf_input('Are you sure?\n y/N\n'):
                break
            continue
        else:
            print('This name is too long, please choose a shorter name')
            continue
    return name
            
            
def conf_input(txt):
    # return True se ok False se no
    while True:
        try:
            conf = str(input(txt))
        except ValueError:
            print('Sorry can\'t understand you')
            continue
        if conf.lower() == 'n':
            return False
        elif conf.lower() == 'y':
            return True
        else:
            print('Sorry this is not a valid answer')
            continue

def is_legit(index, hand, legit_cards):
    if index > len(hands):
        print('choose a position number from your hand list')
        return False
    if not legit_cards or hand[index] in legit_cards:
        print(f'Your choice is: {hand[index]}')
        return True
    print('You choose a wrong card\n')
    return False
                