import random
#from typing import Tuple

def score_calc(income):
    income = float(income)
    print(income)
    num = random.randint(1, 999)
    print(num)
    if num <= 299:
        credit = 0.0
        approval = 'NO'
    elif (num > 299) & (num <= 599):
        credit = 1000
        approval = 'YES'
    elif (num > 599) & (num <= 799):
        approval = 'YES'
        if income*1.5 <= 1000.0:
            credit = 1000.0
        else:
            credit = income*1.5
    elif (num > 799) & (num <= 950):
        approval = 'YES'
        credit = income*2
    else:
        credit = 1000000.0
        approval = 'YES'
    print(credit)
    return num, credit, approval
