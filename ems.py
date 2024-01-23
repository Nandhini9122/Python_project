from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

#functionality part

def iexit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = employeeTable.get_children()
    newlist = []
    for index in indexing:
        content = employeeTable.item(index)
        datalist = content['values']
        newlist.append(datalist)


    table = pandas.DataFrame(newlist, columns=['Id','Name','Mobile','Email','Address','Gender','D.0.B','Role','Salary','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success', 'Data is saved successfully')

def toplevel_data(title, button_text, command):
    global idEntry, nameEntry, mobileEntry, emailEntry, addressEntry, genderEntry, dobEntry, roleEntry, salaryEntry, screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id:', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=12, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=12)

    nameLabel = Label(screen, text='Name:', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=12, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=12)

    mobileLabel = Label(screen, text='Mobile No:', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=30, pady=12, sticky=W)
    mobileEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, padx=10, pady=12)

    emailLabel = Label(screen, text='Email:', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=12, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10, pady=12)

    addressLabel = Label(screen, text='Address:', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=12, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10, pady=12)

    genderLabel = Label(screen, text='Gender:', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=12, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=10, pady=12)

    dobLabel = Label(screen, text='D.O.B:', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=12, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=12)

    roleLabel = Label(screen, text='Role:', font=('times new roman', 20, 'bold'))
    roleLabel.grid(row=7, column=0, padx=30, pady=12, sticky=W)
    roleEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    roleEntry.grid(row=7, column=1, padx=10, pady=12)

    salaryLabel = Label(screen, text='Salary:', font=('times new roman', 20, 'bold'))
    salaryLabel.grid(row=8, column=0, padx=30, pady=12, sticky=W)
    salaryEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    salaryEntry.grid(row=8, column=1, padx=10, pady=12)

    employee_button = ttk.Button(screen, text=button_text, command=command)
    employee_button.grid(row=9, columnspan=2, pady=12)

    if title == 'Update Employee':
        indexing = employeeTable.focus()

        content = employeeTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        mobileEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])
        roleEntry.insert(0, listdata[7])
        salaryEntry.insert(0, listdata[8])


def update_data():
    query = 'update employee set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,role=%s,salary=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(),
                                dobEntry.get(), roleEntry.get(), salaryEntry.get(), date, currenttime, idEntry.get()))
    con.commit()
    messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully', parent=screen)
    screen.destroy()
    show_employee()


def show_employee():
    query = 'select * from employee'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetched_data:
        employeeTable.insert('', END, values=data)

def delete_employee():
    indexing=employeeTable.focus()
    print(indexing)
    content = employeeTable.item(indexing)
    content_id = content['values'][0]
    query = 'delete from employee where id=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')
    query = 'select * from employee'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetched_data:
        employeeTable.insert('', END, values=data)


