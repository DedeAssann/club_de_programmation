def odd(x):
    return x % 2 == 1

a = range(100)

result = filter(odd, a)
print('Original List :', a)
print('Filtered List :', list(result))