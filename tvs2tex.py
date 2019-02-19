# -*- encording: utf8-*-
import tkinter as tk
import pyperclip


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('tvs2tex')
        self.master.geometry('1000x520')
        self.input = ''
        self.caption = ''
        self.label = ''
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

        # クリップボードにコピーするかどうかのチェックボックス
        clipBln = tk.BooleanVar()
        clipBln.set(True)
        clipcheck = tk.Checkbutton(
            self, variable=clipBln, text='クリップボードにコピーする')
        clipcheck.grid(row=4, sticky=tk.W)

        # コンマをドルマークに置換するかどうかのチェックボックス
        conmaBln = tk.BooleanVar()
        conmaBln.set(True)
        conmaCheck = tk.Checkbutton(
            self, variable=conmaBln, text='コンマをドルマークに変換する')
        conmaCheck.grid(row=5, sticky=tk.W)

        # タブ区切りの出力にするかどうかのチェックボックス
        tabBlm = tk.BooleanVar()
        tabBlm.set(False)
        tabCheck = tk.Checkbutton(
            self, variable=tabBlm, text='出力時インデントをタブ区切りにする')
        tabCheck.grid(row=6, sticky=tk.W)

        # 変換ボタンの挙動

        def clickedOnButton():
            initbox(outbox)
            getTable()
            createTable()
            output()

        def initbox(name):
            name.delete('1.0', 'end')

        def initEntry(name):
            name.delete('0', 'end')

        def getTable():
            self.input = inbox.get('1.0', 'end-1c')
            self.caption = capbox.get()
            self.label = labbox.get()

        def countCenter():
            """
            入力された値から列数を返す
            """
            c = 0
            row = ''
            for w in self.input:
                row += w
                if '\n' in row:
                    break
            c = row.count('&')
            c += 1
            return c

        def createTable():
            """
            入力したタブ区切りのテキストから、LaTex のテーブルを生成
            """
            # 文末に改行文字があれば削除する
            while True:
                if '\n' in self.input[-2:]:
                    self.input = self.input.rstrip('\n')
                else:
                    break

            # コンマをドルマークに変換するかどうかの判定
            if conmaBln.get():
                self.input = self.input.replace(',', '$')

            self.input = self.input.replace('\t', ' & ')
            centerCount = countCenter()
            centerNumber = 'c' * centerCount
            self.input = self.input.replace('\n', ' \\\\\n\t\t\t')
            self.input = self.input + ' \\\\'
            self.input = '''\\begin{table}[h]
\t\\begin{center}
\t\t\\caption{caption}
\t\t\\begin{tabular}{centerNumber}
\t\t\t\\hline
\t\t\t{core}
\t\t\t\\hline
\t\t\\end{tabular}
\t\t\\label{label}
\t\\end{center}
\\end{table}'''.format(core=self.input, table='{table}', center='{center}',
                       tabular='{tabular}', centerNumber='{'+centerNumber+'}',
                       caption='{'+self.caption+'}', label='{tab:'+self.label+'}')

            if not tabBlm.get():
                self.input = self.input.replace('\t', '    ')

        def output():
            outbox.insert('1.0', self.input)
            if clipBln.get():
                pyperclip.copy(self.input)

        # 変換ボタン
        chbutton = tk.Button(self, text='変換', padx=20,
                             pady=20, font=(10), command=clickedOnButton)
        chbutton.grid(row=3, column=1)

        def clickedOnClearButton():
            initbox(inbox)
            initbox(outbox)
            initEntry(capbox)
            initEntry(labbox)

        clearButton = tk.Button(self, text='消去', command=clickedOnClearButton)
        clearButton.grid(row=4, column=1)


if __name__ == '__main__':
    f = Application()
    f.pack()
    f.mainloop()
