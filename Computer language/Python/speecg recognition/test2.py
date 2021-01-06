from threading import Thread
import time
import random

def listen():
    print('                                                                     listening....')
    return 1

def one():
    for i in range(5):
        print('                           one')
def two():
    for i in range(5):
        print('                           two')
def three():
    for i in range(5):
        print('                           three')
def four():
    for i in range(5):
        print('                           four')

def recognize(on):
    print('                                                recogning.....')
    time.sleep(1)
    query = random.randint(1,4)
    print(f'                                                                    {on}  recognized')

    if 1 == query:
        one()
    elif 2 == query:
        two()
    elif 3 == query:
        three()
    elif 4 == query:
        four()


if __name__ == '__main__':
    start = time.perf_counter()
    for _ in range(10):
        audio = listen()
        t = Thread(target=recognize,args=[audio])
        t.start()
    end = time.perf_counter()
    print(f'total time : {end-start}')


#  10.4460739

