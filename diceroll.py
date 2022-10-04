from random import randint
choice = input('Role Dice?: [Y] [N]').lower()
dice = 1
while choice == 'y':
    print('Dice is being rolled')
    dice = randint(1, 6)
    print(f'You rolled {dice}')
    choice = input('Roll again?: [Y] [N]')
print('You put the dice away. press any button to exit: ')
input()
