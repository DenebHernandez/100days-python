import os
import math
import tkinter as tk

main_folder = os.getcwd()
cwd = f"{main_folder}\B-Intermediate\day28"
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_counter():
    global reps
    reps += 1

    if reps == 8:
        counter(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        counter(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=GREEN)
    else:
        counter(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):

    count_minute = math.floor(count / 60)
    if count_minute < 10:
        count_minute = f"0{count_minute}"

    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        window.after(1000, counter, count-1)
    else:
        start_counter()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(
    text="Timer",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 50)
)
title_label.grid(column=1, row=0)

canvas = tk.Canvas(
    width=200,
    height=224,
    bg=YELLOW,
    highlightthickness=0
)
image = tk.PhotoImage(file=f"{cwd}\\tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(
    107, 130,
    text="00:00",
    fill=YELLOW,
    font=(FONT_NAME, 30, "bold")
)
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_counter)

reset_button = tk.Button(text="Reset")

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(
    text="✓",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 20)
)
check_marks.grid(column=1, row=3)

window.mainloop()
