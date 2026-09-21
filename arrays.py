def findMulti(numbers, size: int) -> int:
    multi = 1
    for i in range(0,size, 2):
        multi *= numbers[i]
    return multi

def findFirstNull (numbers, size: int) -> int:
    for i in range(size) :
        if numbers[i] == 0:
            return i
    return -1

def findLastNull (numbers, size: int) -> int:
    for i in range(size - 1, 0, -1) :
        if numbers[i] == 0:
            return i
    return -1


numbers = []
size = int(input("Give me size: "))
print("Input numbers")

for i in range(size) :
    x = int(input())
    numbers.append(x)


print(findMulti(numbers, size))



firstNull = findFirstNull(numbers, size)
print(f"First zero in: {firstNull}")
try:
    if firstNull == -1 :
        raise ValueError("there are no zeros")
    
    lastNull = findLastNull(numbers, size)
    print(f"last zero in: {lastNull}")
    
    if firstNull == lastNull :
        raise ValueError("there only 1 zero")
    
    summ = 0
    for i in range(firstNull, lastNull) :
        summ += numbers[i]
    print(f"here is summ: {summ}")
except ValueError as e:
    print(e)

numbers.sort(key = lambda x: x > 0)
print(numbers)