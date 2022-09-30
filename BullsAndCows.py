"""
一個人設定一組四碼不重覆的數字(0~9)作為謎底，另一方猜。每猜一個數，出數者就要根據這個數字給出提示，提示以XAYB形式呈現，直到猜中為止。
其中X表示位置正確的數的個數，而Y表示數字正確而位置不對的數的個數。
例如，當謎底為8123，而猜謎者猜1052時，出題者必須提示0A2B。例如，當謎底為5637，而猜謎者猜4931時，出題者必須提示1A0B。

請完成底下函式: 
隨機產生一組四碼數字的作為謎底 (程式以字串型態表示,如’8123’)
能依據出數者猜的數字給出提示XAYB
 check (’1052’) returns ’0A2B’
設計一個主程式，讓出數者可不斷猜數字，直到猜錯累計達10次為止 
"""
import random

def setEnigma(answer) :    
    temp =list(range(0,10))
    random.shuffle(temp)#random
    answer[0] = temp[0]
    answer[1] = temp[1] 
    answer[2] = temp[2]
    answer[3] = temp[3]    

def checkChar(char,index):
    value = enigmaString.find(char)
    #print(char)
    #print(index)
    returnA = 0
    returnB = 0
    if (value < 0) :#未找到
        pass
    elif (value == index):#字元完全符合
        returnA = 1
    else:#有找到,位置不符
        returnB = 1
    return returnA,returnB

def check(yourInput) :
    if (yourInput == enigmaString):#字串完全符合
       return True
    resultA = 0
    resultB = 0   
    for _ in range(4):
        a,b = checkChar(yourInput[_],_)
        resultA += a
        resultB += b
    print(str(resultA)+"A"+str(resultB)+"B")
    return False   

enigma = list(range(1,5))
setEnigma(enigma)
print(enigma)
enigmaString = ''.join(str(e) for e in enigma)
result = False 
while(result == False):
    tempInput = input("猜數字(四位數):")
    result = check(tempInput)  
    
print('Congratulations!')    
