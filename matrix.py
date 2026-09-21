def findNonPositive (mtr: list[list[int]], col: int, row: int) -> list[int] :
    non_pos = []
    neg = True
    for i in range(row) :
        for j in range(col) :
            if mtr[j][i] > 0 :
                neg = False
        if neg == True :
            non_pos.append(i)
        neg = True
    return non_pos

def FindMax (mtr: list[list[int]], row: int) -> int :
    non_pos = findNonPositive(mtr, col, row)
    if len(non_pos) == 0:
        raise ValueError("there is no neg")
    
    max = mtr[0][non_pos[0]]
    for j in non_pos :
        for i in range(row) :
            if mtr[i][j] > max :
                max = mtr[i][j]
    return max

def CountNegBelow (mtr: list[list[int]], col: int, row: int) -> int:
    counter = 0
    for i in range(row) :
            for j in range(col - i - 1, col) :
                if mtr[i][j] < 0 :
                    counter += 1
    return counter


mtr = []
try:
    col = int(input("Give me columns: "))
    row = int(input("Give me rows: "))
    if col <= 0 or row <= 0 :
        raise ValueError("bad user")
    print("Input numbers")

    for i in range(col) :
        array = []
        for j in range(row) :
            array.append(int(input()))
        mtr.append(array)
        
    print(mtr)


    print(f"here is col w no pos {findNonPositive(mtr, col, row)}")
    print(f"Here is max {FindMax(mtr,row)}")
    print(f"There is {CountNegBelow(mtr, col, row)} not pos")
except ValueError as e:
    print(e)