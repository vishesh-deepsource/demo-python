import os


def Foo(num_1, num_2, baz=[1, 2]):
    assert baz == [num_1, num_2]
    return True
