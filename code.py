import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('700x700')
root.title('Dice roller')
root.config(bg='#FAFAEB')

blank0 = tkinter.Label(root,text="")
blank0.pack()

head1 = tkinter.Label(root,text="Hello Player",fg="#9A9ACD",bg='#FFFFFF',
                   font = "Times,30,Bold")
head1.pack()
Dice=['1.png','2.png','3.png','4.png','5.png','6.png']

old_pic = Image.open("dice.png")
resized = old_pic.resize((500,500), Image.Resampling.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)
Image1 = tkinter.Label(root, image=new_pic,bg='#FAFAEB')
Image1.image = new_pic
Image1.pack( expand=True)
def roll_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    Image1.configure(image=DiceImage,bg='#FAFAEB')
    Image1.image = DiceImage

button = tkinter.Button(root, text='Roll the Dice',font='Arial,Bold',bg='cornsilk4', fg='#FAFAEB', command=roll_dice,
                        width=20, height=2)
button.pack(pady=(0,30),expand=True)

root.mainloop()
