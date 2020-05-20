lower_camel = input()


def lower_camel_to_snake(base_string):
    snake = ''
    for char in base_string:
        if char.isupper():
            snake += '_' + char.lower()
        else:
            snake += char


print(lower_camel_to_snake(lower_camel))
