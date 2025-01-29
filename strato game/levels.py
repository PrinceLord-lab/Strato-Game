import os
import sortalgs
import monsters_look
import monsters_speech
import monsters_shields
import time
import random

width = os.get_terminal_size().columns

###
###
###   Start and Main Menu
###
###

def main_menu():
    os.system('cls')
    
    # Menu Picker
    
    print(' SSSSS  TTTTTTT  RRRRR     AA    TTTTTTT   OOOOO '.center(width))
    print('S          T     R    R   A  A      T     O     O'.center(width))
    print(' SSSS      T     RRRRR   AAAAAA     T     O     O'.center(width))
    print('     S     T     R    R  A    A     T     O     O'.center(width))
    print('SSSSS      T     R    R  A    A     T      OOOOO '.center(width))
    
    print('\n\n' + '[1] Start Game'.center(width))
    print('\n' + '[2] 10---Dash Attacks'.center(width))
    print('\n' + '[3] Quit'.center(width))
    
    selection = input('\n\nInput: ')
    return selection

###
###
###   Level Picking
###
###

def level_selection():
    os.system('cls')
    
    #Level Picker
    
    print('L       EEEEEE  V     V  EEEEEE  L        SSSSS'.center(width))
    print('L       E       V     V  E       L       S     '.center(width))
    print('L       EEEE    V     V  EEEE    L        SSSS '.center(width))
    print('L       E        V   V   E       L            S'.center(width))
    print('LLLLLL  EEEEEE     V     EEEEEE  LLLLLL  SSSSS '.center(width))
    
    print('\n\n' + '[1] Chief Awesomeness'.center(width))
    print('\n' + '[2] The Cyborg Guardian'.center(width))
    print('\n' + '[3] Arachnid Among Us'.center(width))
    
    selection = input('\n\nInput: ')
    return selection

###
###
###   Level One
###
###

def level_one():
    os.system('cls')
    time.sleep(1)
    
    # Assigning and Displaying the Look and Texts
    
    monster = monsters_look.level_one()
    speech = monsters_speech.level_one()
    
    for part in monster: print(part)
        
    for text in speech:
        time.sleep(1.2)
        print('\n' + text)
        
    time.sleep(2.5)
    proceed = input('\n\n\n' + '==Continue=='.center(width))
    
    # Preparing the Lists
    
    shields = monsters_shields.level_one()
    total_points = count = 0
    
    # Main Gameplay Loop
    
    while count != len(shields):
        os.system('cls')
        
        # Displaying the Look, a List, Commands for Sorting Algorithms
        
        for part in monster: print(part)
        
        time.sleep(0.5)
        print('\n' + ('Shield ' + str(count + 1) + ':').center(width))
        print(str(shields[count]).center(width))
        time.sleep(0.5)
        print('\n\n' + 'Select your shield breaker:'.center(width))
        time.sleep(0.3)
        print('_______________'.center(width))
        print('| [1] Insertion |'.center(width))
        print('| [2] Selection |'.center(width))
        print('| [3] Bubble    |'.center(width))
        print('| [4] Merge     |'.center(width))
        print('| [5] Quick_____|'.center(width))
        time.sleep(0.5)
        selection = input('\nInput: ')
        
        print('\n' + 'Breaking shield...'.center(width) + '\n')
        broken = True
        
        # Sorting Algorithm Picker
        
        deduction = points = cut_time = 0
        
        if selection == '1':
            start_time = time.time()
            sortalgs.insertion_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '2':
            start_time = time.time()
            sortalgs.selection_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '3':
            start_time = time.time()
            sortalgs.bubble_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '4':
            start_time = time.time()
            sortalgs.merge_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '5':
            start_time = time.time()
            sortalgs.quick_sort(shields[count])
            cut_time = time.time() - start_time
            
        else:
            print('\n\n' + 'Attempt failed. Try again.'.center(width))
            print('\n\n' + 'Penalty: -2 points'.center(width))
            deduction += 2
            broken = False
            
        # Calculating Points and Summation
            
        if broken:
            points = (1 / 0.8) * (int((len(shields[count]) / 10)) * (1 / cut_time))
            print(str(shields[count]).center(width))
            print('\n' + ('Shields broken! Points: ' + str(points)).center(width))
            
            count += 1
            total_points += points
        
        proceed = input('\n\n' + '==Continue=='.center(width))
        
    #Loop Done, Displaying Total Points

    os.system('cls')
    print(' CCCCC  L       EEEEEE    AA    RRRRR   EEEEEE  DDDDD '.center(width))
    print('C       L       E        A  A   R    R  E       D    D'.center(width))
    print('C       L       EEEE    AAAAAA  RRRRR   EEEE    D    D'.center(width))
    print('C       L       E       A    A  R    R  E       D    D'.center(width))
    print(' CCCCC  LLLLLL  EEEEEE  A    A  R    R  EEEEEE  DDDDD '.center(width))
    
    print('\n\n\n' + ('Total points: ' + str(total_points)).center(width))
    proceed = input('\n\n' + '==Continue=='.center(width))

###
###
###   Level Two
###
###

