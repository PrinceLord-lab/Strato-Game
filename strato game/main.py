import os
import time
import levels

running = True
while running:
    main_menu_selection = '0'
    main_menu_selection = levels.main_menu()
    
    if main_menu_selection == '1':
        level_selection = '0'
        level_selection = levels.level_selection()
        
        if level_selection == '1':
            levels.level_one()
            
        elif level_selection == '2':
            levels.level_two()
            
        elif level_selection == '3':
            levels.level_three()
            
        else: pass
    
    elif main_menu_selection == '2':
        levels.ten_dash_mode()
    
    elif main_menu_selection == '3':
        running = False
        
    else: pass
        
os.system('cls')
    