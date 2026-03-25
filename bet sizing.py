import numpy as np

# Parameters
p = 0.52            # win probability
n_bets = 100       # bets per simulation
n_sims = 1000       # number of simulations
n_money = 100       # starting money
bet_size = 1        # size of bet
results = []
results_utility = []


# for i in range(n_sims): 
#     money = n_money
#     for j in range (n_bets):
#         if money >= bet_size: 
#             if np.random.rand() < p:
#                 money += bet_size
#             else: 
#                 money -= bet_size
#     results.append(money)
#     results_utility.append(np.sqrt(money))

# print (np.mean(results))
# print (np.mean(results_utility))

highest_avg_payoff = [0,0]
highest_avg_utility = [0,0] 

for test_bet_size in range (n_money + 1):
    payoffs = []
    utilities = []
    for i in range(n_sims):
        acc_bets = 0   
        money = n_money
        for j in range (n_bets):
            if money >= test_bet_size: 
                if np.random.rand() < p:
                    money += test_bet_size
                else: 
                    money -= test_bet_size
        payoffs.append(money)
        utility = np.sqrt(money)
        utilities.append(utility)
    average_payoff = np.mean(payoffs)
    average_utility = np.mean(utilities)
    if average_payoff >= highest_avg_payoff[0]:
        highest_avg_payoff = [average_payoff, test_bet_size]
    if average_utility >= highest_avg_utility[0]:
        highest_avg_utility = [average_utility, test_bet_size]
print (f"the highest average payoff of {highest_avg_payoff[0]} occurs with a bet size of {highest_avg_payoff[1]}")
print (f"the highest average utility of {highest_avg_utility[0]} occurs with a bet size of {highest_avg_utility[1]}")


    
highest_avg_payoff = [0,0]
highest_avg_utility = [0,0] 
average_payoffs = []
average_utilities = []

for test_bet_percentage in range (101):    
    payoffs = []
    utilities = []
    for i in range(n_sims):
        acc_bets = 0   
        money = n_money
        for j in range (n_bets):
            if np.random.rand() < p:
                money += test_bet_percentage/100 * money
            else: 
                money -= test_bet_percentage/100 * money
        payoffs.append(money)
        utility = np.sqrt(money)
        utilities.append(utility)
    average_payoff = np.mean(payoffs)
    average_payoffs.append([test_bet_percentage, average_payoff])
    average_utility = np.mean(utilities)
    average_utilities.append([test_bet_percentage, average_utility])
    if average_payoff >= highest_avg_payoff[0]:
        highest_avg_payoff = [average_payoff, test_bet_percentage]
    if average_utility >= highest_avg_utility[0]:
        highest_avg_utility = [average_utility, test_bet_percentage]
print (f"the highest average payoff of {highest_avg_payoff[0]} occurs with a bet percentage of {highest_avg_payoff[1]}")
print (f"the highest average utility of {highest_avg_utility[0]} occurs with a bet percentage of {highest_avg_utility[1]}")





