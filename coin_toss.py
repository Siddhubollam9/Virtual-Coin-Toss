import random
import tkinter as tk
from tkinter import messagebox

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses():
    try:
        num_flips = int(input("Enter the number of times you want to flip the coin: "))
        if num_flips <= 0:
            print("Please enter a valid number greater than 0.")
            return

        heads_count, tails_count = 0, 0

        for _ in range(num_flips):
            result = coin_toss()
            print(result)
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1

        total = heads_count + tails_count
        heads_percent = (heads_count / total) * 100
        tails_percent = (tails_count / total) * 100

        print(f"\nResults: ")
        print(f"Heads: {heads_count} ({heads_percent:.2f}%)")
        print(f"Tails: {tails_count} ({tails_percent:.2f}%)")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def start_program():
    while True:
        multiple_tosses()
        repeat = input("\nDo you want to toss again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thanks for playing!")
            break

# Bonus: GUI with Tkinter
def gui_coin_toss():
    def toss():
        result = coin_toss()
        result_label.config(text=f"Result: {result}")
        if result == "Heads":
            heads_count.set(heads_count.get() + 1)
        else:
            tails_count.set(tails_count.get() + 1)
        
        update_stats()

    def update_stats():
        total = heads_count.get() + tails_count.get()
        if total == 0:
            return
        heads_percent = (heads_count.get() / total) * 100
        tails_percent = (tails_count.get() / total) * 100
        stats_label.config(text=f"Heads: {heads_count.get()} ({heads_percent:.2f}%) | "
                                f"Tails: {tails_count.get()} ({tails_percent:.2f}%)")

    def reset():
        heads_count.set(0)
        tails_count.set(0)
        result_label.config(text="Result: ")
        update_stats()

    root = tk.Tk()
    root.title("Virtual Coin Toss")

    heads_count = tk.IntVar(value=0)
    tails_count = tk.IntVar(value=0)

    toss_button = tk.Button(root, text="Toss Coin", command=toss, font=("Arial", 14))
    toss_button.pack(pady=10)

    result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
    result_label.pack(pady=10)

    stats_label = tk.Label(root, text="Heads: 0 (0%) | Tails: 0 (0%)", font=("Arial", 12))
    stats_label.pack(pady=10)

    reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 12))
    reset_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    choice = input("Do you want to play in GUI mode? (yes/no): ").strip().lower()
    if choice == "yes":
        gui_coin_toss()
    else:
        start_program()
