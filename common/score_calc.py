import random
from typing import Tuple

def score_calc(income: int) -> Tuple:
    num = random.randint(1, 999)
    if num <= 299:
        credit = 0
    elif (num > 299) & (num <= 599):
        credit = 1000
    elif (num > 599) & (num <= 799):
        if income*1.5 <= 1000:
            credit = 1000
        else:
            credit = income*1.5
    elif (num > 799) & (num <= 950):
        credit = income*2
    else:
        credit = 1000000

    return num, credit
