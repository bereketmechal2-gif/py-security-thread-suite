# 🎲 4-Dice Match Betting Game

A command-line Python game featuring dynamic ASCII art rendering, modular gameplay logic, and robust user input validation.

## 🚀 Features
- **Side-by-Side ASCII Art**: Custom-rendered dice graphics built from string arrays.
- **Defensive Programming**: Validates financial transactions, preventing negative bets, non-numeric strings, and overdrafts.
- **Modular Design**: Separated concerns between the terminal rendering engine and win/loss state evaluations.

## 🕹️ Game Rules
You roll 4 dice. If the sum of your dice equals target combinations, you win multipliers:
- **Sum of 4**: 20x Payout pluse 4
- **Sum of 24**: 20x payout pluse 24
- **Sum of 7**: 10x Payout
- **Sum of 10**: 3x Payout
- **Sum of 14**: 2.5x Payout

## 🛠️ How To Run
Ensure you have Python 3 installed. Run the following command in your terminal:
```bash
python main.py
```
