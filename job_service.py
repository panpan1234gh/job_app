from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_maneger import *
from validation import *

employee_list = read_from_file("employee.dat")


def load_data(employee_list):
    employee_list = read_from_file("employee.dat")
    for row in table.get_children():
        table.delete(row)

    for employee in employee_list:
        table.insert("", END, values=employee)


# clear btn
def reset_form():
    id.set(len(employee_list) + 1)
    full_name.set("")
    job.set("")
    work_place.set("")
    start_time.set("")
    retire.set("")
    load_data(employee_list)


def save_btn():
    employee = (id.get(), full_name.get(), job.get(), work_place.get(), start_time.get(), retire.get())
    errors = employee_validator(employee)

    if errors:
        msg.showerror("errors", "\n".join(errors))

    else:
        msg.showinfo("saved", "person saved")
        employee_list.append(employee)
        write_to_file("employee.dat", employee_list)
        reset_form()


def edit_btn():
    pass


def remove_btn():
    pass




def table_select(x):
    selected_employee = table.item(table.focus())["values"]
    if selected_employee:
        id.set(selected_employee[0])
        full_name.set(selected_employee[1])
        job.set(selected_employee[2])
        work_place.set(selected_employee[3])
        start_time.set(selected_employee[4])
        retire.set(selected_employee[5])


window = Tk()
window.title("employee info")
window.geometry("610x500")

# id
Label(window, text="ID").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

# full name
Label(window, text="Full Name").place(x=20, y=60)
full_name = StringVar()
Entry(window, textvariable=full_name).place(x=80, y=60)

# job
Label(window, text="Job").place(x=20, y=100)
job = StringVar()
Entry(window, textvariable=job).place(x=80, y=100)

# workplace
Label(window, text="Workplace").place(x=20, y=140)
work_place = StringVar()
Entry(window, textvariable=work_place).place(x=80, y=140)

# start time
Label(window, text="Start Time").place(x=20, y=180)
start_time = StringVar()
Entry(window, textvariable=start_time).place(x=80, y=180)

# retirement
Label(window, text="retirment").place(x=20, y=220)
retire = StringVar()
Entry(window, textvariable=retire).place(x=80, y=220)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="ID")
table.heading(2, text="Fullname")
table.heading(3, text="Job")
table.heading(4, text="Workplace")
table.heading(5, text="Start time")
table.heading(6, text="Retirement")
# table.heading(7, text="job service")


table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)

table.place(x=270, y=20)

Button(window, text="Save", width=6, command=save_btn).place(x=20, y=290)
Button(window, text="Edit", width=6, command=edit_btn).place(x=90, y=290)
Button(window, text="Remove", width=6, command=remove_btn).place(x=160, y=290)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=260, width=190)

reset_form()

window.mainloop()
