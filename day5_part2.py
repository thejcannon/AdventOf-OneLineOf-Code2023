print(
    (
        lambda collections, bisect, itertools, seeds_chunk, *map_chunks: (
            lambda seed_ranges, maps, batched, Map: (
                # Parse the seeds chunk
                seed_ranges.extend(
                    sorted(
                        batched(
                            list(map(int, seeds_chunk.split(": ")[1].split())),
                            n=2,
                        )
                    )
                )
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
            or min(
                itertools.starmap(
                    lambda seed_start, seed_length: min(
                        location_start
                        for soil_start, soil_length in maps["seed"][
                            seed_start, seed_length
                        ]
                        for fertilizer_start, fertilizer_length in maps["soil"][
                            soil_start, soil_length
                        ]
                        for water_start, water_length in maps["fertilizer"][
                            fertilizer_start, fertilizer_length
                        ]
                        for light_start, light_length in maps["water"][
                            water_start, water_length
                        ]
                        for temperature_start, temperature_length in maps["light"][
                            light_start, light_length
                        ]
                        for humidity_start, humidity_length in maps["temperature"][
                            temperature_start, temperature_length
                        ]
                        for location_start, location_length in maps["humidity"][
                            humidity_start, humidity_length
                        ]
                    ),
                    seed_ranges,
                )
            )
        )(
            [],
            {},
            lambda iterable, n: (
                iterable[i : i + n] for i in range(0, len(iterable), n)
            ),
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
                    "_get_index": lambda self, key: (
                        (
                            lambda bisected_index: bisected_index
                            if bisected_index == 0
                            or (
                                bisected_index < len(self._lookup)
                                and self._lookup[bisected_index][0] == key
                            )
                            else bisected_index - 1
                        )(bisect.bisect_left(self._lookup, key, key=lambda x: x[0]))
                    ),
                    # Lookup the range, and return the relevant mapping mapped ranges.
                    # Use a helper method where instead of "key", we shove key in a list,
                    # so we can mutate it as we iterate. E.g. `key = x` -> `key_cont[0] = x`.
                    "_getitem_helper": lambda self, key_cont: (
                        result[0]
                        for result in itertools.takewhile(
                            lambda result: not result[1],
                            # The return of this lambda is ((<mapped_start>, <mapped_length>), <whether to terminate>)
                            (
                                (
                                    lambda start, overall_length: (
                                        (
                                            lambda value: (
                                                value,
                                                # Assign the new key
                                                key_cont.__setitem__(
                                                    0,
                                                    (
                                                        start + value[1],
                                                        overall_length - value[1],
                                                    ),
                                                )
                                                # Terminate (and throw the result away) if the length is 0, e.g. we're done
                                                or value[1] == 0,
                                            )
                                        )(
                                            (
                                                lambda src_start, dest_start, length: (
                                                    # If the target range start is in this mapped range,
                                                    # we add a range starting at the mapped value (dest_start + (start - src_start))
                                                    # whose length is the shorter of the remaining length of this mapped range,
                                                    # or the remainder of the mapped range.
                                                    (
                                                        dest_start
                                                        + (start - src_start),
                                                        min(
                                                            overall_length,
                                                            (
                                                                length
                                                                - (start - src_start)
                                                            ),
                                                        ),
                                                    )
                                                    if src_start
                                                    <= start
                                                    < (src_start + length)
                                                    # Otherwise, if the target range starts "too low",
                                                    # map values 1:1 whose length is the shorter of the remaining length of this mapped range,
                                                    # or the distance to the next mapped range.
                                                    else (
                                                        start,
                                                        min(
                                                            overall_length,
                                                            src_start - start,
                                                        ),
                                                    )
                                                    if start < src_start
                                                    # We've gone above the map, the rest is a 1:1 mapped range
                                                    else (start, overall_length)
                                                )
                                            )(*self._lookup[self._get_index(start)])
                                        )
                                    )
                                )(*key_cont[0])
                                for _ in itertools.repeat(None)
                            ),
                        )
                    ),
                    "__getitem__": lambda self, key: self._getitem_helper([key]),
                },
            ),
        )
    )(
        __import__("collections"),
        __import__("bisect"),
        __import__("itertools"),
        *__import__("pathlib").Path("input/5").read_text().split("\n\n"),
    )
)
