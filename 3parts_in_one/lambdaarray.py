from train import Train
from train import Train_type
#Part 1
numbers = list(map(int, input("input elements: ").split()))
print(numbers)

summ = sum(numbers)
print(f"summ: {summ}")

print(f"amount: {len(numbers)}")

average = int(summ/len(numbers))
numbers = [average if x == 0 else x for x in numbers]
print(numbers)

''' a = int(input("Input bourder1"))
    b = int(input("Input bourder2"))
'''
a = 3
b = 5
summ = sum(numbers[a: b + 1])
print([x + summ for x in numbers])

#Part 2
with open("source.txt", "r", encoding = "utf-8") as file:
    words = file.read().split()
print(words)

print(sorted(words))

a = "t" #input("Input letter: ")
print([x for x in words if x.startswith(a)])

a = "t" #input("Input letter: ")
words = [x for x in words if not x.startswith(a)]
print(words)

#Part 3
depo = []
with open("trains.txt", "r", encoding = "utf-8") as file:
    for line in file:
        train = Train.make_train(line)
        depo.append(train)
print(depo)

depo.sort(key = lambda x: x.time)
print(depo)

start = "8:00" #input("Input border 1: ")
end = "15:00" #input("Input border 2: ")
print([x for x in depo if x.time < end and x.time > start])

place = "Home" #input("Input place: ")
print([x for x in depo if x.name == place])

print([x for x in depo if x.name == place and x.type == Train_type["fast"]])

good_one = [x for x in depo if x.name == place]
print(min(good_one, key = lambda x: x.road_time))