import random

def  dice_roller():
    diceA = {
            1:("┌──────────┐",
               "|          |",
               "|     ●    |",
               "|          |",          
               "└──────────┘"),
            2:("┌──────────┐",
               "| ●        |",
               "|          |",
               "|        ● |",          
               "└──────────┘"),
            3:("┌──────────┐",
               "| ●        |",
               "|     ●    |",
               "|        ● |",          
               "└──────────┘"),
            4:("┌──────────┐",
               "| ●      ● |",
               "|          |",
               "| ●      ● |",          
               "└──────────┘"),
            5:("┌──────────┐",
               "| ●      ● |",
               "|     ●    |",
               "| ●      ● |",          
               "└──────────┘"),
            6:("┌──────────┐",
               "| ●      ● |",
               "| ●      ● |",
               "| ●      ● |",          
               "└──────────┘")  
    }
    dice = []
    total = 0
    num_dice = 4
    for die in range(num_dice):
        dice.append(random.randint(1, 6))
    #for die in range(num_dice):
    #   for line in diceA.get(dice[die]):
    #      print(line)
    for line in range(5):
        for die in dice:
            print(diceA.get(die)[line],end= "")
        print()

    for die in dice:
        total += die
    print(f" Total : {total}")
    return total

def win_lose(bet,total):
   
   if total == 7:
      return bet * 10
   
   elif total == 10:
      return bet * 3
   elif total == 4 or total == 24:
      if total == 4:
          return bet * 20 + 4
      else:
         return bet * 20 + 24
   elif total == 14:
      return bet * 2.5
   return 0
def main():
    balance = 100.00
    print("Welcome to Dice roll Game!!!!!")
    print("You have 4 dice and the total number of 4 dice that you got is sum is 10 , 14 ,7 or 4 you win other than that you lose")
    while balance > 0:
       print(f"Your current balance is {balance} Birr")
       bet = input("Enter betting amount : ")
       if not bet.isdigit():
          print("Please enter valid number") 
          continue
       bet = float(bet)
       if bet > balance:
           print("Insufficien fund!!")
           continue
       if bet <= 0:
         print("Bet must be greater than 0")
         continue
       balance -= bet
       
       n = dice_roller()
       won = win_lose(bet,n)
       if won > 0:
          print(f"You won {won} birr")
       else:
          print("You Lose!!")
       balance += won
       p_l = input("Do you want try again(Y|N) : ").upper()
       if not p_l == "Y":
         break
    print("Thank you for playing")
if __name__ == "__main__":
   main()