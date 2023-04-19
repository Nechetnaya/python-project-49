from brain_games.func import welcome_user, motivate_user, congratulate_user
import random
import prompt


def check_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1, 1000)
        solve = 'yes' if number % 2 == 0 else 'no'
        if prompt.string(f'Question: {number}\nYour answer: ') == solve:
            print('Correct!')
            i = i + 1
        else:
            motivate_user(name)
            return
    congratulate_user(name)
