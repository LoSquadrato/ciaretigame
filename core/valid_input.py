def input_selezione_carta():  
    while True:
        try:
            pos = int(input('enter the number refered to the card you choose\n'))
        except ValueError:
            print('Sorry wrong digit')
            continue
        if conf_input('Are you sure?\n y/N'):
            break
        else:
            print('Sorry this is not a valid answer')
            continue
    return pos
       
'''   
# Per una versione interattiva in cui si chiede all'utente
# di inserire un nome    
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
'''          
            
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