def level_two():
    os.system('cls')
    time.sleep(1)
    
    monster = monsters_look.level_two()
    speech = monsters_speech.level_two()
    
    for part in monster: print(part)
        
    for text in speech:
        time.sleep(1.2)
        print('\n' + text)
        
    time.sleep(2.5)
    proceed = input('\n\n\n' + '==Continue=='.center(width))
    
    shields = monsters_shields.level_two()
    total_points = count = 0
    
    while count != len(shields):
        os.system('cls')
        
        for part in monster: print(part)
        
        time.sleep(0.5)
        print('\n' + ('Shield ' + str(count + 1) + ':').center(width))
        print(str(shields[count]).center(width))
        time.sleep(0.5)
        print('\n\n' + 'Select your shield breaker:'.center(width))
        time.sleep(0.3)
        print('_______________'.center(width))
        print('| [1] Insertion |'.center(width))
        print('| [2] Selection |'.center(width))
        print('| [3] Bubble    |'.center(width))
        print('| [4] Merge     |'.center(width))
        print('| [5] Quick_____|'.center(width))
        time.sleep(0.5)
        selection = input('\nInput: ')
        
        print('\n' + 'Breaking shield...'.center(width) + '\n')
        broken = True
        
        deduction = points = cut_time = 0
        
        if selection == '1':
            start_time = time.time()
            sortalgs.insertion_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '2':
            start_time = time.time()
            sortalgs.selection_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '3':
            start_time = time.time()
            sortalgs.bubble_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '4':
            start_time = time.time()
            sortalgs.merge_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '5':
            start_time = time.time()
            sortalgs.quick_sort(shields[count])
            cut_time = time.time() - start_time
            
        else:
            print('\n\n' + 'Attempt failed. Try again.'.center(width))
            print('\n\n' + 'Penalty: -2 points'.center(width))
            deduction += 2
            broken = False
            
        if broken:
            points = (2 / 0.8) * (int((len(shields[count]) / 10)) * (2 / cut_time))
            print(str(shields[count]).center(width))
            print('\n' + ('Shields broken! Points: ' + str(points)).center(width))
            
            count += 1
            total_points += points
        
        proceed = input('\n\n' + '==Continue=='.center(width))

    os.system('cls')
    print(' CCCCC  L       EEEEEE    AA    RRRRR   EEEEEE  DDDDD '.center(width))
    print('C       L       E        A  A   R    R  E       D    D'.center(width))
    print('C       L       EEEE    AAAAAA  RRRRR   EEEE    D    D'.center(width))
    print('C       L       E       A    A  R    R  E       D    D'.center(width))
    print(' CCCCC  LLLLLL  EEEEEE  A    A  R    R  EEEEEE  DDDDD '.center(width))
    
    print('\n\n\n' + ('Total points: ' + str(total_points)).center(width))
    proceed = input('\n\n' + '==Continue=='.center(width))

###
###
###   Level Three
###
###

def level_three():
    os.system('cls')
    time.sleep(1)
    
    monster = monsters_look.level_three()
    speech = monsters_speech.level_three()
    
    for part in monster: print(part)
        
    for text in speech:
        time.sleep(1.2)
        print('\n' + text)
        
    time.sleep(2.5)
    proceed = input('\n\n\n' + '==Continue=='.center(width))
    
    shields = monsters_shields.level_three()
    total_points = count = 0
    
    while count != len(shields):
        os.system('cls')
        
        for part in monster: print(part)
        
        time.sleep(0.5)
        print('\n' + ('Shield ' + str(count + 1) + ':').center(width))
        print(str(shields[count]).center(width))
        time.sleep(0.5)
        print('\n\n' + 'Select your shield breaker:'.center(width))
        time.sleep(0.3)
        print('_______________'.center(width))
        print('| [1] Insertion |'.center(width))
        print('| [2] Selection |'.center(width))
        print('| [3] Bubble    |'.center(width))
        print('| [4] Merge     |'.center(width))
        print('| [5] Quick_____|'.center(width))
        time.sleep(0.5)
        selection = input('\nInput: ')
        
        print('\n' + 'Breaking shield...'.center(width) + '\n')
        broken = True
        
        deduction = points = cut_time = 0
        
        if selection == '1':
            start_time = time.time()
            sortalgs.insertion_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '2':
            start_time = time.time()
            sortalgs.selection_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '3':
            start_time = time.time()
            sortalgs.bubble_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '4':
            start_time = time.time()
            sortalgs.merge_sort(shields[count])
            cut_time = time.time() - start_time
            
        elif selection == '5':
            start_time = time.time()
            sortalgs.quick_sort(shields[count])
            cut_time = time.time() - start_time
            
        else:
            print('\n\n' + 'Attempt failed. Try again.'.center(width))
            print('\n\n' + 'Penalty: -2 points'.center(width))
            deduction += 2
            broken = False
            
        if broken:
            points = (3 / 0.8) * (int((len(shields[count]) / 10)) * (3 / cut_time))
            print(str(shields[count]).center(width))
            print('\n' + ('Shields broken! Points: ' + str(points)).center(width))
            
            count += 1
            total_points += points
        
        proceed = input('\n\n' + '==Continue=='.center(width))

    os.system('cls')
    print(' CCCCC  L       EEEEEE    AA    RRRRR   EEEEEE  DDDDD '.center(width))
    print('C       L       E        A  A   R    R  E       D    D'.center(width))
    print('C       L       EEEE    AAAAAA  RRRRR   EEEE    D    D'.center(width))
    print('C       L       E       A    A  R    R  E       D    D'.center(width))
    print(' CCCCC  LLLLLL  EEEEEE  A    A  R    R  EEEEEE  DDDDD '.center(width))
    
    print('\n\n\n' + ('Total points: ' + str(total_points)).center(width))
    proceed = input('\n\n' + '==Continue=='.center(width))

