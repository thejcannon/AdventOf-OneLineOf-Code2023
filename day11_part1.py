# NOTE: I wanted to try and do one without lambdas...
(
    (
        universe := list(
            list(row)
            for row in __import__("pathlib").Path("input/11").read_text().splitlines()
        )
    )
    and (collections := __import__("collections"))
    and (bisect := __import__("bisect"))
    and (itertools := __import__("itertools"))
    # Index the galaxies, and keep track of the rows/cols which have no galaxy
    and (galaxy_coords := [])
    or (galaxyless_rows := set(range(len(universe))))
    and (galaxyless_cols := set(range(len(universe[0]))))
    and (
        collections.deque(
            (
                (
                    galaxy_coords.append([x, y])
                    or galaxyless_rows.discard(x)
                    or galaxyless_cols.discard(y)
                )
                if char == "#"
                else None
                for x, row in enumerate(universe)
                for y, char in enumerate(row)
            ),
            maxlen=0,
        )
    )
    or (galaxyless_rows := sorted(galaxyless_rows))
    and (galaxyless_cols := sorted(galaxyless_cols))
    # (originally I "blew up the universe", but then did nothing with it.
    #   So after reading part 2 I realized that and removed the dead code
    # )
    # Iterate the known galaxies, and increment them by the number of rows and columns
    # that got expanded between them and the "origin".
    or (
        collections.deque(
            (
                galaxy_coords.__setitem__(
                    index,
                    (
                        x + bisect.bisect_left(galaxyless_rows, x),
                        y + bisect.bisect_left(galaxyless_cols, y),
                    ),
                )
                for index, (x, y) in enumerate(galaxy_coords)
            ),
            maxlen=0,
        )
    )
    # Now calculate all pairs of coordinates
    # First if the rows and cols dont match, we travel diagonally
    # Then, we travel either horizontally or vertically
    # What this boils down to is calculating the amount of steps of each we'd do
    # and just doing the math (rather than playing it out)
    or (
        offsets := (
            (abs(a[0] - b[0]), abs(a[1] - b[1]))
            for a, b, in itertools.combinations(galaxy_coords, 2)
        )
    )
    and (
        result := sum(
            (min(*offset) * 2) + (max(*offset) - min(*offset)) for offset in offsets
        )
    )
    and print(result)
)
