def get_random_password(n=8) -> str:
    from random import sample
    p = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    pas = ''.join(sample(p, n))
    return pas
    #  написать функцию генерации случайных паролей


print(get_random_password())
