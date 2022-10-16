import pyautogui
import time

while True:
    #chao1=pyautogui.locateOnScreen('chao1.png')
    #if chao1!=None:
    #    print('achei1')
    #    s2=pyautogui.center(chao1)
    #    d2=list(s2)
    #    pyautogui.click(pyautogui.moveTo(d2[0],d2[1]))
    #    time.sleep(2)
    #else:
    #    print('n achei chao1')
    #chao2=pyautogui.locateOnScreen('chao2.png')
    #if chao2!=None:
    #    print('achei2')
    #    s1=pyautogui.center(chao2)
    #    d1=list(s1)
     #   pyautogui.click(pyautogui.moveTo(d1[0],d1[1]))
    #    time.sleep(2)
    #else:
    #    print('n achei chao2')

    xicara=pyautogui.locateOnScreen('xicara.png',confidence=0.9)
    if xicara!=None:
        print('achei dxicara')
        sxicara=pyautogui.center(xicara)
        dxicara=list(sxicara)
        pyautogui.click(pyautogui.moveTo(dxicara[0],dxicara[1]))
        time.sleep(1)
    else:
        print('nao achei dxicara')
    xicara2=pyautogui.locateOnScreen('xicara2.png')
    if xicara2!=None:
        print('achei dxicara2')
        sxicara2=pyautogui.center(xicara2)
        dxicara2=list(sxicara2)
        pyautogui.rightClick(pyautogui.moveTo(dxicara2[0],dxicara2[1]))
        time.sleep(1)
    else:
        print('nao achei dxicara2')
    xicara3=pyautogui.locateOnScreen('xicara3.png')
    if xicara3!=None:
        print('achei dxicara3')
        sxicara3=pyautogui.center(xicara3)
        dxicara3=list(sxicara3)
        pyautogui.click(pyautogui.moveTo(dxicara3[0],dxicara3[1]))
        time.sleep(1)
    else:
        print('nao achei dxicara3')
