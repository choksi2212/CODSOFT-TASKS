import tkinter as tk
from tkinter import font

class BasicCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Basic Calculator")
        self.geometry("400x500")
        self.configure(bg="#F5F5F5")
        
        # Set custom fonts
        self.custom_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.display_font = font.Font(family="Helvetica", size=24)
        
        self.create_widgets()
        
    def create_widgets(self):
        self.result_var = tk.StringVar()
        
        # Display
        display = tk.Entry(self, textvariable=self.result_var, font=self.display_font, bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            if button == "=":
                btn = tk.Button(self, text=button, padx=20, pady=20, bd=8, fg="white", bg="#4CAF50",
                                font=self.custom_font, command=lambda b=button: self.calculate())
            else:
                btn = tk.Button(self, text=button, padx=20, pady=20, bd=8, fg="white", bg="#2196F3",
                                font=self.custom_font, command=lambda b=button: self.on_button_click(b))
            
            btn.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            
            if col_val > 3:
                col_val = 0
                row_val += 1
                
        # Clear button
        clear_btn = tk.Button(self, text='C', padx=20, pady=20, bd=8, fg="white", bg="#f44336",
                              font=self.custom_font, command=self.clear_display)
        clear_btn.grid(row=row_val, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        # Backspace button
        backspace_btn = tk.Button(self, text='⌫', padx=20, pady=20, bd=8, fg="white", bg="#FFC107",
                                  font=self.custom_font, command=self.backspace)
        backspace_btn.grid(row=row_val, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")
        
    def on_button_click(self, char):
        current_text = self.result_var.get()
        new_text = current_text + char
        self.result_var.set(new_text)
    
    def clear_display(self):
        self.result_var.set("")
        
    def backspace(self):
        current_text = self.result_var.get()
        new_text = current_text[:-1]
        self.result_var.set(new_text)
    
    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    app = BasicCalculator()
    app.mainloop()
