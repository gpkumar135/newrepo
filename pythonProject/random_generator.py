import random

def gen_random_num(start,end,count=10):


    return[random.randint(start,end) for _ in range(count)]

