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

# --- Part Two ---
#
# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.
#
# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.
#
# Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.
#
# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.
#
# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.
#
# Consider the same engine schematic again:
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
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.
#
# What is the sum of all of the gear ratios in your engine schematic?
#

print(
    (
        lambda engine, collections, itertools, gear_indexes, numbers_by_index, numberindex_by_position, digit_container, offsets:
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
                                # If this is a gear
                                (
                                    gear_indexes.append((row_index, col_index))
                                    if char != "."
                                    else None
                                )
                                if char == "*"
                                else None,
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
                (
                    numbers_by_index[(nums[0][0], nums[0][1])]
                    * numbers_by_index[(nums[1][0], nums[1][1])]
                )
                for nums in [
                    list(
                        {
                            numberindex_by_position[
                                (row + row_offset, col + col_offset)
                            ]
                            for row_offset, col_offset in offsets
                            if (row + row_offset, col + col_offset)
                            in numberindex_by_position
                        }
                    )
                    for row, col in gear_indexes
                ]
                if len(nums) == 2
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
