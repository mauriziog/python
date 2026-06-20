import random

def genera_numeri_casuali():
    # Opzione 1: 10 numeri casuali che possono contenere duplicati
    numeri_con_duplicati = [random.randint(1, 100) for _ in range(10)]
    
    # Opzione 2: 10 numeri casuali unici (senza duplicati)
    numeri_unici = random.sample(range(1, 101), 10)
    
    print("10 Numeri casuali (possono contenere duplicati):")
    print(numeri_con_duplicati)
    print("\n10 Numeri casuali unici (senza duplicati):")
    print(numeri_unici)

if __name__ == "__main__":
    genera_numeri_casuali()
