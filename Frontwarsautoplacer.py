import pyautogui
def place(number, times_to_run):
    '''
    number is to be set to what building you want to place and times to run is the number of them you want to place
    '''
    try:
        match number:
            case 1 | 2 | 3 | 4 | 5 | 6:
                print("slow")
                for p in range(0, times_to_run):
                    pyautogui.press(str(number), interval=0.015)
                    pyautogui.click()
                    print(f"\r{i}", end=" ")
            case 0 | 7 | 8 | 9:
                print("fast")
                for p in range(times_to_run):
                    pyautogui.press(str(number), _pause=False)
                    pyautogui.click()
                    print(f"\r{i}", end=" ")
        if number > 9:
            print("Value Error [Value must be {0, 9}]!")
    except:
        print("Ended!")
put = input("Enter the item you want to place [0, 9], and the number of times you want it to run for: ")
i = put.split(", ")
pyautogui.countdown(3)
try:
    place(int(i[0]), int(i[1]))
except ValueError:
    print("Value Incorrect Error1 [Value must be an integer]!")
