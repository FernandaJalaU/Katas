def winner(deckSteve, deckJosh):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    steve_score = 0
    josh_score = 0

    while deckSteve and deckJosh:
        steve_card = deckSteve.pop(0)
        josh_card = deckJosh.pop(0)

        if card_values[steve_card] > card_values[josh_card]:
            steve_score += 1
        elif card_values[steve_card] < card_values[josh_card]:
            josh_score += 1

    if steve_score > josh_score:
        return f"Steve wins {steve_score} to {josh_score}"
    elif steve_score < josh_score:
        return f"Josh wins {josh_score} to {steve_score}"
    else:
        return "Tie"

# Example usage:
deckSteve = ['2', '3', '4', '5', '6']
deckJosh = ['3', '4', '5', '6', '7']
print(winner(deckSteve, deckJosh))
