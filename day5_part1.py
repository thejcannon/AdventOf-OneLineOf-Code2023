print(
    (
        lambda collections, bisect, seeds_chunk, *map_chunks: (
            lambda seeds, maps, Map: (
                # Parse the seeds chunk
                seeds.extend(map(int, seeds_chunk.split(": ")[1].split()))
            )
            or (
                # Then parse the chunks
                collections.deque(
                    map(
                        lambda chunk: (
                            lambda map_header, *map_lines: (
                                lambda srcname, destname: (
                                    maps.__setitem__(srcname, Map(map_lines))
                                )
                            )(*map_header.split(" ")[0].split("-to-"))
                        )(*chunk.splitlines()),
                        map_chunks,
                    ),
                    maxlen=0,
                )
            )
            or (
                min(
                    map(
                        lambda seed: (
                            maps["humidity"][
                                maps["temperature"][
                                    maps["light"][
                                        maps["water"][
                                            maps["fertilizer"][
                                                maps["soil"][maps["seed"][seed]]
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ),
                        seeds,
                    )
                )
            )
        )(
            [],
            {},
            # Make a new class, because `__getitem__` syntax is too nice not to use.
            # We store the map triplets sorted based on source start, so we can efficiently look it up
            # using a binary search later.
            type(
                "Map",
                (),
                {
                    "__init__": lambda self, map_lines: setattr(
                        self,
                        "_lookup",
                        sorted(
                            (int(src_start), int(dest_start), int(length))
                            for dest_start, src_start, length in (
                                line.split() for line in map_lines
                            )
                        ),
                    ),
                    # Lookup the number and return the relevant mapped number
                    "__getitem__": lambda self, src_num: (
                        lambda bisected_index: (
                            lambda src_start, dest_start, length: (
                                (dest_start + (src_num - src_start))
                                if (src_start <= src_num < (src_start + length))
                                else src_num
                            )
                        )(
                            *(
                                self._lookup[bisected_index]
                                if bisected_index < len(self._lookup)
                                and self._lookup[bisected_index][0] == src_num
                                else self._lookup[bisected_index - 1]
                            )
                        )
                    )(bisect.bisect_left(self._lookup, src_num, key=lambda x: x[0])),
                },
            ),
        )
    )(
        __import__("collections"),
        __import__("bisect"),
        *__import__("pathlib").Path("input/5").read_text().split("\n\n")
    )
)
