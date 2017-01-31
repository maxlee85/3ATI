import tkinter
from tkinter import *




def snooze(secs):
    """
    Snoozes for the given number of seconds. During the snooze, a progress
    dialog is launched notifying the
    """

    def decrement_label():
        global remaining, prompt
        remaining -= 1
        prompt.set('Snoozing %d sec(s)' % remaining)
        label1.update_idletasks()
        if not remaining:
            print("end ... ")
            root.destroy()

    global remaining
    prompt.set("hello")
    label1 = tkinter.Label(root, textvariable=prompt, width=30)
    label1.pack()

    remaining = secs
    for i in range(1, secs + 1):
        root.after(i * 1000, decrement_label)


# just init some vars
remaining = 0
secs = 0
root = tkinter.Tk()
prompt = StringVar()

snooze(5)
root.mainloop()