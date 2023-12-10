print(
    (
        lambda itertools, grid, starting_point, pipe_action, direction_map, grid_at: next(
            ((value + 1) // 2)
            for info_container in [
                [(direction_map["N"](starting_point)), "N"],
                [(direction_map["E"](starting_point)), "E"],
                [(direction_map["W"](starting_point)), "W"],
                [(direction_map["S"](starting_point)), "S"],
            ]
            if (
                value := (lambda turns: turns if grid_at(info_container) == "S" else 0)(
                    sum(
                        1
                        for _ in itertools.takewhile(
                            lambda _: print(info_container) or info_container[1],
                            (
                                (
                                    lambda location, direction, char: info_container.__setitem__(
                                        1, pipe_action[char].get(direction)
                                    )
                                    or (
                                        info_container.__setitem__(
                                            0,
                                            direction_map[info_container[1]](location),
                                        )
                                        if info_container[1]
                                        else None
                                    )
                                )(
                                    info_container[0],
                                    info_container[1],
                                    grid_at(info_container),
                                )
                                for _ in itertools.repeat(None)
                            ),
                        )
                    )
                )
            )
        )
    )(
        __import__("itertools"),
        grid := list(__import__("pathlib").Path("input/10").read_text().splitlines()),
        next(
            (x, y)
            for x, line in enumerate(grid)
            for y, char in enumerate(line)
            if char == "S"
        ),
        {
            # Maps the tile to a mapping of what direction you're headed based on what direction
            # you've been
            "|": {"N": "N", "S": "S"},
            "-": {"E": "E", "W": "W"},
            "L": {"S": "E", "W": "N"},
            "J": {"S": "W", "E": "N"},
            "7": {"N": "W", "E": "S"},
            "F": {"N": "E", "W": "S"},
            ".": {},
            "S": {},
        },
        # Maps a cardinal direction to a relative coordinate of the next location
        {
            "N": lambda xy: (xy[0] - 1, xy[1]),
            "E": lambda xy: (xy[0], xy[1] + 1),
            "W": lambda xy: (xy[0], xy[1] - 1),
            "S": lambda xy: (xy[0] + 1, xy[1]),
        },
        lambda info_container: grid[info_container[0][0]][info_container[0][1]],
    )
)
