#Parametre olarak alacağı 3 adet tamsayının en büyüğünü bulup döndören bir fonksiyon ve 
# bu fonksiyonu bir ana program içerisinde kullanıp sonucunu yazdıran program kodu


def find_largest_int(number1,number2,number3):   
    if number1 > number2 and number1 >number3:
        print("number1 is the largest than other")
    elif number2 > number1 and number2 >number3:
        print("number 2 is the largest than other")
    else:
        print("number 3 is the largest than other")    
find_largest_int(1,2,3)        




