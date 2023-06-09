import tkinter as tk

class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Window')
        self.geometry('300x200')

        button = tk.Button(self, text='Нажми на меня!')
        button.place(x=100, y=100)
        button.config(command=self.on_button_click)

    def on_button_click(self):
        print('Кнопка нажата')

if __name__ == '__main__':
    window = MyWindow()
    window.mainloop()