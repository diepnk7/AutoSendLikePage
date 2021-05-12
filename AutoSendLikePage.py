import pyautogui
from time import sleep


print("READY IN 2 SEC")
sleep(2)

# so lan lap quy trinh
j=10
while(1):
    # bam ba cham
    sleep(1)
    r = pyautogui.locateOnScreen(r'C:\Users\yoyal\Desktop\ThucTap\Auto\PyAutoFb\bacham.png')
    if(str(r)=="None"): 
        print("Can't locate ... button") 
        break
    pyautogui.click(r.left+10, r.top+10)
    sleep(1.5)

    # pyautogui.press('tab', presses=1)
    # pyautogui.press('down', presses=5) # sua vi tri  moi ban be
    # pyautogui.press('enter', presses=1)
    # sleep(2)
    
    # click moi ban be
    r = pyautogui.locateOnScreen(r'C:\Users\yoyal\Desktop\ThucTap\Auto\PyAutoFb\moibanbe.png')
    if (str(r)=="None"): 
        print("Can't click Moi ban be")
        break
    pyautogui.click(r.left+10, r.top+10)
    sleep(2)

    # tick ban dau tien
    pyautogui.press('tab', presses=6) 
    pyautogui.press('enter', presses=1)
    
    i=1 
    while(1):
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter', presses=1)
        pyautogui.press('pgdn', presses=1)
        print(str(i) + " sent")
        sleep(0.1)
        i+=1
        if(i==20): # so luong tick
            break
    sleep(1)
    # bam gui loi moi
    a = pyautogui.locateOnScreen(r'C:\Users\yoyal\Desktop\ThucTap\Auto\PyAutoFb\guiloimoi.png')
    if (str(a)=="None"): 
        print("Can't click gui loi moi")
        break
    pyautogui.click(a.left+10, a.top+10) 
    
    j-=1
    if (j==0):
        break

