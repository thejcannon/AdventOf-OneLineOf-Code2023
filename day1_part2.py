print(
    next(
        (
            __import__("itertools").starmap(
                lambda lookup, lines: sum(
                    map(
                        lambda mv: (
                            next(
                                v
                                for index in range(len(mv))
                                for k, v in lookup.items()
                                for p in k
                                if mv[index : index + len(p)] == p
                            )
                            * 10
                            + next(
                                v
                                for index in reversed(range(len(mv), 0, -1))
                                for k, v in lookup.items()
                                for p in k
                                if mv[-index : len(mv) - index + len(p)] == p
                            )
                        ),
                        map(memoryview, lines),
                    )
                ),
                [
                    (
                        {
                            (b"1", b"one"): 1,
                            (b"2", b"two"): 2,
                            (b"3", b"three"): 3,
                            (b"4", b"four"): 4,
                            (b"5", b"five"): 5,
                            (b"6", b"six"): 6,
                            (b"7", b"seven"): 7,
                            (b"8", b"eight"): 8,
                            (b"9", b"nine"): 9,
                        },
                        __import__("pathlib").Path("input/1").read_bytes().splitlines(),
                    )
                ],
            )
        )
    )
)
