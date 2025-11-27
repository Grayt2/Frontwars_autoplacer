import pyautogui
def place(number, times_to_run):
    '''
    number is to be set to what building you want to place and times to run is the number of them you want to place
    '''
    match number:
        case 1 | 2 | 3 | 4 | 5 | 6:
            print("slow")
            for i in range(0, times_to_run):
                pyautogui.press(str(number), interval=0.015)
                pyautogui.click()
                print(f"\r{i}", end=" ")
        case 0 | 7 | 8 | 9:
            print("fast")
            for i in range(times_to_run):
                pyautogui.press(str(number), _pause=False)
                pyautogui.click()
                print(f"\r{i}", end=" ")
pyautogui.countdown(3)
place(7, 100)