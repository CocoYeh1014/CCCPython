import random
answer = random.randint(1,10)
while True:
    guess = int(input('Gess a number?'))
    if guess==answer:
        print('right')
        break
    elif guess<answer:
        print('bigger')
    else:
        print('smaller')
