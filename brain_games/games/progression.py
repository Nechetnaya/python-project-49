import random
import prompt


def say_conditions():
    return 'What number is missing in the progression?'


def get_random():
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
    return question


def ask(question):
    pr, solve = question
    return int(prompt.string(f'Question: {pr.strip()}\nYour answer: '))


def get_solve(question):
    pr, solve = question
    return solve


def motivate_user(name, answer, solve):
    text_1 = f"'{answer}' is wrong answer ;(. Correct answer was '{solve}'."
    text_2 = f"Let's try again, {name}"
    return f"{text_1}\n{text_2}!"
