# -*- encording: utf8-*-
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('tvs2tex')
        self.master.geometry('1000x500')
        # caption の入力
        captitle = tk.Label(self, text=u'表タイトル')
        captitle.grid(row=0, column=0)
        capbox = tk.Text(self, width=30, height=1)
        capbox.grid(row=0, column=1, padx=10, pady=30)



if __name__=='__main__':
    f = Application()
    f.pack()
    f.mainloop()
