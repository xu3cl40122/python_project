import tkinter as tk
import tr as tr

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
        self.entry_inputFile = tk.Entry(self, textvariable=self.inputFile, width=20)
        self.entry_inputFile.insert(0, './tr_pic.xlsx')
        self.entry_inputFile.grid(row=1, column=1, padx=10, pady=10)

        self.label_outputFile = tk.Label(self, text='output excel:')
        self.label_outputFile.grid(row=1, column=2, padx=10, pady=10)
        self.outputFile = tk.StringVar()
        self.entry_outputFile = tk.Entry(self, textvariable=self.outputFile, width=20)
        self.entry_outputFile.insert(0, 'tr_pic_output.xlsx')
        self.entry_outputFile.grid(row=1, column=3, padx=10, pady=10)

        self.start_button = tk.Button(self, text = 'start', width = 10, command = self.start )
        self.start_button.grid(row=2, column=2, padx=10, pady=10)
    def say_hi(self):
        print(self.rows.get())
    def start(self):
        subfile = self.subFile.get()
        rows = int(self.rows.get())
        inputFile = self.inputFile.get()
        outputFile = self.outputFile.get() 
        tr.main(subfile, rows, outputFile ,inputFile)


root = tk.Tk()
app = Application(master=root)
app.master.title("My Application")
app.master.maxsize(800, 600)
app.mainloop()
