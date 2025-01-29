import os
import sortalgs
import monsters_look
import monsters_speech
import monsters_shields
import time
import random

width = os.get_terminal_size().columns

# Start and Main Menu

def main_menu():
    os.system('cls')
    
    print(' SSSSS   OOOOO    GGGGG    AA    M    M  EEEEEE'.center(width))
    print('S       O     O  G        A  A   MM  MM  E     '.center(width))
    print(' SSSS   O     O  G  GGG  AAAAAA  M MM M  EEEE  '.center(width))
    print('     S  O     O  G    G  A    A  M    M  E     '.center(width))
    print('SSSSS    OOOOO    GGGGG  A    A  M    M  EEEEEE'.center(width))
    
    print('\n\n' + '[1] Start Game'.center(width))
    print('\n' + '[2] 10---Dash Attacks'.center(width))
    print('\n' + '[3] Quit'.center(width))
    
    selection = input('\n\nInput: ')
    return selection

def level_selection():
    os.system('cls')
    
    print('L       EEEEEE  V    V  EEEEEE  L        SSSSS'.center(width))
    print('L       E       V    V  E       L       S     '.center(width))
    print('L       EEEE    v    V  EEEE    L        SSSS '.center(width))
    print('L       E        V  V   E       L            S'.center(width))
    print('LLLLLL  EEEEEE    VV    EEEEEE  LLLLLL  SSSSS '.center(width))
    
    print('\n\n' + '[1] Chief Awesomeness'.center(width))
    print('\n' + '[2] The Cyborg Guardian'.center(width))
    print('\n' + '[3] Arachnid Among Us'.center(width))
    
    selection = input('\n\nInput: ')
    return selection

#
#
# Level One
#
#

def level_one():
    os.system('cls')
    time.sleep(1)
    
    monster = monsters_look.level_one_virus()
    speech = monsters_speech.level_one()
    
    for parts in monster:
        print(parts)
        
    for text in speech:
        time.sleep(1.5)
        
        print('\n' + text)
    
    time.sleep(3)
    proceed = input('\n\n\n' + '==Continue=='.center(width))
    
    shields = monsters_shields.level_one()
    total_points = count = 0
    
    while count != (len(shields)):
        os.system('cls')
        
        for parts in monster:
            print(parts)
            
        time.sleep(0.5)
        print('\n'+ ('Shield ' + str(count + 1) + ':').center(width))
        print(str(shields[count]).center(width))
        
        time.sleep(0.3)
        print('\n\n' + 'Select your magic:'.center(width))
        time.sleep(0.3)
        print('_______________'.center(width))
        print('| [1] Insertion |'.center(width))
        print('| [2] Selection |'.center(width))
        print('| [3] Bubble    |'.center(width))
        print('| [4] Merge     |'.center(width))
        print('| [5] Quick_____|'.center(width))
        time.sleep(0.3)
        selection = input('\nInput: ')
        
        print('\n' + 'Breaking shield...'.center(width) + '\n')
        
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
            total_time -= 2
            broken = False

        if broken:
            print(str(shields[count]).center(width))
            print('\n' + str(shields[count + 1]).center(width))
            print('\n' + ('Shields broken! Points: ' + str(cut_time)).center(width))
            count += 1
            total_time += cut_time
                
        proceed = input('\n\n' + '==Continue=='.center(width))
        
    os.system('cls')
    print(' CCCCC  L       EEEEEE    AA    RRRRR   EEEEEE  DDDDD '.center(width))
    print('C       L       E        A  A   R    R  E       D    D'.center(width))
    print('C       L       EEEE    AAAAAA  RRRRR   EEEE    D    D'.center(width))
    print('C       L       E       A    A  R    R  E       D    D'.center(width))
    print(' CCCCC  LLLLLL  EEEEEE  A    A  R    R  EEEEEE  DDDDD '.center(width))
    
    print('\n\n\n' + ('Total points: ' + str(total_time)).center(width))
    proceed = input('\n\n' + '==Continue=='.center(width))

#
#
# Level Two
#
#

