print(
    (
        lambda collections, itertools, network, node_container, instructions, _, *node_lines: (
            # Parse the network
            collections.deque(
                (
                    itertools.starmap(
                        lambda node, neighbors: (
                            network.__setitem__(
                                node, tuple(neighbors[1:-1].split(", "))
                            )
                        ),
                        (node_line.split(" = ") for node_line in node_lines),
                    )
                ),
                maxlen=0,
            )
            # Walk!
            or 1
            + sum(
                1
                for _ in itertools.takewhile(
                    lambda node: node != "ZZZ",
                    (
                        # Go left or right in the network
                        node_container.__setitem__(
                            0,
                            network[node_container[0]][0 if instruction == "L" else 1],
                        )
                        # "yield" the next node
                        or node_container[0]
                        for instructions in itertools.repeat(instructions)
                        for instruction in instructions
                    ),
                )
            )
        )
    )(
        __import__("collections"),
        __import__("itertools"),
        {},
        ["AAA"],
        *__import__("pathlib").Path("input/8").read_text().splitlines()
    )
)
