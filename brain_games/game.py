import prompt
from brain_games.games import even, calc, gcd, prime, progression


# gameplay
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
            return print(motivate_user(name, game_name, answer, solve))
    congratulate_user(name)


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def say_conditions(game_name):
    if game_name == 'even':
        conditions = even.say_conditions()
    elif game_name == 'calc':
        conditions = calc.say_conditions()
    elif game_name == 'gcd':
        conditions = gcd.say_conditions()
    elif game_name == 'progression':
        conditions = progression.say_conditions()
    elif game_name == 'prime':
        conditions = prime.say_conditions()
    return conditions


# getting random numbers and a problem
def get_random(game_name):
    if game_name == 'even':
        random = even.get_random()
    elif game_name == 'calc':
        random = calc.get_random()
    elif game_name == 'gcd':
        random = gcd.get_random()
    elif game_name == 'progression':
        random = progression.get_random()
    elif game_name == 'prime':
        random = prime.get_random()
    return random


def ask(question, game_name):
    if game_name == 'even':
        output = even.ask(question)
    elif game_name == 'calc':
        output = calc.ask(question)
    elif game_name == 'gcd':
        output = gcd.ask(question)
    elif game_name == 'progression':
        output = progression.ask(question)
    elif game_name == 'prime':
        output = prime.ask(question)
    return output


def get_solve(question, game_name):
    if game_name == 'even':
        solve = even.get_solve(question)
    elif game_name == 'calc':
        solve = calc.get_solve(question)
    elif game_name == 'gcd':
        solve = gcd.get_solve(question)
    elif game_name == 'progression':
        solve = progression.get_solve(question)
    elif game_name == 'prime':
        solve = prime.get_solve(question)
    return solve


def motivate_user(name, game_name, answer, solve):
    if game_name == 'even':
        motivation = even.motivate_user(name)
    elif game_name == 'calc':
        motivation = calc.motivate_user(name, answer, solve)
    elif game_name == 'gcd':
        motivation = gcd.motivate_user(name, answer, solve)
    elif game_name == 'progression':
        motivation = progression.motivate_user(name, answer, solve)
    elif game_name == 'prime':
        motivation = prime.motivate_user(name)
    return motivation


def congratulate_user(name):
    print(f'Congratulations, {name}!')
