from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0
timer = None
interval=1000


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    label_timer.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text=f'00:00')
    label_checkmark.config(text='')
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        label_timer.config(text='Work', fg=GREEN)
        count_down(work_sec)
    elif reps == 1 or reps == 3 or reps == 5:
        label_timer.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    elif reps == 7:
        label_timer.config(text='Break', fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(interval, count_down, count - 1)
    elif count == 0 and reps < 8:
        check_mark = ''
        work_sessions = math.floor(reps / 2 + 1)
        for rep in range(work_sessions):
            check_mark += '✔'
        label_checkmark.config(text=check_mark)
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", font=(FONT_NAME, 32, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
label_timer.grid(column=1, row=0)

tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)
button_start = Button(text="start", width=5, highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

label_checkmark = Label(fg=GREEN, font=(FONT_NAME, 12, 'normal'), bg=YELLOW, highlightthickness=0)
label_checkmark.grid(column=1, row=3)

button_restart = Button(text="restart", width=5, highlightthickness=0, command=reset)
button_restart.grid(column=2, row=2)

window.mainloop()
