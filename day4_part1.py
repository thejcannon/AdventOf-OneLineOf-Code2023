print(
    sum(
        map(
            lambda card_info: (
                lambda winners, ours: (
                    lambda num_winners: (2 ** (num_winners - 1)) if num_winners else 0
                )(len(set(map(int, winners.split())) & set(map(int, ours.split()))))
            )(*(card_info.split(": ")[1].split(" | "))),
            __import__("pathlib").Path("input/4").read_text().splitlines(),
        )
    )
)
