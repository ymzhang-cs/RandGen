import random
from time import time


def randGenerate(lR, rR, n):
    """
    生成[rL,rR]范围内的n个随机数
    """
    lR = int(lR)
    rR = int(rR)
    n = int(n)
    tick = time()
    random.seed(tick)
    if rR - lR + 1 < n:
        raise ValueError("无法生成指定数量的不重复随机数，因为范围太小。")
    random_numbers = sorted(random.sample(range(lR, rR + 1), n))
    return random_numbers, tick

if __name__ == "__main__":
    print(randGenerate(10,30,5))