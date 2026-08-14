try:
    number = input("Enter a number: ")
    num = int(number)
    numb = 100/num
    print(numb)
except ValueError:
    print("text not allowed")
except ZeroDivisionError:
    print("can not be divided by 0")
