percentage = eval(input('Enter the percentage'))

if type(percentage) in [int,float]:
    if percentage >=0 and percentage <35:
        print('Fail')
    elif percentage >=35 and percentage <60:
        print('pass')
    elif percentage >=60 and percentage <70:
        print('C')
    elif percentage >=70 and percentage <80:
        print('B')
    elif percentage >=80  and percentage <90:
        print('A')
    elif percentage >= 90 and percentage <=100:
        if percentage>=95:
            print('A++++++')
        else:
            print('A+')
    else:
        print('enter Valid marks')

else:
    print('invalid input')

