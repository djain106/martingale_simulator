import random
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

# Create limbo game with betting to simulate losses/gains using martingale strategy

# Seed random number generator
seed = round(time.time()*1000)
random.seed(seed)

# Set initial inputs and pick number of rounds
loss_odds = 0.505
rounds = int(input("Number of rounds: "))
balance = 600  # Starting Balance Amount
initial_balance = balance
initial_bet = 0.02  # Starting Bet Amount
bet = initial_bet
max_bet = initial_bet
reserve = 0
reserve_limit = 100  # When to Save Money
loss = 0
stop_loss = 80  # Max Loss
round_nums = []
balances = []
last_win = 0

# Set up plot
plt.xlabel('Round')
plt.ylabel('Profit')
plt.title('Profit Plot')

# Conduct bets
for r in range(1, rounds+1):
    multiplier = random.random()
    round_nums.append(r)
    balances.append(balance - initial_balance)
    if balance > initial_balance + reserve_limit:
        reserve += reserve_limit
        balance -= reserve_limit
    if loss > stop_loss:
        print("Loss: ", loss)
        print("Final Round: ", r)
        break
    print("Win, " + str(r - last_win - 1)
          if multiplier > loss_odds else "Lose", round(balance, 2))
    balance -= bet
    if multiplier > loss_odds:
        balance += 2*bet
        bet = initial_bet
        loss = 0
        last_win = r
    else:
        loss += bet
        bet *= 2
    plt.plot(round_nums, balances, 'g' if balance -
             initial_balance > 0 else 'r')
    plt.style.use('dark_background')
    plt.pause(0.25)
    max_bet = max(bet, max_bet)

# Show final output
print("Final Balance:", balance)
print("Reserve:", reserve)
plt.show()
