import random

def fisher_yates_shuffle(l):
    for i in range(0, len(l)):
        random_index = random.randint(0, len(l) - 1)
        l[random_index], l[i] = l[i], l[random_index]