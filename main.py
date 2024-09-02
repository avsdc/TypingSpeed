import random
from tkinter import *
import time
import re

counter = 0
var1 = 0
var2 = 0

accurate_wds = 0
user_str = " "
ctime = True
elapsed_secs = 0.0
start_time = 0.0
current_time = 0.0
type_speed = 0


def start_timer():
    global elapsed_secs
    elapsed_secs += 1
    timer_label.config(text=elapsed_secs)
    if ctime == True:
        timer_label.after(1000, start_timer)

def start():
    global start_time
    user_text.focus()
    start_time = time.time()
    start_timer()

def stop_timer():
    global ctime, user_txt_wordcount, var1, var2, user_str
    user_str = user_text.get("1.0", "end-1c")
    user_txt_wordcount = len(user_str.split(" "))
    var1 = round(calc_typing_speed())
    type_speed_label.config(text=f"Typing Speed:{var1}")
    ctime = False
    var2 = calc_accuracy()
    accuracy_label.config(text=f"Accuracy:{var2}")

def calc_typing_speed():
    global var1, user_txt_wordcount, elapsed_secs
    var1 = user_txt_wordcount / (elapsed_secs / 60)
    return var1

def calc_accuracy():
     global var2, original_text_para, user_str, accurate_wds

     original_list = original_text_para.split(" ")
     user_list = user_str.split(" ")
     correct_words = set(original_list) & set(user_list)
     accurate_wds = len(correct_words)
     var2 = round(((accurate_wds / original_txt_wordcount) * 100),2)
     return var2


def reset_all():
    user_text.delete(1.0, END)
    user_text.insert(1.0,"Start typing here.")
    type_speed_label.config(text= f"Typing Speed: {0.0} wpm")
    accuracy_label.config(text= f"Accuracy:{0.0} %")
    timer_label.config(text = "0.0")


# Creating a new window and configurations
window = Tk()
window.title("Typing Speed And Accuracy Calculator")
window.minsize(width=1000, height=800)
window.config(bg='skyblue')

# Creating three frames: two for the two text areas and one for the timer
first_frame = Frame(master=window, width=350, height=600, bg='grey')
first_frame.grid(row=4, column=0, padx=10, pady=5)
second_frame = Frame(master=window, width=600, height=600, bg='grey')
second_frame.grid(row=4, column=1, padx=10, pady=5)
third_frame = Frame(master=window, width=200, height=600, bg='grey')
third_frame.grid(row=4, column=2, padx=10, pady=5)

label_frame = Frame(master=window, width=80, height=20, bg='grey')
label_frame.grid(row=0, column=1)

original_text_frame = Frame(master=first_frame, width=100, height=20, bg='grey')
original_text_frame.grid(row=4, column=0)
user_text_frame = Frame(master=second_frame, width=100, height=20, bg='grey')
user_text_frame.grid(row=4, column=1)

start_btn_frame = Frame(master=window, width=100, height=20, bg='grey')
start_btn_frame.grid(row=7, column=1)
reset_btn_frame = Frame(master=window, width=100, height=20, bg='grey')
reset_btn_frame.grid(row=7, column=0)
# type_speed_frame = Frame(master = window, width = 100, height = 50, bg='grey')
# type_speed_frame.grid(row=100, column=0)

# Label for title
main_label = Label(master=label_frame, text="Typing Speed And Accuracy Calculator",
                   font=("Times New Roman", 20, "bold")).grid(row=0, column=1)
# Label for textbox for original text
original_text_label = Label(master=original_text_frame, text="Original Text", font=("Times New Roman", 15)).grid(row=4,
                                                                                                                 column=0,
                                                                                                                 padx=2,
                                                                                                                 pady=2)
# Label for textbox for user text
user_text_label = Label(master=user_text_frame, text="User Text", font=("Times New Roman", 15)).grid(row=4, column=1,
                                                                                                     padx=2, pady=2)
timer_label = Label(master=third_frame, text="0.0", font=("Times New Roman", 30))
timer_label.grid(row=4, column=2, padx=20, pady=20)
timer_secs_label = Label(master=third_frame, text="Time in seconds", font=("Times New Roman", 20))
timer_secs_label.grid(row=10, column=2)


type_speed_label = Label(master=window, text=f"Typing Speed: {var1} wpm", font=("Times New Roman", 20))
type_speed_label.grid(row=500, column=0, rowspan=2, columnspan=2, padx=2, pady=2)

accuracy_label = Label(master=window, text=f"Accuracy: {var2} %", font=("Times New Roman", 20))
accuracy_label.grid(row=800, column=0, rowspan=2, columnspan=2, padx=5, pady=5)

# Text

text1 = "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."

text2 = "Possibly nothing at all; the overflow of my brain would probably, in a state of freedom, have evaporated in a thousand follies; misfortune is needed to bring to light the treasures of the human intellect. Compression is needed to explode gunpowder. Captivity has brought my mental faculties to a focus; and you are well aware that from the collision of clouds electricity is produced — from electricity, lightning."


text3 = "No one would have believed in the last years of the nineteenth century that this world was being watched keenly and closely by intelligences greater than man’s and yet as mortal as his own; that as men busied themselves about their various concerns they were scrutinised and studied, perhaps almost as narrowly as a man with a microscope might scrutinise the transient creatures that swarm and multiply in a drop of water."

original_text_list = [text1, text2, text3]
original_text_para = random.choice(original_text_list)
original_text_para = original_text_para.strip()


original_text = Text(master=first_frame, height=30, width=50, wrap=WORD)
original_text.grid(row=3, column=0, padx=10, pady=10)
original_text.insert(1.0, original_text_para)
original_txt_wordcount = len(original_text_para.split(" "))


user_text = Text(master=second_frame, height=30, width=50, wrap=WORD)
user_text.grid(row=0, column=1, padx=10, pady=10)
user_text.insert(1.0, "Start typing here.")
user_text_para = user_text.get(1.0, 'end-1c')
user_txt_wordcount = len(user_text_para.split(" "))


# user_text.bind('<Control-Return>', stop_timer())
# Button for start and reset
start_btn = Button(master=start_btn_frame, text="START", width=20, bg='grey', fg='white', command=start)
start_btn.grid(row=7, column=1)

reset_btn = Button(master=reset_btn_frame, text="RESET", width=20, bg='grey', fg='white', command=reset_all)
reset_btn.grid(row=7, column=0)
stop_btn = Button(master=start_btn_frame, text="STOP", width=20, bg='grey', fg='white', command=stop_timer)
stop_btn.grid(row=7, column=2)

window.mainloop()
