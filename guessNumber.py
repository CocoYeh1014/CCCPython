import random
num = random.randint(1,10)
time = 0
while True:
    guess = int(input('num?'))
    if guess < num:
        print('bigger')
        time+=1
        if time>5:
            print('over 5 times')
            break
    elif guess > num:
        print('smaller')
        time+=1
        if time>5:
            print('over 5 times')
            break
    else:
        print('right')
        print('guess',time,'times')
        break
