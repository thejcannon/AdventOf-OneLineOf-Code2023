print(
    (
        lambda functools, itertools, collections: sum(
            map(
                lambda line: (
                    (
                        lambda numbers: functools.reduce(
                            lambda sum, y: (sum - y[1])
                            if y[0] % 2 == 1
                            else (sum + y[1]),
                            enumerate(
                                itertools.takewhile(
                                    lambda diff: any(numbers) or diff != 0,
                                    (
                                        collections.deque(
                                            itertools.starmap(
                                                lambda index, xy: numbers.__setitem__(
                                                    index + 1, xy[1] - xy[0]
                                                ),
                                                enumerate(itertools.pairwise(numbers)),
                                            ),
                                            maxlen=0,
                                        )
                                        or numbers.pop(0)
                                        for _ in itertools.repeat(None)
                                    ),
                                )
                            ),
                            0,
                        )
                    )(list(map(int, line.split())))
                ),
                __import__("pathlib").Path("input/9").read_text().splitlines(),
            )
        )
    )(
        __import__("functools"),
        __import__("itertools"),
        __import__("collections"),
    )
)
