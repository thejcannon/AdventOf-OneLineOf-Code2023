print(
    (
        lambda collections, itertools, math, network, current_nodes, instructions, _, *node_lines: (
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
            # Find the starting positions
            or (current_nodes.extend(node for node in network if node.endswith("A")))
            # Walk each individually, turns out they cycle, so from the distances we'll just find the
            # least common multiple
            or math.lcm(
                *[
                    1
                    + sum(
                        1
                        for _ in itertools.takewhile(
                            lambda node: not node.endswith("Z"),
                            (
                                # Go left or right in the network
                                current_nodes.__setitem__(
                                    index,
                                    network[current_nodes[index]][
                                        0 if instruction == "L" else 1
                                    ],
                                )
                                # "yield" the next node
                                or current_nodes[index]
                                for instructions in itertools.repeat(instructions)
                                for instruction in instructions
                            ),
                        )
                    )
                    for index, node in enumerate(current_nodes)
                ]
            )
        )
    )(
        __import__("collections"),
        __import__("itertools"),
        __import__("math"),
        {},
        [],
        *__import__("pathlib").Path("input/8").read_text().splitlines()
    )
)
