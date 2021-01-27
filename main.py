import random
loop = True
while loop:
# input

    print('Select an option from the menu (1-5):')
    print('1. Roll Dice Once') 
    print('2. Roll Dice 5 Time')
    print('3: Roll Dice ‘n’ Times')
    print('4: Roll Dice until Snake Eyes')
    print('5: Exit')
    menu_num = input('Enter here:')
    
    if int(menu_num) == 1:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(str(die1), ' - ',str(die2))
        
    elif int(menu_num) == 2:
        i = 0
        while i < 5:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(str(die1), ' - ',str(die2),'  (total = ',(die1 + die2),')')
            i += 1
            
    elif int(menu_num) == 3:
        i = 0
        num_of_rolls = int(input('How many rolls would you like?'))
        while i < num_of_rolls:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(str(die1), ' - ',str(die2),'  (total = ',(die1 + die2),')')
            i += 1
            
    elif int(menu_num) == 4:
        snakeEyes = True    
        while snakeEyes:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(str(die1), ' - ',str(die2),'  (total = ',(die1 + die2),')')
            if die1 == 1 and die2 == 1:
                print('SNAKE EYES!')
                snakeEyes = False
            
            
    elif int(menu_num) == 5:
        print('Goodbye!')
        loop = False
# if int(menu_num) > 0:
#     menu_num = input('1. Roll Dice Once | 2. Roll Dice 5 Time | 3: Roll Dice ‘n’ Times | 4: Roll Dice until Snake Eyes | 5: ExitSelect an option from the menu (1-5):')