###
###
###   Ten Dash
###
###

def ten_dash_mode():
    # Main Gameplay Loop
    
    running = 0
    total_points = 0
    while running != 10:
        
        #Displaying the Title of Mode
        
        os.system('cls')
        print('  11     0000                DDDDD     AA     SSSSS  H    H'.center(width))
        print(' 1 1    0   00               D    D   A  A   S       H    H'.center(width))
        print('   1    0 00 0  === === ===  D    D  AAAAAA   SSSS   HHHHHH'.center(width))
        print('   1    00   0               D    D  A    A       S  H    H'.center(width))
        print('111111   0000                DDDDD   A    A  SSSSS   H    H'.center(width))
        print('\n\n')
        time.sleep(1)
        
        # Randomizer for Look and What List to Make
        
        roulette = random.randint(1, 3)
        monster = shield = []
        size = random.randint(10, 50)
        
        if roulette == 1:
            monster = monsters_look.level_one()
            query = []

            for number in range(1, size + 1):
                query.append(number)

                if len(query) == 5 or number == size:
                    random.shuffle(query)

                    for num in query: shield.append(num)
                    query = []

        if roulette == 2:
            monster = monsters_look.level_two()
            
            for number in range(1, size + 1): shield.append(number)
            shield_copy = shield.copy()

            while shield == shield_copy:
                random.shuffle(shield)

        if roulette == 3:
            monster = monsters_look.level_three()
            
            for number in range(size, 0, -1): shield.append(number)
        
        # Displaying the Look, List, Commands for Sorting Algorithms
        
        for part in monster: print(part)
        
        time.sleep(0.5)
        print('\n' + ('Shield ' + str(running + 1) + ':').center(width))
        print(str(shield).center(width))
        time.sleep(0.5)
        print('\n\n' + 'Select your shield breaker:'.center(width))
        time.sleep(0.3)
        print('_______________'.center(width))
        print('| [1] Insertion |'.center(width))
        print('| [2] Selection |'.center(width))
        print('| [3] Bubble    |'.center(width))
        print('| [4] Merge     |'.center(width))
        print('| [5] Quick_____|'.center(width))
        time.sleep(0.5)
        selection = input('\nInput: ')
        
        print('\n' + 'Breaking shield...'.center(width) + '\n')
        broken = True
        
        # Sorting Algorithm Picker
        
        deduction = points = cut_time = 0
        
        if selection == '1':
            start_time = time.time()
            sortalgs.insertion_sort(shield)
            cut_time = time.time() - start_time
            
        elif selection == '2':
            start_time = time.time()
            sortalgs.selection_sort(shield)
            cut_time = time.time() - start_time
            
        elif selection == '3':
            start_time = time.time()
            sortalgs.bubble_sort(shield)
            cut_time = time.time() - start_time
            
        elif selection == '4':
            start_time = time.time()
            sortalgs.merge_sort(shield)
            cut_time = time.time() - start_time
            
        elif selection == '5':
            start_time = time.time()
            sortalgs.quick_sort(shield)
            cut_time = time.time() - start_time
            
        else:
            print('\n\n' + 'Attempt failed. Try again.'.center(width))
            print('\n\n' + 'Penalty: -2 points'.center(width))
            deduction += 2
            broken = False
            
        # Calculating Points and Summation
        
        if broken:
            points = (2 / 0.8) * (int((len(shield) / 10)) / (cut_time ** (1/2)))
            print(str(shield).center(width))
            print('\n' + ('Shields broken! Points: ' + str(points)).center(width))
            
            running += 1
            total_points += points
        
        proceed = input('\n\n' + '==Continue=='.center(width))
        
    # Loop Done, Displaying the Total Points
    
    os.system('cls')
    print(' CCCCC  L       EEEEEE    AA    RRRRR   EEEEEE  DDDDD '.center(width))
    print('C       L       E        A  A   R    R  E       D    D'.center(width))
    print('C       L       EEEE    AAAAAA  RRRRR   EEEE    D    D'.center(width))
    print('C       L       E       A    A  R    R  E       D    D'.center(width))
    print(' CCCCC  LLLLLL  EEEEEE  A    A  R    R  EEEEEE  DDDDD '.center(width))
    
    print('\n\n\n' + ('Total points: ' + str(total_points)).center(width))
    proceed = input('\n\n' + '==Continue=='.center(width))