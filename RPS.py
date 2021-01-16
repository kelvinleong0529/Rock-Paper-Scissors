import random as rn
import tkinter as tk

def check(user,bot):
    winv = int(win["text"])
    matchv = int(match["text"])
    losev = int(lose["text"])
    drawv = int(draw["text"])
    match["text"] = f'{ matchv + 1}'
    if user-bot == 1 or ( user==1 and bot ==3):
        win["text"]  = f'{ winv + 1}'
        info1["text"]= "You Win!"
    elif user-bot == 0:
        draw["text"] = f'{drawv + 1}'
        info1["text"]= "Draw Game!"
    else:
        lose["text"] = f"{losev + 1 }"
        info1["text"]= "You Lose!"

def chck(x):
    switcher = {1:"Opponent choose Rock!",
                2:"Opponent choose Paper!",
                3:"Opponent choose Scissors!"}
    return switcher.get(x)
        

def rock():
    x=rn.randint(1,3)
    check(1,x)
    info2["text"]=chck(x)
def paper():
    x=rn.randint(1,3)
    check(2,x)
    info2["text"]=chck(x)
def scissors():
    x=rn.randint(1,3)
    check(3,x)
    info2["text"]=chck(x)
    

window = tk.Tk()
frame_1 = tk.Frame(master=window)
frame_1.pack()
window.title("Rock Paper and Scissors")
frame_1.columnconfigure([0,1],minsize = 450)
frame_1.rowconfigure(0, minsize = 100)
display = tk.Label(master=frame_1,text="Please choose your option!",relief=tk.SUNKEN)
display.pack()
frame_2 = tk.Frame(master=window)
frame_2.columnconfigure([0,1,2],minsize = 150)
frame_2.rowconfigure(0, minsize = 100)
frame_2.pack(fill=tk.Y)
rock_btn = tk.Button(master=frame_2,text="ROCK",command=rock)
rock_btn.grid(row=0,column=0)
paper_btn = tk.Button(master=frame_2,text="PAPER",command=paper)
paper_btn.grid(row=0,column=1)
scissors_btn = tk.Button(master=frame_2,text="SCISSORS",command=scissors)
scissors_btn.grid(row=0,column=2)
frame_4 = tk.Frame(master=window)
frame_4.pack()
frame_4.columnconfigure(0,minsize = 350)
frame_4.rowconfigure([0,1], minsize = 10)
info1 = tk.Label(master=frame_4,text = ' ')
info1.pack()
info2 = tk.Label(master=frame_4,text = ' ')
info2.pack()
frame_3 = tk.Frame(master=window)
frame_3.pack(fill=tk.Y)
label = ["Matches:","Win:","Lose:","Draw:"]
for index,text in enumerate(label):
    t = tk.Label(master=frame_3,text = text)
    t.grid(row=index,column=0,sticky='e')
match = tk.Label(master=frame_3,text='0')
win = tk.Label(master=frame_3,text='0')
lose = tk.Label(master=frame_3,text='0')
draw = tk.Label(master=frame_3,text='0')
match.grid(row=0,column=1,sticky='w')
win.grid(row=1,column=1,sticky='w')
lose.grid(row=2,column=1,sticky='w')
draw.grid(row=3,column=1,sticky='w')
window.mainloop()