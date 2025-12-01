import tkinter as tk
from tkinter import messagebox, ttk

# -----------------------------
# YOUR ORIGINAL FUNCTIONS (logic same)
# -----------------------------
def show_balance(balance):
    messagebox.showinfo("Balance", f"Your balance is ${balance:.2f}")

def deposit(amount):
    if amount < 0:
        messagebox.showerror("Error", "That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance, amount):
    if amount > balance:
        messagebox.showerror("Error", "Insufficient Funds")
        return 0
    elif amount < 0:
        messagebox.showerror("Error", "Amount must be greater than 0")
        return 0
    else:
        return amount


# -----------------------------
# ADVANCED TKINTER UI
# -----------------------------
root = tk.Tk()
root.title("🏦 Banking App")
root.geometry("500x420")
root.configure(bg="#f5f5f5")

# Make window centered
root.eval('tk::PlaceWindow . center')

balance = 0.0


# -----------------------------
# Styling
# -----------------------------
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 13, "bold"),
                padding=10)

style.configure("TLabel",
                font=("Arial", 14))

title_label = tk.Label(root, text="🏦 Banking Management System",
                       font=("Arial", 22, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=20)


# -----------------------------
# Balance Display
# -----------------------------
balance_var = tk.StringVar()
balance_var.set(f"Current Balance: ${balance:.2f}")

balance_label = tk.Label(root, textvariable=balance_var,
                         font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#1a73e8")
balance_label.pack(pady=10)


# -----------------------------
# Amount Entry Box
# -----------------------------
amount_label = tk.Label(root, text="Enter Amount:", font=("Arial", 14), bg="#f5f5f5")
amount_label.pack(pady=5)

amount_entry = ttk.Entry(root, font=("Arial", 14), width=20)
amount_entry.pack(pady=5)


# -----------------------------
# Button Actions
# -----------------------------
def do_deposit():
    global balance
    try:
        amt = float(amount_entry.get())
        balance += deposit(amt)
        balance_var.set(f"Current Balance: ${balance:.2f}")
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


def do_withdraw():
    global balance
    try:
        amt = float(amount_entry.get())
        balance -= withdraw(balance, amt)
        balance_var.set(f"Current Balance: ${balance:.2f}")
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


def do_show_balance():
    show_balance(balance)


# -----------------------------
# Buttons (Advanced Layout)
# -----------------------------
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=20)

btn1 = ttk.Button(button_frame, text="Show Balance", command=do_show_balance)
btn1.grid(row=0, column=0, padx=10, pady=10)

btn2 = ttk.Button(button_frame, text="Deposit", command=do_deposit)
btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = ttk.Button(button_frame, text="Withdraw", command=do_withdraw)
btn3.grid(row=0, column=2, padx=10, pady=10)


# Exit button (at bottom)
exit_btn = ttk.Button(root, text="Exit Program", command=root.destroy)
exit_btn.pack(pady=20)


# Run App
root.mainloop()