def level_two():
    os.system('cls')
    time.sleep(1)
    
    monster = monsters_look.level_two_virus()
    speech = monsters_speech.level_two()
    
    for parts in monster:
        print(parts)
        
    for text in speech:
        time.sleep(1.5)
        
        print('\n' + text)
    
    time.sleep(3)
    proceed = input('\n\n\n' + '==Continue=='.center(width))
    
    shields = shields_copy = monsters_shields.level_two()
    total_time = count = 0
    
    while count != (len(shields)):
        os.system('cls')
        
        for parts in monster:
            print(parts)
            
        time.sleep(0.5)
        print('\n'+ ('Shield ' + str(count + 1) + ':').center(width))
        print(str(shields[count]).center(width))
        
        time.sleep(0.3)
        print('\n\n' + 'Select your magic:'.center(width))
        time.sleep(0.3)
        print('_______________'.center(width))
        print('| [1] Insertion |'.center(width))
        print('| [2] Selection |'.center(width))
        print('| [3] Bubble    |'.center(width))
        print('| [4] Merge     |'.center(width))
        print('| [5] Quick_____|'.center(width))
        time.sleep(0.3)
        selection = input('\nInput: ')
        
        print('\n' + 'Breaking shield...'.center(width) + '\n')
        broken = True
        
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
            total_time -= 2
            broken = False

        if broken:
            print(str(shields[count]).center(width))
            print('\n' + str(shields[count + 1]).center(width))
            print('\n' + ('Shields broken! Points: ' + str(cut_time)).center(width))
            count += 2
            total_time += cut_time
                
    proceed = input('\n\n' + '==Continue=='.center(width))
        
    os.system('cls')
    print(' CCCCC  L       EEEEEE    AA    RRRRR   EEEEEE  DDDDD '.center(width))
    print('C       L       E        A  A   R    R  E       D    D'.center(width))
    print('C       L       EEEE    AAAAAA  RRRRR   EEEE    D    D'.center(width))
    print('C       L       E       A    A  R    R  E       D    D'.center(width))
    print(' CCCCC  LLLLLL  EEEEEE  A    A  R    R  EEEEEE  DDDDD '.center(width))
    
    print('\n\n\n' + ('Total points: ' + str(total_time)).center(width))
    proceed = input('\n\n' + '==Continue=='.center(width))

#
#
# Level Three
#
#

