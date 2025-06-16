import os
import sys
import time
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import pygame

pygame.mixer.init()

console = Console()
balance = 1000000000000
receipts_log = []

def play_sound(file):
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing sound: {e}")


def loading_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    with Progress(
        SpinnerColumn(spinner_name="bouncingBar"),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        task = progress.add_task("[bold blue]Booting up Black Card Bank™ OS...", total=None)
        time.sleep(2)
        progress.update(task, description="[cyan]Loading financial data...")
        time.sleep(2)
        progress.update(task, description="[green]Injecting cash into RAM...")
        time.sleep(1.5)
        progress.update(task, description="[magenta]Launching Quantum Banking Protocol...")
        time.sleep(2.5)

    print("\n🎉 Welcome to BLACK CARD BANK™ v1.0\n")

def exit_animation():
    with Progress(
        SpinnerColumn(spinner_name="earth"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
        console=console
    ) as progress:
        task = progress.add_task("[bold cyan]Saving your session...", total=None)
        time.sleep(2.5)
        progress.update(task, description="[bold magenta]Logging you out securely...")
        time.sleep(2)

        if receipts_log:
            with open("transaction_receipts.txt", "w", encoding="utf-8") as file:
                file.writelines(receipts_log)

        progress.update(task, description="[bold green]Finalizing exit protocol...")
        time.sleep(1.5)

    console.print("\n[bold red]✅ Logout successful. Thank you for using Black Card Bank™.[/bold red]")
    console.print("[dim]Your transaction receipt has been generated: 'transaction_receipts.txt'[/dim]")
    sys.exit()


def authentication():
    for i in range(3):
        try:
            passkey = int(input("Please enter your 4-digit PIN: "))
        except ValueError:
            print("Invalid input. Numbers only, bruh.")
            continue

        if passkey == 6969:
            with Progress(
                SpinnerColumn(spinner_name="dots"),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                task = progress.add_task("\U0001F510 Verifying credentials...", total=None)
                time.sleep(2)

            console.print("✅ [bold green]Authentication successful. Welcome to your account.[/bold green]")
            return True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"❌ Incorrect PIN. {2 - i} tries left. Get it together bro 😤")
            time.sleep(1)

    print("🚨 Too many failed attempts. Account temporarily locked.")
    return False


def show_balance():
    os.system('cls' if os.name == 'nt' else 'clear')
    with Progress(
        SpinnerColumn(spinner_name="dots2"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("\U0001F4CA Fetching account balance...", total=None)
        time.sleep(3)

    print(f"💰 Your balance is: ₹{balance:,}")
    print("Thank u sir, have a nice day.")

def write_receipt(transaction_type, amount):
    log = (
        "\n====== BLACK CARD BANK™ RECEIPT ======\n"
        f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Transaction: {transaction_type}\n"
        f"Amount: ₹{amount:,}\n"
        f"Balance: ₹{balance:,}\n"
        "========================================\n"
    )
    receipts_log.append(log)

def deposit(amount):
    os.system('cls' if os.name == 'nt' else 'clear')
    global balance
    if amount < 0:
        print("You tryna rob the bank in reverse? 💀")
        return

    balance += amount
    write_receipt("Deposit", amount)
    play_sound("deposit.mp3")

    with Progress(
        SpinnerColumn(spinner_name="bouncingBall"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("\U0001F4B8 Crediting your account...", total=None)
        time.sleep(4.3)

    print(f"✅ ₹{amount:,} has been added to your account.")
    if input("Check balance? (yes/no): ").lower() == "yes":
        show_balance()

def withdraw(amount):
    os.system('cls' if os.name == 'nt' else 'clear')
    global balance
    if amount < 0:
        print("That's not how money works, fam 😒")
        return
    if amount > balance:
        print(f"🚫 You broke! Balance: ₹{balance:,}")
        return

    balance -= amount
    write_receipt("Withdraw", amount)
    play_sound("withdraw.mp3")

    with Progress(
        SpinnerColumn(spinner_name="bouncingBall"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("\U0001F4B8 Debiting your account...", total=None)
        time.sleep(1.5)

    print(f"✅ ₹{amount:,} has been withdrawn.")
    if input("Check balance? (yes/no): ").lower() == "yes":
        show_balance()

def start(choice):
    match choice:
        case "s":
            show_balance()
        case "d":
            try:
                amount = int(input("Enter amount to deposit: "))
                deposit(amount)
            except:
                print("Numbers only, champ 🧠")
        case "w":
            try:
                amount = int(input("Enter amount to withdraw: "))
                withdraw(amount)
            except:
                print("Numbers only, champ 🧠")
        case "q":
            exit_animation()
        case _:
            print("❌ Invalid choice. No freestyles allowed 💀")


loading_screen()

if authentication():
    while True:
        console.print("\n[bold yellow]Main Menu:[/bold yellow]")
        console.print("[green]s[/green] - Show Balance")
        console.print("[blue]d[/blue] - Deposit Money")
        console.print("[red]w[/red] - Withdraw Money")
        console.print("[magenta]q[/magenta] - Quit\n")

        choice = input("What do you wanna do? ").lower()
        start(choice)

        again = input("\nAnother transaction? (yes/no): ").lower()
        if again != "yes":
            exit_animation()


