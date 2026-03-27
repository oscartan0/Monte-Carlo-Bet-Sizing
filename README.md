# Optimal Bet Sizing via Monte Carlo Simulation

## Overview:
This project explores the long-run optimal bet size under uncertainty through the use of a Monte Carlo simulation. The goal is to understand how to maximise expected return while managing the associated risk of large drawdowns.

## Approach:
- within a bet, a player pays $x for a p chance of winning $2x
- when the probability is above 
- simulate repeated bets to show a long-run streak

## Key Concepts:
- Expected Value
- Log-Utility / Sqrt-Utility
- Kelly optimal bet sizing
- Risk/Return Tradeoff
- Variance / Drawdowns (measure of risk)\

## Implementation:
- Language: Python
- Libraries: Numpy, Matplotlib
- Simulations: 

## Results:
- Due to positive expected value bets, aggressive bet sizing can be good for maximising expected returns but leads to large drawdowns
- betting a percentage of bankroll rather than a constant size leads to both higher payoff and higher utility (under both metrics)
- Maximising log-utility within the simulation led to near idential optimization to kelly criteria
- The optimal sizing is very sensitive to changes in win probability
- the number of bets required to converge to the kelly criteria is fairly small (only requiring about 5 bets)
- In order to maximise payoff of a small number of bets, one should bet a high percentage of their bankroll, as number of bets increase this should deteriorate rapidly from a pure payoff maximisation perspective
- if judging based on expected payoff, this will overstate the optimal bet size vs judging based on sqrt utility, which in turn will overstate optimal bet percentage compared to log utility.

## How to Run:
### 1. clone repository
### 2. install required libraries:
- pip install numpy
- pip install matplotlib
### 3. Run Jupyter Notebooks in order
1. Interactive notebook: test outcomes of given probability, number of bets, bet_size (% and abs), and number of simulations
2. Betting Absolute Size vs Percentage: test optimal bet size under given conditions as a dollar bet and as a percentage bet: highlighting optimality of betting %, due to higher payoff and utility
3. Effect of Win_Probability on optimal bet size: demonstrating the increased betting amount on a higher win probability, optimal bet percentage aligns with kelly criteria.
4. Effect of Number of Bets on optimal bet size: showcasing 

## Future Improvements
- Incorporating Transactions costs (both fixed and percentage)
- Graph of Bankroll Paths
- Create a "multi-asset" universe with more than one bet option

## Author
Oscar Tan