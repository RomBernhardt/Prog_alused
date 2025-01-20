class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialize Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Return a string representation of the card."""
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize Hand."""
        self.cards = []

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suit.
        """
        if len(self.cards) >= 5:
            return False
        if card.value not in self.values or card.suit not in self.suits:
            return False
        for c in self.cards:
            if c.value == card.value and c.suit == card.suit:
                return False
        return True

    def add_card(self, card: Card):
        """Add a card to hand."""
        if self.can_add_card(card):
            self.cards.append(card)

    def can_remove_card(self, card: Card):
        """Check if a card can be removed from hand."""
        return card in self.cards

    def remove_card(self, card: Card):
        """Remove a card from hand."""
        if self.can_remove_card(card):
            self.cards.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.cards

    def is_straight(self):
        """Determine if the hand is a straight."""
        values = [self.values.index(card.value) for card in self.cards]
        values.sort()
        for i in range(1, len(values)):
            if values[i] != values[i-1] + 1:
                return False
        return True

    def is_flush(self):
        """Determine if the hand is a flush."""
        suits = [card.suit for card in self.cards]
        return len(set(suits)) == 1

    def is_straight_flush(self):
        """Determine if the hand is a straight flush."""
        return self.is_straight() and self.is_flush()

    def is_full_house(self):
        """Determine if the hand is a full house."""
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in set(values)}
        return sorted(value_counts.values()) == [2, 3]

    def is_four_of_a_kind(self):
        """Determine if there are four cards of the same value."""
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in set(values)}
        return 4 in value_counts.values()

    def is_three_of_a_kind(self):
        """Determine if there are three cards of the same value."""
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in set(values)}
        return 3 in value_counts.values()

    def is_pair(self):
        """Determine if there are two cards of the same value."""
        values = [card.value for card in self.cards]
        value_counts = {value: values.count(value) for value in set(values)}
        return 2 in value_counts.values()

    def get_hand_type(self):
        """Return a string representation of the hand."""
        if len(self.cards) < 5:
            return None
        if self.is_straight_flush():
            return "straight flush"
        if self.is_flush():
            return "flush"
        if self.is_straight():
            return "straight"
        if self.is_full_house():
            return "full house"
        if self.is_four_of_a_kind():
            return "four of a kind"
        if self.is_three_of_a_kind():
            return "three of a kind"
        if self.is_pair():
            return "pair"
        return "high card"

    def __repr__(self):
        """Return a string representation of the hand."""
        hand_type = self.get_hand_type()
        if hand_type:
            return f"I got a {hand_type} with cards: {', '.join(str(card) for card in self.cards)}"
        return f"I'm holding {', '.join(str(card) for card in self.cards)}"


# Test cases as in the example
if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "straight"

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "flush"

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "four of a kind"
