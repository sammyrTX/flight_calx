# Dev code for GUI portion of flight calculator

from tkinter import *

# CONSTANTS
#
# Geometry:
# '380x550+850+200'
geometry_settings = '550x550+850+200'
# geometry_settings = '380x550+850+200'

root = Tk()
root.title('Flight Calculator Prototype')
root.geometry(geometry_settings)
root.resizable(False, False)

########################Functions##############################################


def enterNumber(x):
    if entry_box.get() == 'O':
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(x))
    else:
        length_ = len(entry_box.get())
        entry_box.insert(length_, str(x))


def enterOperator(operator_):
    if entry_box.get() != 'O':  # prevents entry starting with an operator
        length_ = len(entry_box.get())
        entry_box.insert(length_, btn_operator[operator_]['text'])


def funcClear():
    entry_box.delete(0, 'end')
    entry_box.insert(0, 'O')


result_ = 0
result_list = []


def funcOperator():
    content_ = entry_box.get()
    print(content_)
    result_ = eval(content_)
    print(result_)
    entry_box.delete(0, 'end')
    entry_box.insert(0, str(result_))

    result_list.append(content_)
    result_list.reverse()
    status_bar.configure(text='History :'+'|'.join(result_list[:5]),
                         font='verdana 10 bold')

def funcDelete():
    length_=len(entry_box.get())
    entry_box.delete(length_ - 1, 'end')

    if length_ == 1:
        entry_box.insert(0, 'O')


########################Entry Box #############################################

entry_box = Entry(font='verdana 14 bold',
                  width=28,  # orginally 22
                  bd=10,
                  justify=RIGHT,
                  bg='#e6e6fa')
entry_box.insert(0, 'O')
entry_box.place(x=20, y=10)

########################Number Buttons#########################################

btn_numbers = []

for _ in range(10):
    btn_numbers.append(Button(width=4,
                              text=str(_),
                              font='times 15 bold',
                              bd=5,
                              command=lambda x=_: enterNumber(x)))

btn_text = 1

for x_ in range(0, 3):
    for y_ in range(0, 3):
        btn_numbers[btn_text].place(x=25+y_*90, y=70+x_*70)
        btn_text += 1

######################Operator Buttons#########################################

btn_operator = []

for _ in range(4):
    btn_operator.append(Button(width=4,
                               font='times 15 bold',
                               bd=5,
                               command=lambda x=_:enterOperator(x)))

btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for _ in range(4):
    btn_operator[_].place(x=290, y=70+_*70)

######################Other Buttons############################################

btn_zero = Button(width=19,
                  text='0',
                  font='times 15 bold',
                  bd=5,
                  command=lambda x=0:enterNumber(x))

btn_clear = Button(width=4,
                   text='C',
                   font='times 15 bold',
                   bd=5,
                   command=funcClear)

btn_dot = Button(width=4,
                 text='.',
                 font='times 15 bold',
                 bd=5,
                 command=lambda x='.':enterNumber(x))

btn_equal = Button(width=4,
                   text='=',
                   font='times 15 bold',
                   bd=5,
                   command=funcOperator)

icon_ = PhotoImage(file='icon/arrow.png')
btn_delete = Button(width=50,
                    height='35',
                    font='times 15 bold',
                    bd=5,
                    command=funcDelete,
                    image=icon_)

status_bar = Label(root,
                   text='History : ',
                   relief=SUNKEN,
                   height=3,
                   anchor=W,
                   font='verdana 11 bold')

btn_zero.place(x=25, y=280)
btn_clear.place(x=25, y=340)
btn_dot.place(x=110, y=340)
btn_equal.place(x=200, y=340)
btn_delete.place(x=290, y=340)
status_bar.pack(side=BOTTOM, fill=X)


######################## mainloop #############################################

root.mainloop()
