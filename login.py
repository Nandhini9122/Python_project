from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get() == 'Nandhini' and passwordEntry.get() == '9122':
        messagebox.showinfo('Success','Welcome Nandhini')
        window.destroy()
        import ems

    else:
        messagebox.showerror('Error','Please enter correct credentials')

window=Tk()

window.geometry('1280x700+0+0')
window.title('Login System of Employee Management System')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

backgroundLabel = Label(window, image=backgroundImage)
backgroundLabel.place(x=0, y=0)

loginFrame = Frame(window)
loginFrame.place(x=500, y=150)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Username:', compound=LEFT, font=('times new roman', 17, 'bold'), bg='white')

usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=('times new roman', 17), bd=3, fg='blue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password:', compound=LEFT, font=('times new roman', 17, 'bold'), bg='white')

passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('times new roman', 17), bd=3, fg='blue')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 12, 'bold'), width=15, fg='white', bg='cornflowerblue', activebackground='cornflowerblue', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)


window.mainloop()