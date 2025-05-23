from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
G = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def action2():
    global G
    G = 0
    window.after_cancel(timer)
    label1.config(text="Timer", fg=GREEN)
    label2.config(text="")
    canvas.itemconfig(text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def action1():
    global G
    G += 1
    if G % 8 == 0:
        label1.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif G % 2 == 0:
        label1.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        label1.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        if G < 16:
            for _ in range(G // 2):
                mark += "✓"
            action1()
            label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Widget Examples")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50, bg=YELLOW)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.place(x=60, y=50)

label1 = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
label1.place(x=100, y=0)

label2 = Label(font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
label2.place(x=70, y=280)

button1 = Button(text="Start", command=action1)
button1.place(x=40, y=280)

button2 = Button(text="Reset", command=action2)
button2.place(x=250, y=280)

window.mainloop()
