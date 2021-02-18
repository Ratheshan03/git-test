print("   Multipliactions   ")
print(" 1 2 3 4 5 6 7 8 9 ")
print('----------------------------')
for i in range(1, 10):
    print(i, '', '|', end='')
    for y in range(1, 10):
        print(i*y, '', end='')
    print()
