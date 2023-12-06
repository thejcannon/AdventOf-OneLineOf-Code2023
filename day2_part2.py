print(
    (
        lambda deque, starmap, reduce, mul: sum(
            map(
                lambda line: reduce(
                    mul,
                    (
                        (
                            lambda maxs, rounds: [
                                deque(
                                    starmap(
                                        lambda count, color: (
                                            (
                                                lambda index: maxs.__setitem__(
                                                    index, max(maxs[index], int(count))
                                                )
                                            )(
                                                0
                                                if color[0] == "r"
                                                else 1
                                                if color[0] == "g"
                                                else 2
                                            )
                                        ),
                                        [
                                            info.split(" ", 1)
                                            for info_str in rounds
                                            for info in info_str.split(", ")
                                        ],
                                    ),
                                    maxlen=0,
                                ),
                                maxs,
                            ][1]
                        )([1, 1, 1], line.split(": ", 1)[1].split("; "))
                    ),
                ),
                __import__("pathlib").Path("input/2").read_text().splitlines(),
            )
        )
    )(
        __import__("collections").deque,
        __import__("itertools").starmap,
        __import__("functools").reduce,
        __import__("operator").mul,
    )
)
