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
        return even.say_conditions()
    elif game_name == 'calc':
        return calc.say_conditions()
    elif game_name == 'gcd':
        return gcd.say_conditions()
    elif game_name == 'progression':
        return progression.say_conditions()
    elif game_name == 'prime':
        return prime.say_conditions()


# getting random numbers and a problem
def get_random(game_name):
    if game_name == 'even':
        return even.get_random()
    elif game_name == 'calc':
        return calc.get_random()
    elif game_name == 'gcd':
        return gcd.get_random()
    elif game_name == 'progression':
        return progression.get_random()
    elif game_name == 'prime':
        return prime.get_random()


def ask(question, game_name):
    if game_name == 'even':
        return even.ask(question)
    elif game_name == 'calc':
        return calc.ask(question)
    elif game_name == 'gcd':
        return gcd.ask(question)
    elif game_name == 'progression':
        return progression.ask(question)
    elif game_name == 'prime':
        return prime.ask(question)


def get_solve(question, game_name):
    if game_name == 'even':
        return even.get_solve(question)
    elif game_name == 'calc':
        return calc.get_solve(question)
    elif game_name == 'gcd':
        return gcd.get_solve(question)
    elif game_name == 'progression':
        return progression.get_solve(question)
    elif game_name == 'prime':
        return prime.get_solve(question)


def motivate_user(name, game_name, answer, solve):
    if game_name == 'even':
        return even.motivate_user(name)
    elif game_name == 'calc':
        return calc.motivate_user(name, answer, solve)
    elif game_name == 'gcd':
        return gcd.motivate_user(name, answer, solve)
    elif game_name == 'progression':
        return progression.motivate_user(name, answer, solve)
    elif game_name == 'prime':
        return prime.motivate_user(name)


def congratulate_user(name):
    print(f'Congratulations, {name}!')
