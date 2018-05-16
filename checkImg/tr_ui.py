import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_rows = tk.Label(self, text = 'excel 列數:')
        self.label_rows.grid(row=0, column=0, padx=10, pady=10)

        self.rows = tk.StringVar()
        self.entry_rows = tk.Entry(self, textvariable = self.rows, width = 10)
        self.entry_rows.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_subFile = tk.Label(self, text='子資料夾:')
        self.label_subFile.grid(row=0, column=2, padx=10, pady=10)

        self.subFile = tk.StringVar()
        self.entry_subFile = tk.Entry(self, textvariable=self.subFile, width=10)
        self.entry_subFile.insert(0,'/05')#預設值
        self.entry_subFile.grid(row=0, column=3, padx=10, pady=10)

        self.label_inputFile = tk.Label(self, text='input excel:')
        self.label_inputFile.grid(row=1, column=0, padx=10, pady=10)
        self.inputFile = tk.StringVar()
        self.entry_inputFile = tk.Entry(self, textvariable=self.inputFile, width=10)
        self.entry_inputFile.insert(0, './test.xlsx')
        self.entry_inputFile.grid(row=1, column=1, padx=10, pady=10)

        self.label_outputFile = tk.Label(self, text='output excel:')
        self.label_outputFile.grid(row=1, column=2, padx=10, pady=10)
        self.outputFile = tk.StringVar()
        self.entry_outputFile = tk.Entry(self, textvariable=self.outputFile, width=10)
        self.entry_outputFile.insert(0, 'output_test.xlsx')
        self.entry_outputFile.grid(row=1, column=3, padx=10, pady=10)



    def say_hi(self):
        print(self.rows.get())


root = tk.Tk()
app = Application(master=root)
app.master.title("My Application")
app.master.maxsize(800, 600)
app.mainloop()
