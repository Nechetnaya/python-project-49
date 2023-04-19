import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congratulate_user(name_user):
    print(f'Congratulations, {name_user}!')


def motivate_user(name_user):
    print(f"Let's try again, {name_user}!")
