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
    elif game_name == 'prime':
        return 'Answer "yes" if given number is prime. Otherwise answer "no".'


# getting random numbers and a problem
def get_random(game_name):
    if game_name in ['even', 'prime']:
        question = random.randint(1, 50)
    elif game_name == 'calc':
        a = random.randint(10, 30)
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
        pr = list(numbers)[:10]
        i = random.randint(0, len(pr) - 1)
        solve = pr.pop(i)
        pr.insert(i, '..')
        pr_0 = ''
        for item in pr:
            pr_0 += str(item) + ' '
        pr = pr_0
        question = (pr, solve)
    else:
        return
    return question


def ask(question, game_name):
    if game_name in ['even', 'prime']:
        return prompt.string(f'Question: {question}\nYour answer: ')
    elif game_name == 'calc':
        a, b, c = question
        return int(prompt.string(f'Question: {a} {c} {b}\nYour answer: '))
    elif game_name == 'gcd':
        a, b = question
        return int(prompt.string(f'Question: {a} {b}\nYour answer: '))
    elif game_name == 'progression':
        pr, solve = question
        return int(prompt.string(f'Question: {pr.strip()}\nYour answer: '))


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


def solve_prime(question):
    if question == 1:
        return 'yes'
    else:
        i = 2
        while question % i != 0:
            i += 1
        return 'yes' if i == question else 'no'


# common solve
def get_solve(question, game_name):
    if game_name == 'even':
        return solve_even(question)
    elif game_name == 'calc':
        return solve_calc(question)
    elif game_name == 'gcd':
        return solve_gcd(question)
    elif game_name == 'progression':
        pr, solve = question
        return solve
    elif game_name == 'prime':
        return solve_prime(question)


def motivate_user(name, game_name, answer, solve):
    if game_name in ['even', 'prime']:
        return f"Let's try again, {name}!"
    elif game_name in ['calc', 'gcd', 'progression']:
        text_1 = f"'{answer}' is wrong answer ;(. Correct answer was '{solve}'."
        text_2 = f"Let's try again, {name}"
        return f"{text_1}\n{text_2}!"


def congratulate_user(name):
    print(f'Congratulations, {name}!')
