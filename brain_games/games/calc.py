import random
import prompt
import operator


def say_conditions():
    return 'What is the result of the expression?'


def get_random():
    a = random.randint(10, 30)
    b = random.randint(1, 10)
    operators = ('+', '*', '-')
    c = random.choice(operators)
    question = (a, b, c)
    return question


def ask(question):
    a, b, c = question
    return int(prompt.string(f'Question: {a} {c} {b}\nYour answer: '))


def get_solve(question):
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    a, b, c = question
    return action[c](a, b)


def motivate_user(name, answer, solve):
    text_1 = f"'{answer}' is wrong answer ;(. Correct answer was '{solve}'."
    text_2 = f"Let's try again, {name}"
    return f"{text_1}\n{text_2}!"
