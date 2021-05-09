from tkinter import *
import pyperclip
import string
import random
import re


#pass multiple commands to button_main
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


#gui for generating password (2nd window)


def generate_password():
    global bg_pic
    global var1
    global var2
    global var3
    global l

    def low(): 
        entry.delete(0, END) 

        # Get the length of passowrd 
        length = password_length.get()
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789!@#$%^&*()"
        password = ''
        # if strength selected is low 
        
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 0: 
            while True: 
                password = password + random.choice(lower)
                if length == 1:
                    break
                length -= 1

        if var1.get() == 0 and var2.get() == 1 and var3.get() == 0: 
            while True: 
                password = password + random.choice(upper)
                if length == 1:
                    break
                length -= 1

        if var1.get() == 0 and var2.get() == 0 and var3.get() == 1: 
            while True: 
                password = password + random.choice(digits)
                if length == 1:
                    break
                length -= 1

        if var1.get() == 1 and var2.get() == 1 and var3.get() == 0: 
            while True: 
                password = password + random.choice(lower)
                if length == 1:
                    break
                length -= 1
                password = password + random.choice(upper)
                if length == 1:
                    break
                length -= 1

        if var1.get() == 1 and var2.get() == 0 and var3.get() == 1: 
            while True: 
                password = password + random.choice(upper)
                if length == 1:
                    break
                length -= 1
                password = password + random.choice(digits)
                if length == 1:
                    break
                length -= 1

        if var1.get() == 0 and var2.get() == 1 and var3.get() == 1: 
            while True: 
                password = password + random.choice(lower)
                if length == 1:
                    break
                length -= 1
                password = password + random.choice(digits)
                if length == 1:
                    break
                length -= 1

        if var1.get() == 1 and var2.get() == 1 and var3.get() == 1: 
            while True: 
                password = password + random.choice(upper)
                if length == 1:
                    break
                length -= 1
                password = password + random.choice(lower)
                if length == 1:
                    break
                length -= 1
                password = password + random.choice(digits)
                if length == 1:
                    break
                length -= 1
            

        p = list(password)
        random.shuffle(p)
        password = ''
        for i in p:
            password += i
         
        return password

    def generate(): 
        password1 = low() 
        entry.insert(10, password1) 



    top = Toplevel()
    top.geometry("500x500")
    top.title("Generating a secure password")
    top.resizable(0,0)
    top.configure(background = '#000000') #272525
    bg_pic = PhotoImage(file = "main_final.png")
    label1 = Label(top, image = bg_pic, bg = '#000000') 
    label1.place(x = 135, y = 250)
    label = Label(top, text = 'Set Password Length: ',bg = '#000000',
                font = ('Times', 20), fg = "#149414",
                pady = 5)
    label.place(x = 150, y = 150)

    # button to show generate password option
    button = Button(top, text = 'Generate Password', bg = '#000000',
                font = ('Times', 10), fg = "#149414",
                pady = 5, bd = 5, activebackground = '#149414', command = generate)

    def copy1(): 
        random_password = entry.get() 
        pyperclip.copy(random_password)

    copy_password = Button(top, text = 'Copy To Clipboard', command = copy1, bg = '#000000',
                font = ('Times', 10), fg = "#149414",
                pady = 5, bd = 5, activebackground = '#149414')

    #button.place(x = 525, y = 125)  

    password_length = IntVar() 

    pass_length = Spinbox(top, textvariable = password_length, from_=8, to=32, bg = '#000000', activebackground = '#000000',
                            fg = "#149414")

    entry = Entry(top, textvariable = '',bg = '#000000',
                font = ('Times', 20), fg = "#149414", bd = 5,
                highlightcolor = '#000000', relief = GROOVE)
    

    #entry.place(x = 625, y = 125)  
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    uppercase_check = Checkbutton(top, text='Uppercase Letters',variable=var1, onvalue=1, offvalue=0,# command=print_selection,
                                bg = '#000000', font = 'Times', fg = "#149414",
                                activebackground = '#000000', activeforeground = '#000000', selectcolor = "#272525")

    lowercase_check = Checkbutton(top, text='Lowercase Letters',variable=var2, onvalue=1, offvalue=0,# command=print_selection,
                                bg = '#000000', font = 'Times', fg = "#149414",
                                activebackground = '#000000', activeforeground = '#000000', selectcolor = "#272525")

    symbols_check = Checkbutton(top, text='Symbols',variable=var3, onvalue=1, offvalue=0, #command=print_selection,
                                bg = '#000000', font = 'Times', fg = "#149414",
                                activebackground = '#000000', activeforeground = '#000000', selectcolor = "#272525")    

    uppercase_check.pack()
    lowercase_check.pack()
    symbols_check.pack()
    label.pack()
    pass_length.pack()
    button.pack()
    entry.pack()
    copy_password.pack()



# gui for user to enter their password and we check strength
# and give appropiate suggestion



root = Tk()
root.title('Checking your password')
root.resizable(0,0)
root.geometry("485x400")

bg_pic_main = PhotoImage(file = "first_screen_copy.png")
label_pic = Label(root, image = bg_pic_main)
label_pic.place(x = 0, y = 0)
label_main = Label(root, text = 'Enter your password: ', bg = '#0d0d0d',
            font = ('Times', 20), fg = "#f2f2f2",
            pady = 5)
label_main.place(x = 150, y = 150)


entry_main = Entry(root,show = '*', bg = '#0d0d0d',
                font = ('Times', 20), fg = "#f2f2f2", bd = 5,
                highlightcolor = '#000000', relief = GROOVE)



#====== Strength Check =======


def checkPassword():
    strength = ['Password can not be Blank', 'Very Weak, Try our Password Generator instead!', 'Weak,  Try our Password Generator instead!',
                'Medium', 'Strong', 'Very Strong']
    score = 1
    password = entry_main.get()

    if len(password) < 1:
        return strength[0]

    if len(password) < 4:
        return strength[1]

    if len(password) >= 8:
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    if re.search(".", password):
        score += 1

    passwordStrength.set(strength[score])

passwordStrength = StringVar()
check_main = Button(root, text = 'Start Checking...', bg = '#0d0d0d',
                font = ('Times', 10), fg = "#f2f2f2",
                pady = 5, bd = 5, command = checkPassword)

l = Label(root, bg='white', width=34, textvariable = passwordStrength, font = ('Times', 10))

button_main = Button(root, text = 'Try our Password Generator!', bg = '#0d0d0d',
                font = ('Times', 10), fg = "#f2f2f2",
                pady = 5, bd = 5, command = combine_funcs(generate_password, root.iconify))

label_main.pack()
entry_main.pack()
check_main.pack()
l.pack()
button_main.pack()

mainloop()