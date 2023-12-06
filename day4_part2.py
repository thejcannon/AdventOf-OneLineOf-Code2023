print(
    (
        lambda collections, copies_counts, lines: sum(
            map(
                lambda card_info: (
                    lambda winners, ours: (
                        lambda num_winners, this_card_count: collections.deque(
                            # For as many winners as we have, increment that many cards at the head
                            # of the card count by our own count.
                            # E.g. If there's 20 of our card, and we won 2, increment the next 2
                            # positions by 20.
                            (
                                copies_counts.__setitem__(
                                    offset, copies_counts[offset] + this_card_count
                                )
                                for offset in range(num_winners)
                            ),
                            maxlen=0,
                        )
                        # This iteration should yield the count of this card in the final calculation.
                        or this_card_count
                    )(
                        # Calculate the winners, and pop our card count off the front of the list
                        len(
                            set(map(int, winners.split())) & set(map(int, ours.split()))
                        ),
                        copies_counts.pop(0),
                    )
                )(*(card_info.split(": ")[1].split(" | "))),
                lines,
            )
        )
    )(
        __import__("collections"),
        # We build a list of card counts, which all start at 1
        *(lambda lines: ([1] * len(lines), lines))(
            __import__("pathlib").Path("input/4").read_text().splitlines()
        )
    )
)
