print(
    (
        lambda engine, collections, itertools, symbol_indexes, numbers_by_index, numberindex_by_position, digit_container, offsets:
        # First parse the grid
        collections.deque(
            itertools.starmap(
                lambda row_index, row: collections.deque(
                    itertools.starmap(
                        lambda col_index, char: (
                            digit_container.append(
                                int(char) * (10 ** len(digit_container))
                            )
                        )
                        if char.isdigit()
                        else (
                            [
                                # Always try and build the last parsed number
                                (
                                    collections.deque(
                                        map(
                                            # Because there are duplicates, we track numbers by their position, and use that to uniquely identify the number
                                            lambda offset: numberindex_by_position.__setitem__(
                                                (row_index, col_index + 1 + offset),
                                                (row_index, col_index + 1),
                                            ),
                                            range(len(digit_container)),
                                        ),
                                        maxlen=0,
                                    )
                                    # Store the number's index -> number
                                    or numbers_by_index.__setitem__(
                                        (row_index, col_index + 1), sum(digit_container)
                                    )
                                    # Clear the parsing container
                                    or digit_container.clear()
                                )
                                if digit_container
                                else None,
                                # If this is a symbol
                                (
                                    symbol_indexes.append((row_index, col_index))
                                    if char != "."
                                    else None
                                ),
                            ]
                        ),
                        reversed(list(enumerate(row))),
                    ),
                    maxlen=0,
                ),
                enumerate(engine),
            ),
            maxlen=0,
        )
        or (
            # Now solve the problem...
            sum(
                # First get a set of all the _indexes_ that are symbol adjacent,
                # then look up those _indexes_ numbers.
                numbers_by_index.get((row, col), 0)
                for row, col in {
                    numberindex_by_position.get(
                        (row + row_offset, col + col_offset), (0, 0)
                    )
                    for (row, col), (row_offset, col_offset) in itertools.product(
                        symbol_indexes, offsets
                    )
                }
            )
        )
    )(
        [
            # Add a '.' to the front to make number parsing easier
            (".") + row
            for row in __import__("pathlib").Path("input/3").read_text().splitlines()
        ],
        __import__("collections"),
        __import__("itertools"),
        [],
        {},
        {},
        [],
        [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ],
    )
)
