# _______________________________POMODORO TIMER_____________________________ #
# Allows users to start a timer that goes through a pomodoro cycle.
# 25 minutes of work and a five-minute break.
# After four sessions, the user receives a 25-minute timer for a long-break.

# Import necessary modules
from tkinter import *
import math

# Constant variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# _______________________________TIMER RESET_____________________________ #
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_top.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    reps = 0


# _______________________________TIMER START_____________________________ #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        label_top.config(text="Work", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        label_top.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        label_top.config(text="Break", fg=RED)


# _______________________________TIMER COUNTDOWN_____________________________ #
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark.config(text=marks)


# _______________________________UI SETUP_____________________________ #
# Create Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create and Set Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create and Set Labels
label_top = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
label_top.grid(column=1, row=0)
checkmark.grid(column=1, row=3)

# Create and Set Buttons
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)


window.mainloop()
