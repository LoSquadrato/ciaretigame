
from core.costants import MAX_NAME_LENGHT

# funzione check_input se uno scrive help gli copio il manuale
# altrimenti enum dei diversi input

def valid_input_card(hand):
        
    while True:
        try:
            pos = int(input('enter the number refered to the card you choose\n'))
        except ValueError:
            print('Sorry wrong digit')
            continue
        if drop_rule(pos, hand):
            if conf_input('Are you sure?\n y/N'):
                break
            continue
        else:
            print('Sorry this is not a valid answer')
            continue
    return hand[pos]
       
        
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

def drop_rule(pos, hand):
    for i, v in hand.items():
        if i == pos:
            if v.is_legit == False:
                print('You choose a wrong card,\n if you have some question digit "help"')
                return False
            if v.is_legit == True:
                print(f'Your choice is: {v}')
                return True