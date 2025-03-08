#!/usr/bin/env python3

import signal
import time
import sys
import os
import tkinter as tk
from tkinter import messagebox

# Function to show a pop-up alert
def show_popup(signal_name):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showwarning("Process Interrupted", f"{signal_name} received! Process stopped.")
    root.destroy()

# Signal handler function
def handle_signal(signum, frame):
    signals = {
        signal.SIGINT: "SIGINT (Ctrl+C)",
        signal.SIGTERM: "SIGTERM (Kill -15)",
        signal.SIGHUP: "SIGHUP (Logout)",
        signal.SIGTSTP: "SIGTSTP (Ctrl+Z)"
    }
    signal_name = signals.get(signum, f"Unknown Signal ({signum})")

    print(f"\n{signal_name} received! Showing pop-up alert...")

    # Show a pop-up alert
    show_popup(signal_name)

    sys.exit(0)  # Exit gracefully

# Register signal handlers
signal.signal(signal.SIGINT, handle_signal)   # Handle Ctrl+C
signal.signal(signal.SIGTERM, handle_signal)  # Handle ⁠ kill -15 ⁠
signal.signal(signal.SIGHUP, handle_signal)   # Handle logout
signal.signal(signal.SIGTSTP, handle_signal)  # Handle Ctrl+Z

# Running process simulation
print(f"Process running in the background with PID: {os.getpid()}")
print("Try stopping it with ⁠ Ctrl+C ⁠, ⁠ kill -15 <PID> ⁠, or ⁠ Ctrl+Z ⁠.")

while True:
    try:
        time.sleep(1)  # Simulate a long-running process
    except Exception as e:
        print(f"Error: {e}")
