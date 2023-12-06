print(
    (
        lambda itertools, functools, math: (
            functools.reduce(
                lambda x, y: x * y,
                (
                    lambda time_line, distance_line: itertools.starmap(
                        lambda time, distance: (
                            # There's a little equation this makes: D = (x(T-x)).
                            # So solve that for the two values of x:
                            # (sing the quadratic formula in your head)
                            # x = (T ± √(T^2 - 4D)) / 2.
                            # Lower bound = round(x, when we use -)
                            # Upper bound = round(x, when we use +)
                            # But since that solves for "break even point", we also should handle if x was a whole number
                            #   pre-rounding
                            (
                                lambda sqrt_part: (
                                    lambda upper, lower: (
                                        math.ceil(upper)
                                        if math.modf(upper)[0] > 0
                                        else int(upper) - 1
                                    )
                                    - (
                                        math.floor(lower)
                                        if math.modf(lower)[0] > 0
                                        else int(lower) - 1
                                    )
                                    - 1
                                )(
                                    (time + sqrt_part) / 2,
                                    (time - sqrt_part) / 2,
                                )
                            )(math.sqrt((time**2) - (4 * distance)))
                        ),
                        zip(
                            map(
                                lambda t: int(t.strip()),
                                time_line.split(":")[1].split(),
                            ),
                            map(
                                lambda t: int(t.strip()),
                                distance_line.split(":")[1].split(),
                            ),
                        ),
                    )
                )(*__import__("pathlib").Path("input/6").read_text().splitlines()),
                1,
            )
        )
    )(
        __import__("itertools"),
        __import__("functools"),
        __import__("math"),
    )
)
