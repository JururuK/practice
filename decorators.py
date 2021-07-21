def decorator(func):
    def decorated(input_text):
        print('start')
        func(input_text)
        print('end')
    return decorated


@decorator
def introduce(input_text):
    print(input_text)


introduce('Hello world!')