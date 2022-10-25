import math
import tkinter

# Setting constants
PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


#reset mechanism
def reset_timer():
    window.after_cancel(timer)
    label_1.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_marks.config(text="")
    global REPS
    REPS = 0


#Timer start
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if REPS % 2 != 0:
        count_down(work_sec)
        label_1.config(text="Work")
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        label_1.config(text="Break",fg=RED)
    else:
        count_down(short_break_sec)
        label_1.config(text="Break",fg=PINK)


# Countdown Mechanism
def count_down(count):
    global REPS
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer=window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()
        mark = ""
        work_sessions = math.floor((REPS/2))
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

# UI Setup
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


label_1=tkinter.Label(text="Timer",font=(FONT_NAME,24,"bold"),fg=GREEN,highlightthickness=0,bg=YELLOW)
label_1.grid(column=2,row=0)


button_1=tkinter.Button(text="Start",command=start_timer)
button_1.grid(column=1,row=3)

button_2=tkinter.Button(text="Reset",command=reset_timer)
button_2.grid(column=3,row=3)

check_marks=tkinter.Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=2,row=4)


window.mainloop()
