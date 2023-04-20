import random
import prompt


def lets_play(game_name):
    name = welcome_user()
    print(say_conditions(game_name))
    i = 0
    while i < 3:
        question = get_random(game_name)
        answer = ask(question, game_name)
        solve = get_solve(question, game_name)
        if answer == solve:
            print('Correct!')
            i = i + 1
        else:
            return print(motivate_user(name, game_name))
    congratulate_user(name)


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def say_conditions(game_name):
    if game_name == 'even':
        return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random(game_name):
    if game_name == 'even':
        return random.randint(1, 1000)


def ask(question, game_name):
    if game_name == 'even':
        return prompt.string(f'Question: {question}\nYour answer: ')


def get_solve(question, game_name):
    if game_name == 'even':
        return 'yes' if question % 2 == 0 else 'no'


def motivate_user(name, game_name):
    if game_name == 'even':
        return f"Let's try again, {name}!"


def congratulate_user(name):
    print(f'Congratulations, {name}!')
