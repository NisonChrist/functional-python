class Functor:
    def __init__(self, value):
        self._value = value

    @staticmethod
    def of(value):
        return Functor(value)

    def map(self, fn):
        return Functor(fn(self._value))

    def __str__(self):
        return f"Functor({self._value})"


def main():
    print(Functor.of(2).map(lambda x: x + 1))  # Functor(3)
    print(Functor.of(-1).map(lambda x: x + 1))  # Functor(0)
    print(Functor.of(0).map(lambda x: x + 1))  # Functor(1)
    print(Functor.of(99).map(lambda x: x + 1))  # Functor(100)
    print(Functor.of(99).map(lambda x: x + 1).map(lambda x: x * x))  # Functor(10000)


if __name__ == "__main__":
    main()
