import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        # setting title
        root.title("Hesap Makinesi - Almina Akbal")
        # setting window size
        width = 558
        height = 648
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Labels for "Rakam1", "Rakam2", and "Sonuc"
        self.create_label(root, "Rakam1", 110, 200)
        self.create_label(root, "Rakam2", 230, 200)
        self.create_label(root, "Sonuc", 370, 200)

        # Entry fields for input
        self.num1_entry = self.create_entry(root, 110, 290)
        self.num2_entry = self.create_entry(root, 230, 290)
        self.result_entry = self.create_entry(root, 370, 290)

        # Operation buttons
        self.create_button(root, "+", 50, 420, self.add)
        self.create_button(root, "-", 180, 420, self.subtract)
        self.create_button(root, "*", 310, 420, self.multiply)
        self.create_button(root, "/", 440, 420, self.divide)

    def create_label(self, root, text, x, y):
        label = tk.Label(root, text=text, font=("Times", 10), fg="#333333", justify="center")
        label.place(x=x, y=y, width=70, height=25)
    
    def create_entry(self, root, x, y):
        entry = tk.Entry(root, font=("Times", 10), fg="#333333", justify="center")
        entry.place(x=x, y=y, width=70, height=25)
        return entry

    def create_button(self, root, text, x, y, command):
        button = tk.Button(root, text=text, bg="#2b2a33", fg="#fbfbfe", font=("Times", 10), justify="center", command=command)
        button.place(x=x, y=y, width=70, height=25)

    def add(self):
        self.calculate("add")

    def subtract(self):
        self.calculate("subtract")

    def multiply(self):
        self.calculate("multiply")

    def divide(self):
        self.calculate("divide")

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    result = "Hata: Bölme hatası"
                else:
                    result = num1 / num2
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Hata: Geçersiz giriş")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
