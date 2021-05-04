"""
s - step
n - next
c - continue
unt - until
l - list
ll - list
p - print
pp - pretty print
"""


num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']


def internal_loop(number):
    if number > 600:
        return
    # import ipdb; ipdb.set_trace()
    for letter in alpha_list:
        print(f'{number} {letter}')


def main_loop():
    for number in num_list:
        internal_loop(number)


if __name__ == '__main__':
    main_loop()
