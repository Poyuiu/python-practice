# guess number game
import random

answer = random.randint(1, 100)
guess = 0
rangeDown = 1
rangeUp = 100
guess_cnt = 0
guess_limit = 5

while answer != int(guess) and guess_cnt < guess_limit:
    print('you remain ' + str(guess_limit - guess_cnt) + ' times to guess')
    guess = input('please text a number from ' + str(rangeDown) + ' to ' + str(rangeUp) + ': ')
    guess_cnt += 1
    if int(guess) > answer:
        rangeUp = guess
    else:
        rangeDown = guess

if int(guess) == answer:
    print('congratulate! the answer is ' + str(answer))
else:
    print('sorry, you lose. and the answer is ' + str(answer))
