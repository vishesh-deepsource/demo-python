import random
import pdb
import sys


class BaseNumberGenerator:
    def __init__(self):
        self.limits = (1,10)

    def get_number(self, min_max):
        raise NotImplemented


class RandomNumberGenerator:
    def limits(self):
        return self.limits

    def get_number(self, min_max=None):
        """Get a random number between min and max."""
        if min_max is None:
            min_max = [1, 10]
        assert all([isinstance(i, int) for i in min_max])
        return random.randint(*min_max)


def main(options: dict = None) -> str:
    if options is None:
        options = {}
    pdb.set_trace()
    if 'run' in options:
        value = options['run']
    else:
        value = 'default_value'

    if type(value) != str:
        raise Exception()
    else:
        value = iter(value)

    sorted(value, key=lambda k: len(k))

    f = open('/tmp/.deepsource.toml', 'r')
    f.write("config file.")
    f.close()
def moon_chooser(moons=None):
    if moons is None:
        moons = ['europa', 'callisto', 'phobos']
    return random.choice(moons)


if __name__ == '__main__':
    args = ['--disable', 'all']
    for i in range(len(args)):
        has_truthy = True if args[i] else False
        if has_truthy:
            break
