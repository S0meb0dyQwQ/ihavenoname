

"""minNum = 9
buf = x
while buf > 0:
    digit = buf % 10
    if digit < minNum:
        minNum = digit
    buf //= 10
    
if minNum == 0:
    print(x)
elif minNum == 1:
    print("idk here is 0")

buf = x
new_x = 0
while buf > 0:
    digit = buf % 10
    if digit % minNum != 0:
        new_x = new_x * 10 + digit
    buf //= 10
print(new_x)
 """
 
 
def find_min(digit:int, min_Num: int) -> int:
    return digit if digit < min_Num else min_Num

def make_Number(digit:int, min_Num: int) -> int:
    return digit % min_Num


def dividenum (x:int, func, min_Num, change_min:bool = False) -> int:
    buf = x
    box = 0
    while buf > 0:
        digit = buf % 10
        if change_min:
            box = func(digit, min_Num)
            min_Num = box
        if not change_min :
            if func(digit, min_Num) != 0:
                box = box * 10 + digit
        buf //= 10
    return box if not change_min else min_Num

x = int(input("Give me number "))
try:
    min_Num = dividenum(x,find_min,9,True)
    print(min_Num)
    if min_Num < 2:
        raise ValueError(" your number won't change")
    new_x = dividenum(x,make_Number,min_Num)
    print(new_x)
    new_x = dividenum(new_x,make_Number,min_Num)
    print(new_x)
except ValueError as e:
    print(e)