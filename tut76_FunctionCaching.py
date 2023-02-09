import time
from functools import lru_cache

@lru_cache(maxsize=3) ## latest 3 entry are saved
def some_Work(n):
    ## some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_Work(3)  ## run in single and store in cache
    print("done...calling again")
    some_Work(3)
    print("called again")

