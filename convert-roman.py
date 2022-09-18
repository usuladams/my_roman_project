

def convert(number):
    ones_roman=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens_roman=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hundreds_roman=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thousands_roman=["","M","MM","MMM"]
    
    if int(number)<10:
        return str(ones_roman[int(number)])
    elif int(number)<100:
        tens=int(number[0])
        ones=int(number[1])
        return str(tens_roman[tens])+str(ones_roman[ones])
    elif int(number)<1000:
        hundreds=int(number[0])
        tens=int(number[1])
        ones=int(number[2])
        return str(hundreds_roman[hundreds])+str(tens_roman[tens])+str(ones_roman[ones])
    else:
        thousands=int(number[0])
        hundreds=int(number[1])
        tens=int(number[2])
        ones=int(number[3])
        return str(thousands_roman[thousands])+str(hundreds_roman[hundreds])+str(tens_roman[tens])+str(ones_roman[ones])

info="""
    ###  This program converts decimal numbers to Roman Numerals ###
    (To exit the program, please type "exit")
    Please enter a number between 1 and 3999, inclusively :  """

while True:
    numbers=input(info)

    if numbers.lower()=='exit':
        break
    elif not numbers.isdigit() or int(numbers)<1 or int(numbers)>3999:
        print('Not Valid Input !!!')
    else:
        print(convert(numbers))
