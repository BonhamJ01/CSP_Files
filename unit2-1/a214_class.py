import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title('Login Practice')



user_label = tk.Label(root, text = 'Username:')
user_label.pack()
root.mainloop()