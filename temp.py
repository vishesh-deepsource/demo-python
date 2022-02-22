import os


def Foo(num_1, num_2, baz=None):
    """This is a sample function."""
    if baz is None:
        baz = [1, 2]
    print(os.getenv(num_1))
    return baz == [num_1, num_2]
