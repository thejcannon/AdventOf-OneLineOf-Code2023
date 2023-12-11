print(
    (
        lambda itertools, collections: sum(
            map(
                lambda line: (
                    (
                        lambda numbers: sum(
                            itertools.takewhile(
                                lambda diff: any(numbers) or diff != 0,
                                (
                                    collections.deque(
                                        itertools.starmap(
                                            lambda index, xy: numbers.__setitem__(
                                                index, xy[1] - xy[0]
                                            ),
                                            enumerate(itertools.pairwise(numbers)),
                                        ),
                                        maxlen=0,
                                    )
                                    or numbers.pop()
                                    for _ in itertools.repeat(None)
                                ),
                            )
                        )
                    )(list(map(int, line.split())))
                ),
                __import__("pathlib").Path("input/9").read_text().splitlines(),
            )
        )
    )(
        __import__("itertools"),
        __import__("collections"),
    )
)