def level_three():
    os.system('cls')
    time.sleep(1)
    round_count = 1
    
    monster = monsters_look.level_three_virus()
    speech = monsters_speech.level_three()
    
    for parts in monster:
        print(parts)
        
    for text in speech:
        time.sleep(1.5)
        
        print('\n' + text)
    
    time.sleep(3)
    proceed = input('\n\n\n' + '==Continue=='.center(width))
    
    shields = shields_copy = monsters_shields.level_three()
    total_time = count = 0
    
    while count != (len(shields)):
        os.system('cls')
        
        for parts in monster:
            print(parts)
            
        if count == 0:
            time.sleep(0.5)
            print('\n'+ ('Shield ' + str(round_count) + ':').center(width))
            print(str(shields[count]).center(width))

            time.sleep(0.3)
            print('\n\n' + 'Select your magic:'.center(width))
            time.sleep(0.3)
            print('_______________'.center(width))
            print('| [1] Insertion |'.center(width))
            print('| [2] Selection |'.center(width))
            print('| [3] Bubble    |'.center(width))
            print('| [4] Merge     |'.center(width))
            print('| [5] Quick_____|'.center(width))
            time.sleep(0.3)
            selection = input('\nInput: ')
        
            broken = True
            print('\n' + 'Breaking shield...'.center(width) + '\n')
            
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
                print('\n\n' + 'Penalty: +2 seconds'.center(width))
                total_time += 2
                broken = False

            if broken:
                print(str(shields[count]).center(width))
                print('\n' + str(shields[count + 1]).center(width))
                print('\n' + ('Shields broken! Time: ' + str(cut_time)).center(width))
                count += 2
                total_time += cut_time
                round_count += 1
                
        else:
            time.sleep(0.5)
            print('\n'+ ('Shield ' + str(round_count) + ':').center(width))
            print(str(shields[count]).center(width))
            print('\n' + str(shields[count + 1]).center(width))

            time.sleep(0.3)
            print('\n\n' + 'Select your magic:'.center(width))
            time.sleep(0.3)
            print('_______________'.center(width))
            print('| [1] Insertion |'.center(width))
            print('| [2] Selection |'.center(width))
            print('| [3] Bubble    |'.center(width))
            print('| [4] Merge     |'.center(width))
            print('| [5] Quick_____|'.center(width))
            time.sleep(0.3)
            selection = input('\nInput: ')
            
            broken = True
            print('\n' + 'Breaking shields...'.center(width) + '\n')

            if selection == '1':
                start_time = time.time()
                sortalgs.insertion_sort(shields[count])
                sortalgs.insertion_sort(shields[count + 1])
                cut_time = time.time() - start_time

            elif selection == '2':
                start_time = time.time()
                sortalgs.selection_sort(shields[count])
                sortalgs.selection_sort(shields[count + 1])
                cut_time = time.time() - start_time

            elif selection == '3':
                start_time = time.time()
                sortalgs.bubble_sort(shields[count])
                sortalgs.bubble_sort(shields[count + 1])
                cut_time = time.time() - start_time

            elif selection == '4':
                start_time = time.time()
                sortalgs.merge_sort(shields[count])
                sortalgs.merge_sort(shields[count + 1])
                cut_time = time.time() - start_time

            elif selection == '5':
                start_time = time.time()
                sortalgs.quick_sort(shields[count])
                sortalgs.quick_sort(shields[count + 1])
                cut_time = time.time() - start_time

            else:
                print('\n\n' + 'Attempt failed. Try again.'.center(width))
                print('\n\n' + 'Penalty: -2 points'.center(width))
                total_time -= 2
                broken = False

            if broken:
                print(str(shields[count]).center(width))
                print('\n' + str(shields[count + 1]).center(width))
                print('\n' + ('Shields broken! Points: ' + str(cut_time)).center(width))
                count += 2
                total_time += cut_time
                round_count += 1
                
        proceed = input('\n\n' + '==Continue=='.center(width))
        
    os.system('cls')
    print(' CCCCC  L       EEEEEE    AA    RRRRR   EEEEEE  DDDDD '.center(width))
    print('C       L       E        A  A   R    R  E       D    D'.center(width))
    print('C       L       EEEE    AAAAAA  RRRRR   EEEE    D    D'.center(width))
    print('C       L       E       A    A  R    R  E       D    D'.center(width))
    print(' CCCCC  LLLLLL  EEEEEE  A    A  R    R  EEEEEE  DDDDD '.center(width))
    
    print('\n\n\n' + ('Total points: ' + str(total_time)).center(width))
    proceed = input('\n\n' + '==Continue=='.center(width))
    
def endless_mode():
    running =   1
    total_time = 0
    while running != 11:
        cut_time = 0
        roulette = random.randint(1, 3)
        monster = []
        shield = []
        if roulette == 1: monster = monsters_look.level_one_virus()
        elif roulette == 2: monster = monsters_look.level_two_virus()
        else: roulette = monster = monsters_look.level_three_virus()

        os.system('cls')
        print('  11     0000                DDDDD     AA     SSSSS  H    H'.center(width))
        print(' 1 1    0   00               D    D   A  A   S       H    H'.center(width))
        print('   1    0 00 0  === === ===  D    D  AAAAAA   SSSS   HHHHHH'.center(width))
        print('   1    00   0               D    D  A    A       S  H    H'.center(width))
        print('111111   0000                DDDDD   A    A  SSSSS   H    H'.center(width))
        print('\n\n')
        time.sleep(1)

        for parts in monster: print(parts.center(width))

        if roulette == 1:
            size = random.randint(15, 100)

        elif roulette == 2:
            size = random.randint(15, 100)
            
            for number in range(1, size): shield.append(number)
            
            shield_copy = shield.copy()
            
            while shield == shield_copy:
                random.shuffle(shield)
                
        else:
            size = random.randint(15, 100)
            
            for number in range(size, 0, -1): shield.append(number)
        
        time.sleep(1)
        print('\n\n' + ('Shield ' + str(running) + ':').center(width))
        print('\n' + str(shield).center(width))
        
        time.sleep(0.3)
        print('\n\n' + 'Select your magic: '.center(width))
        time.sleep(0.3)
        print('_______________'.center(width))
        print('| [1] Insertion |'.center(width))
        print('| [2] Selection |'.center(width))
        print('| [3] Bubble    |'.center(width))
        print('| [4] Merge     |'.center(width))
        print('| [5] Quick_____|'.center(width))
        time.sleep(0.3)
        selection = input('\nInput: ')
    
        print('\n' + 'Breaking shield...'.center(width))
        broken = True
        