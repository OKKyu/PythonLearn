#!python3
# -*- coding:utf-8 -*-
import numpy as np


def monty_hole_show(window_num = 3, change_decide = False, guest:int=0):
    '''
      This method is simulating process that monty show at one time.
    '''
    #debug
    print("guest " + str(guest))
    
    #operation set to one window by correct value(car) at random.
    correct_win_num = np.random.randint(0, window_num)
    print("  correct_window_number is, " + str(correct_win_num))
    
    #guest choise one window.
    choice_win_num = np.random.randint(0, window_num)
    print("  first selected window by guest is, " + str(choice_win_num))
    
    #monthy leak answer about one window is uncorrect(goat).
    monthy_leak_num = np.random.randint(0, window_num)
    while True:
        if monthy_leak_num != correct_win_num and monthy_leak_num != choice_win_num:
            break
        else:
            monthy_leak_num = np.random.randint(0, window_num)
    print("  monty leak one answer that not selected by guest, " + str(monthy_leak_num))
    
    #if guest will decide to changing before choise, rechoise one window that exclude leaked by monty.
    if change_decide == True:
        rechoice_num = np.random.randint(0, window_num)
        while True:
            if monthy_leak_num != rechoice_num and rechoice_num != choice_win_num:
                break
            else:
                rechoice_num = np.random.randint(0, window_num)
        choice_win_num = rechoice_num
        print("  then, guest rechoise window is, " + str(choice_win_num))
    else:
        print("  but, guest is not changing decision himself.")
        
    #judge if these is equal that correct window and guest's prediction.
    if correct_win_num == choice_win_num:
        return 1
    else:
        return 0

#common_setting
guest_num = 100
window_num = 3

#In case of that gusest no change first dicision.
get_car_num_no_changed = 0
for i in range(guest_num):
    get_car_num_no_changed += monty_hole_show(window_num, change_decide=False, guest=i)

#In case of that gusest change first dicision after monty leaked one answer.
get_car_num_changed = 0
for i in range(guest_num):
    get_car_num_changed += monty_hole_show(window_num, change_decide=True, guest=i)

#result of experiment.
print("report that result of experiment....")
print("In Case of that guests no changed first decision, getting car num is, " + str(get_car_num_no_changed))
print("In Case of that guests change first decision, getting car num is, " + str(get_car_num_changed))
