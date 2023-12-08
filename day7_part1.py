print(
    sum(
        ((index + 1) * int(info[1]))
        for index, info in (
            lambda collections, hand_count_to_rank, card_to_rank: enumerate(
                sorted(
                    (
                        line.split()
                        for line in __import__("pathlib")
                        .Path("input/7")
                        .read_text()
                        .splitlines()
                    ),
                    key=lambda info: (
                        lambda hand, rank: (
                            (rank, "".join(card_to_rank[card] for card in hand))
                        )
                    )(
                        info[0],
                        hand_count_to_rank[
                            tuple(
                                sorted(
                                    collections.Counter(info[0]).values(), reverse=True
                                )
                            )
                        ],
                    ),
                )
            )
        )(
            __import__("collections"),
            {
                (5,): 7,
                (4, 1): 6,
                (3, 2): 5,
                (3, 1, 1): 4,
                (2, 2, 1): 3,
                (2, 1, 1, 1): 2,
                (1, 1, 1, 1, 1): 1,
            },
            {
                "A": "E",
                "K": "D",
                "Q": "C",
                "J": "B",
                "T": "A",
                "9": "9",
                "8": "8",
                "7": "7",
                "6": "6",
                "5": "5",
                "4": "4",
                "3": "3",
                "2": "2",
            },
        )
    )
)
