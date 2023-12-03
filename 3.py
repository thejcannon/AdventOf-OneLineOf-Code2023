# --- Day 3: Gear Ratios ---
#
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.
#
# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
#
# "Aaah!"
#
# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
#
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
#
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
#
# Here is an example engine schematic:
#
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
#
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?


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
