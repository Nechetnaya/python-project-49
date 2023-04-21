import random
import prompt


def say_conditions():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random():
    return random.randint(1, 50)


def ask(question):
    return prompt.string(f'Question: {question}\nYour answer: ')


def get_solve(question):
    return 'yes' if question % 2 == 0 else 'no'


def motivate_user(name):
    return f"Let's try again, {name}!"
