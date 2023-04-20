import random
import prompt
import operator


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


def get_solve(question, game_name):
    if game_name == 'even':
        return 'yes' if question % 2 == 0 else 'no'
    elif game_name == 'calc':
        action = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }
        a, b, c = question
        return action[c](a, b)
    elif game_name == 'gcd':
        a, b = question
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b


def motivate_user(name, game_name, answer, solve):
    if game_name == 'even':
        return f"Let's try again, {name}!"
    elif game_name == 'calc' or 'gcd':
        return f"'{answer}' is wrong answer ;(. Correct answer was {solve}'.\nLet's try again, {name}!"


def congratulate_user(name):
    print(f'Congratulations, {name}!')
