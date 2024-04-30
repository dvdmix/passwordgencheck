import random
import re

while True:
    fch = int(input("Введите, что вы хотите открыть: 1 - генератор паролей, 2 - проверка паролей "))
    if fch == 1:
        letterAmount = int(input("Введите количество символов в пароле (рекомендуемо от 8): "))
        password = []
        letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"№;%:?*()[]#')
        for i in range(0,letterAmount):
            letter = random.choice(letters)
            password.append(letter)        
        passw = ('').join(password)
        print(passw)
    elif fch == 2:
        chpass = input("Введите пароль для проверки: ")
        check = 0
        for i in chpass:
            if i.isupper():
                check += 1
                break
        if re.search(r'[!"#№;%:?*()\[\]]', chpass):
            check+=1
        if re.search(r"1234567890", chpass):
            check+=1
        if len(chpass)>=5:
            check+=1
        if len(chpass)>=10:
            check+=1
        
        if chpass == "cirnofumo":
            print("Браво. Это лучший пароль.")
        elif check == 0:
            print("Этот пароль плохой. Рекомендуется добавить заглавные буквы, разные символы и увеличить длину пароля.")
        elif check == 1:
            print("Этот пароль так себе.")
        elif check == 2:
            print("Этот пароль неплохой.")
        elif check == 3:
            print("Этот пароль хороший.")
        elif check == 4:
            print("Этот пароль отличный.")
        elif check == 5:
            print("Этот пароль замечательный.")
    else:
        break