print(
    sum(
        map(
            (
                lambda line: (
                    int(next(c for c in line if c.isdigit())) * 10
                    + int(next(c for c in reversed(line) if c.isdigit()))
                )
            ),
            __import__("pathlib").Path("input/1").read_text().splitlines(),
        )
    )
)
