def blackjack_check(hand):
    total = hand_total(hand)
    if total[0] == 21:
        return "yes"
    else:
        return "no"
    
player_hand = [11, 10]
blackjack = blackjack_check(player_hand)
print(blackjack)