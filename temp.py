import os


def Foo(num_1, num_2, baz=[1, 2]):
    print(os.getenv(num_1))
    return baz == [num_1, num_2]