def search_data():
    query = 'select * from employee where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s or role=%s or salary=%s'
    mycursor.execute(query,(idEntry.get(), nameEntry.get(), emailEntry.get(), mobileEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(), roleEntry.get(), salaryEntry.get()))
    employeeTable.delete(*employeeTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        employeeTable.insert('', END, values=data)


def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or mobileEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='' or roleEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error', 'All fields required', parent=screen)

    else:
        try:
            query = 'insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(),
            genderEntry.get(), dobEntry.get(), roleEntry.get(), salaryEntry.get(), date, currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?', parent=screen)
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                mobileEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
                roleEntry.delete(0, END)
                salaryEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error', 'Id cannot be repeated', parent=screen)
            return

        query = 'select * from employee'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        employeeTable.delete(*employeeTable.get_children())
        for data in fetched_data:
            employeeTable.insert('', END, values=data)

def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host=hostnameEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
            return

        try:
            query = 'create database employeemanagementsystem'
            mycursor.execute(query)
            query = 'use employeemanagementsystem'
            mycursor.execute(query)
            query = ('create table employee(id int not null primary key, name varchar(30), mobile varchar(10), email varchar(50),'
                     'address varchar(100), gender varchar(20), dob varchar(20),role varchar(50), salary varchar(10), date varchar(50), time varchar(50))')
            mycursor.execute(query)
        except:
            query='use employeemanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectWindow)
        connectWindow.destroy()
        addEmployeeButton.config(state=NORMAL)
        searchEmployeeButton.config(state=NORMAL)
        updateEmployeeButton.config(state=NORMAL)
        showEmployeeButton.config(state=NORMAL)
        exportEmployeeButton.config(state=NORMAL)
        deleteEmployeeButton.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel = Label(connectWindow, text='Host Name:', font=('arial', 20, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)

    hostnameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostnameEntry.grid(row=0, column=1, padx=40, pady=20)

    usernameLabel = Label(connectWindow, text='User Name:', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password:', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)


count=0
text=''
def slider():
    global text,count
    if count == len(s):
        count = 0
        text = ''
    text=text+s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(200,slider)

def clock():
    global date,currenttime
    date = time.strftime('%d-%m-%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)

#GUI part
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1190x680+0+0')
root.resizable(0, 0)
root.title('Employee Management System')

datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()
s = 'Employee Management System'  #s[count]=E when count is 0,t is 1,...
sliderLabel = Label(root, font=('arial', 23, 'italic bold'), width=32)
sliderLabel.place(x=300, y=0)
slider()

connectButton=ttk.Button(root, text='Connect to Database', command=connect_database)
connectButton.place(x=970,y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file='employee 1.png')
logo_Label = Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)

addEmployeeButton = ttk.Button(leftFrame, text='Add Employee', width=25, state=DISABLED, command=lambda: toplevel_data('Add Employee', 'Add', add_data))
addEmployeeButton.grid(row=1, column=0, pady=20)

searchEmployeeButton = ttk.Button(leftFrame, text='Search Employee', width=25, state=DISABLED, command=lambda: toplevel_data('Search Employee', 'Search', search_data))
searchEmployeeButton.grid(row=2, column=0, pady=20)

deleteEmployeeButton = ttk.Button(leftFrame, text='Delete Employee', width=25, state=DISABLED, command=delete_employee)
deleteEmployeeButton.grid(row=3, column=0, pady=20)

updateEmployeeButton = ttk.Button(leftFrame, text='Update Employee', width=25, state=DISABLED, command=lambda: toplevel_data('Update Employee', 'Update', update_data))
updateEmployeeButton.grid(row=4, column=0, pady=20)

showEmployeeButton = ttk.Button(leftFrame, text='Show Employee', width=25, state=DISABLED, command=show_employee)
showEmployeeButton.grid(row=5, column=0, pady=20)

exportEmployeeButton = ttk.Button(leftFrame, text='Export data', width=25, state=DISABLED, command=export_data)
exportEmployeeButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=iexit)
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

employeeTable = ttk.Treeview(rightFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender',
                                  'D.O.B', 'Role', 'Salary', 'Added Date', 'Added Time'),
                             xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
scrollBarX.config(command=employeeTable.xview)
scrollBarY.config(command=employeeTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

employeeTable.pack(fill=BOTH, expand=1)

employeeTable.heading('Id', text='Id')
employeeTable.heading('Name', text='Name')
employeeTable.heading('Mobile No', text='Mobile No')
employeeTable.heading('Email', text='Email')
employeeTable.heading('Address', text='Address')
employeeTable.heading('Gender', text='Gender')
employeeTable.heading('D.O.B', text='D.O.B')
employeeTable.heading('Role', text='Role')
employeeTable.heading('Salary', text='Salary')
employeeTable.heading('Added Date', text='Added Date')
employeeTable.heading('Added Time', text='Added Time')

employeeTable.column('Id', width=50, anchor=CENTER)
employeeTable.column('Name', width=300, anchor=CENTER)
employeeTable.column('Email', width=350, anchor=CENTER)
employeeTable.column('Mobile No', width=200, anchor=CENTER)
employeeTable.column('Address', width=300, anchor=CENTER)
employeeTable.column('Gender', width=120, anchor=CENTER)
employeeTable.column('D.O.B', width=120, anchor=CENTER)
employeeTable.column('Role', width=370, anchor=CENTER)
employeeTable.column('Salary', width=200, anchor=CENTER)
employeeTable.column('Added Date', width=160, anchor=CENTER)
employeeTable.column('Added Time', width=160, anchor=CENTER)

style = ttk.Style()

style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), foreground='dark blue', background='light blue', fieldbackground='light blue')
style.configure('Treeview.Heading', font=('arial', 14,'bold'))
employeeTable.config(show='headings')

root.mainloop()