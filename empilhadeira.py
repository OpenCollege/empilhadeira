import random
import time


def test1():
    for i in range(1000000):
        random.randint(0, 1)


def test2():
    myList = ['00', '01', '10', '11']
    for i in range(1000000):
        random.choice(myList)


inicio = time.time()
test1()
result = time.time() - inicio

print("Teste 1:")
print(result)

inicio = time.time()
test2()
result = time.time() - inicio

print("Teste 2:")
print(result)
