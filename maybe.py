from functor import Functor


class Maybe(Functor):
    def __init__(self, value):
        super(Maybe, self).__init__(value)

    @staticmethod
    def of(value):
        return Maybe(value)

    def map(self, fn):
        if self._value is None:
            return Maybe(None)
        else:
            return Maybe(fn(self._value))

    def __str__(self):
        return f"Maybe({self._value})"


def main():
    print(Maybe.of(None).map(lambda x: x + 1))  # Maybe(None)
    print(Maybe.of(None).map(lambda x: x * x))  # Maybe(None)
    print(Maybe.of(0).map(lambda x: x + 1))  # Maybe(1)
    print(Maybe.of(99).map(lambda x: x + 1))  # Maybe(100)
    print(Maybe.of(99).map(lambda x: x + 1).map(lambda x: x * x))  # Maybe(10000)


if __name__ == "__main__":
    main()
