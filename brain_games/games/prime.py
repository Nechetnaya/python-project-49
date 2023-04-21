import random
import prompt


def say_conditions():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_random():
    return random.randint(1, 50)


def ask(question):
    return prompt.string(f'Question: {question}\nYour answer: ')


def get_solve(question):
    if question == 1:
        return 'yes'
    else:
        i = 2
        while question % i != 0:
            i += 1
        return 'yes' if i == question else 'no'


def motivate_user(name):
    return f"Let's try again, {name}!"
