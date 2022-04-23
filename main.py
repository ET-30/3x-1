number = int(input("number : "))

while True:
    if (number % 2) == 0:
        print("{0} Even" .format(number))
        number = number / 2
   
    else:
     if number == 1:
         print("1.0 Odd (loop)")
         quit()
     print("{0} Odd" .format(number))
     number =  number * 3 + 1 
     