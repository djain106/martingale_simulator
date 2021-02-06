import random
import time
import matplotlib.pyplot as plt

# Create limbo game with betting to simulate losses/gains using martingale strategy
seed = round(time.time()*1000)
random.seed(seed)

loss_odds = 0.505
rounds = int(input("Number of rounds: "))
balance = 600
initial_balance = balance
initial_bet = 0.02
bet = initial_bet
max_bet = initial_bet
reserve = 0
reserve_limit = 100
loss = 0
stop_loss = 80
round_nums = []
balances = []
last_win = 0

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
          if multiplier > loss_odds else "Lose")
    balance -= bet
    if multiplier > loss_odds:
        balance += 2*bet
        bet = initial_bet
        loss = 0
        last_win = r
    else:
        loss += bet
        bet *= 2
    max_bet = max(bet, max_bet)

print("Final Balance:", balance)
print("Reserve:", reserve)
plt.plot(round_nums, balances)
plt.xlabel('Round')
plt.ylabel('Profit')
plt.title('Profit Plot')
plt.show()
