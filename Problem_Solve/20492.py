winner_price = int(input())
first = winner_price - winner_price * 0.22
second = winner_price - ((winner_price * 0.2) * 0.22)
print(int(first), int(second))