import random
import time

start_time = time.time()
answers = [[], [], [], [], [], [], [], [], [], []]
for i in range(10):
    num1 = 0
    num2 = 0
    while num1 <= num2:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    print(f'What is {num1} - {num2} ? ')
    answer = int(input(': '))
    sub = num1-num2
    if sub == answer:
        print("You are correct!")
        s = 'correct'
    else:
        print("Your answer is wrong. ")
        print(f'{num1}-{num2} should be {sub}')
        s = 'wrong'

    answers[i].append(num1)
    answers[i].append(num2)
    answers[i].append(answer)
    answers[i].append(s)

print()
End_time = time.time() - start_time
print(f'Test time is {End_time} seconds')
for i in range(10):
    print(
        f'{answers[i][0]} - {answers[i][1]} = {answers[i][2]} {answers[i][3]}')
        
print()
