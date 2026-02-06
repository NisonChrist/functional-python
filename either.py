class Either:
    def __init__(self, left, right):
        self._left = left
        self._right = right

    @staticmethod
    def of(left, right):
        return Either(left, right)

    def map(self, fn):
        if self._right:
            return Either.of(self._left, fn(self._right))
        else:
            return Either.of(self._left, self._right)

    def __str__(self):
        return f"{self.__class__.__name__}({self._left}, {self._right})"


def main():
    print(Either.of("Error", None).map(lambda x: x + 1))  # Either("Error", None)
    print(Either.of("Error", 0).map(lambda x: x + 1))  # Either("Error", 1)
    print(Either.of("Error", 99).map(lambda x: x + 1))  # Either("Error", 100)
    print(
        Either.of("Error", 99).map(lambda x: x + 1).map(lambda x: x * x)
    )  # Either("Error", 10000)


if __name__ == "__main__":
    main()
