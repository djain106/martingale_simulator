import os
import random
import time

# Create limbo game with betting to simulate losses/gains using martingale strategy
seed = round(time.time()*1000)
random.seed(seed)

odds = 0.505
rounds = int(input("Number of rounds: "))
balance = 100
initial_bet = 0.02
bet = initial_bet
max_bet = initial_bet
reserve = 0

for r in range(rounds):
    multiplier = random.random()
    if balance > 200:
        reserve += 100
        balance -= 100
    if balance < bet:
        print("Round: ", r)
        break
    balance -= bet
    if multiplier > odds:
        balance += 2*bet
        bet = initial_bet
    else:
        bet *= 2
    max_bet = max(bet, max_bet)
    print(("Win" if multiplier > odds else "Lose") +
          ": ", round(multiplier, 2), bet)

print(round(balance, 2))
print("Reserve: ", reserve)
