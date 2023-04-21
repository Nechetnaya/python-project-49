import random
import prompt
import operator


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
        return 'Answer "yes" if the number is even, otherwise answer "no".'
    elif game_name == 'calc':
        return 'What is the result of the expression?'
    elif game_name == 'gcd':
        return 'Find the greatest common divisor of given numbers.'
    elif game_name == 'progression':
        return 'What number is missing in the progression?'


# getting random numbers and a problem
def get_random(game_name):
    if game_name == 'even':
        question = random.randint(1, 1000)
    elif game_name == 'calc':
        a = random.randint(10, 50)
        b = random.randint(1, 10)
        operators = ('+', '*', '-')
        c = random.choice(operators)
        question = (a, b, c)
    elif game_name == 'gcd':
        a = random.randint(20, 100)
        b = random.randint(20, 100)
        question = (a, b)
    elif game_name == 'progression':
        a = random.randint(1, 10)
        b = random.randint(50, 80)
        c = random.randint(3, 8)
        numbers = range(a, b, c)
        progression = list(numbers)[:10]
        i = random.randint(0, len(progression) - 1)
        solve = progression.pop(i)
        progression.insert(i, '..')
        question = (progression, solve)
    else:
        return
    return question


def ask(question, game_name):
    if game_name == 'even':
        return prompt.string(f'Question: {question}\nYour answer: ')
    elif game_name == 'calc':
        a, b, c = question
        return int(prompt.string(f'Question: {a} {c} {b}\nYour answer: '))
    elif game_name == 'gcd':
        a, b = question
        return int(prompt.string(f'Question: {a} {b}\nYour answer: '))
    elif game_name == 'progression':
        progression, solve = question
        return int(prompt.string(f'Question: {str(progression)[1:-1]}\nYour answer: '))


# solves
def solve_even(question):
    return 'yes' if question % 2 == 0 else 'no'


def solve_calc(question):
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    a, b, c = question
    return action[c](a, b)


def solve_gcd(question):
    a, b = question
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


# common solve
def get_solve(question, game_name):
    if game_name == 'even':
        return solve_even(question)
    elif game_name == 'calc':
        return solve_calc(question)
    elif game_name == 'gcd':
        return solve_gcd(question)
    elif game_name == 'progression':
        progression, solve = question
        return solve


def motivate_user(name, game_name, answer, solve):
    if game_name == 'even':
        return f"Let's try again, {name}!"
    elif game_name == 'calc' or 'gcd' or 'progression':
        return f"'{answer}' is wrong answer ;(. Correct answer was {solve}'.\nLet's try again, {name}!"


def congratulate_user(name):
    print(f'Congratulations, {name}!')
