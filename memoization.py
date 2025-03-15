# It's a technique to memory optimization by storing the expensive function calls
# and returning the results from cache when same inputs occur again
import time
ef_cache ={}
def expensive_function(num):
    if (num in ef_cache):
        return ef_cache[num]
    print(f'Computing {num}')
    # programme sleeps for 1sec
    time.sleep(1)
    result = num**2
    ef_cache[num] = result
    return result

print(expensive_function(2))
print(expensive_function(4))
print(expensive_function(2))
print(expensive_function(4))
