from tkinter import *

root = Tk()
x = IntVar()


def test():
    global x
    x.set(x.get() + 1)
    print(x)

label_1 = Label(root, text=x.get(), textvariable = x)
button_1 = Button(root, text='Click', command=test)
button_1.grid(row=0, column=0)
label_1.grid(row=0, column=1)

root.mainloop()



def snooze(secs):
    """
    Snoozes for the given number of seconds. During the snooze, a progress
    dialog is launched notifying the
    """

    def decrement_label():
        global remaining, prompt
        remaining -= 1
        prompt.set('%d sec(s)' % remaining)

    global remaining
    label1 = tkinter.Label(w, textvariable=prompt, width=5).grid(row=3, column=2, padx=1, pady=1)

    remaining = secs
    for i in range(1, secs + 1):
        w.after(i * 1000, decrement_label)

# just init some vars
remaining = 0
secs = 0
prompt = StringVar()