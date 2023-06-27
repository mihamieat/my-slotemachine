# -*- coding: utf-8 -*-
"""Main execution of the program."""
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(columns, lines, bet, values):
    """Check if the player has won the game."""
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """Return the slot machine spin."""
    all_symbols = []
    for symbol, sym_count in symbols.items():
        for _ in range(sym_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine_spin(columns):
    """Print a slot machine spin."""
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def enter_number(input_prompt):
    """Enter a number function."""
    while True:
        number = input(input_prompt)
        try:
            number = int(number)
        except ValueError:
            print("Please enter a number.")
            continue
        if number < 0:
            print("Please enter a positive number.")
            continue
    return number


def deposit():
    """Collect the user money input."""
    amount = enter_number("How much money do you want to deposit? $")
    return amount


def get_bet():
    """Collect the user bet input."""
    amount = enter_number(
        f"How much do you want to bet on each line (${MIN_BET} to ${MAX_BET})? $"
    )
    if amount < MIN_BET or amount > MAX_BET:
        print(f"Please enter a number between {MIN_BET} and {MAX_BET}.")
        return get_bet()
    return amount


def get_number_of_lines():
    """Return the number of lines between 1 and 3."""
    lines = enter_number(f"How many lines do you want to play with? (1 to {MAX_LINES})")
    if lines < 1 or lines > MAX_LINES:
        print(f"Please enter a number between 1 and {MAX_LINES}.")
        return get_number_of_lines()
    return lines


def check_balance(input_deposit, bet):
    """Check if the user has enough money."""
    balance = input_deposit - bet
    if balance < 0:
        print("You don't have enough money to bet.")
        return False
    return True


def spin(balance):
    """Spin action returns remaining money."""
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    """Main execution of the program."""
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()
