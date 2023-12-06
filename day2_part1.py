print(
    (
        lambda takewhile, limits: sum(
            map(
                lambda line: (
                    (
                        lambda game_header, rounds_str: (
                            lambda rounds: int(game_header.split(" ", 1)[1])
                            if len(rounds)
                            == sum(
                                1
                                for _ in takewhile(
                                    lambda round_str: (
                                        lambda round: len(round)
                                        == sum(
                                            1
                                            for _ in takewhile(
                                                lambda info_str: (
                                                    lambda count, color: int(count)
                                                    <= limits[color]
                                                )(*info_str.split(" ", 1)),
                                                round,
                                            )
                                        )
                                    )(round_str.split(", ")),
                                    rounds,
                                )
                            )
                            else 0
                        )(rounds_str.split("; "))
                    )(*line.split(": ", 1))
                ),
                __import__("pathlib").Path("input/2").read_text().splitlines(),
            )
        )
    )(
        __import__("itertools").takewhile,
        {
            "red": 12,
            "green": 13,
            "blue": 14,
        },
    )
)
