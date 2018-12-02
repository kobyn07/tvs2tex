# -*- encording: utf8-*-
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('tvs2tex')
        self.master.geometry('1000x500')
        self.input = ''' bb'''
        # caption の入力
        captitle = tk.Label(self, text='表タイトル')
        captitle.grid(row=0, column=0, sticky=tk.E)
        capbox = tk.Entry(self, width=30)
        capbox.grid(row=0, column=1, padx=10, pady=10)

        # label の入力
        labtitle = tk.Label(self, text='ラベル')
        labtitle.grid(row=1, column=0, sticky=tk.E)
        labbox = tk.Entry(self, width=30)
        labbox.grid(row=1, column=1)

        # 表の入力
        intitle = tk.Label(self, text='入力')
        intitle.grid(row=2, column=0, padx=10, pady=10)
        inbox = tk.Text(self, width=50, wrap=tk.NONE)
        inbox.grid(row=3, column=0, padx=10)

        # 表の出力
        outtitle = tk.Label(self, text='出力')
        outtitle.grid(row=2, column=2, padx=30, pady=10)
        outbox = tk.Text(self, width=50, wrap=tk.NONE)
        outbox.grid(row=3, column=2, padx=10)

        def clickedOnButton():
            getTable()
            createTable()
            print(self.input)

        def getTable():
            self.input = inbox.get('1.0', 'end-1c')

        def createTable():
            outbox.insert('1.0', self.input)

        # 変換ボタン
        chbutton = tk.Button(self, text='変換', padx=20, pady=20, font=(10), command=clickedOnButton)
        chbutton.grid(row=3, column=1)



if __name__=='__main__':
    f = Application()
    f.pack()
    f.mainloop()
