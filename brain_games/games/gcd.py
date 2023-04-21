import random
import prompt


def say_conditions():
    return 'Find the greatest common divisor of given numbers.'


def get_random():
    a = random.randint(20, 100)
    b = random.randint(20, 100)
    question = (a, b)
    return question


def ask(question):
    a, b = question
    return int(prompt.string(f'Question: {a} {b}\nYour answer: '))


def get_solve(question):
    a, b = question
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def motivate_user(name, answer, solve):
    text_1 = f"'{answer}' is wrong answer ;(. Correct answer was '{solve}'."
    text_2 = f"Let's try again, {name}"
    return f"{text_1}\n{text_2}!"
