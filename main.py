import random
import time

# Stratégia lista
strategiak = [
    "Trendkövető",
    "Sideway (oldalazó)",
    "Kitörés figyelő",
    "Scalp",
    "Swing",
    "Arbitrázs szimuláció"
]

def valassz_strategiat():
    return random.choice(strategiak)

def futtat_robot():
    profit = 0.0
    for lepes in range(10):  # 10 szimulált lépés
        strategia = valassz_strategiat()
        eredmeny = random.uniform(-0.5, 1.5)  # random profit/veszteség %
        profit += eredmeny
        print(f"{lepes+1}. lépés → {strategia} stratégia → {eredmeny:.2f}% változás")
        time.sleep(0.5)
    print(f"\nÖsszesített profit: {profit:.2f}%")

if __name__ == "__main__":
    futtat_robot()