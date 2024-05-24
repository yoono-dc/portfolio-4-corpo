import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch Game")
        self.root.geometry("400x240")
        self.root.configure(bg="#333")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="0", font=("Helvetica", 48), fg="#fff", bg="#333")
        self.time_label.pack(pady=20)

        button_frame = tk.Frame(root, bg="#333")
        button_frame.pack()

        self.start_button = self.create_button(button_frame, "Start", self.start, "#fff")
        self.stop_button = self.create_button(button_frame, "Stop", self.stop, "#fff")

        self.update_time()

    def create_button(self, frame, text, command, color):
        button = tk.Button(frame, text=text, font=("Helvetica", 12), command=command, bg=color, fg="#000")
        button.pack(side=tk.LEFT, padx=10)
        return button
        
    def start(self):
        if not self.running:
            self.running = False
            self.start_time = 0
            self.elapsed_time = 0
            self.running = True
            self.start_time = datetime.now()
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time += (datetime.now() - self.start_time).total_seconds()
            if self.elapsed_time >= 11:
                messagebox.showinfo('結果', 'FAIL かたつむり級')
            elif self.elapsed_time >= 10.81:
                messagebox.showinfo('結果', 'POOR のろま級')
            elif self.elapsed_time >= 10.51:
                messagebox.showinfo('結果', 'OK 凡人級')
            elif self.elapsed_time >= 10.21:
                messagebox.showinfo('結果', 'GOOD 玄人級!')
            elif self.elapsed_time >= 10.11:  
                messagebox.showinfo('結果', 'GREAT 超人級!')
            elif self.elapsed_time > 10:
                messagebox.showinfo('結果', 'NEAR-PERFECT サイボーグ級!')
            elif self.elapsed_time == 10:
                messagebox.showinfo('結果', 'PERFECT AI級!!')
            elif self.elapsed_time >= 9.9:
                messagebox.showinfo('結果', 'NEAR-PERFECT サイボーグ級!')
            elif self.elapsed_time >= 9.8:
                messagebox.showinfo('結果', 'GREAT 超人級!')
            elif self.elapsed_time >= 9.6:
                messagebox.showinfo('結果', 'GOOD 玄人級!')
            elif self.elapsed_time >= 9.5:
                messagebox.showinfo('結果', 'OK 凡人級')
            elif self.elapsed_time >= 9.2:
                messagebox.showinfo('結果', 'POOR せっかち級')
            else:
                messagebox.showinfo('結果', 'FAIL 鉄砲玉級')

    def update_time(self):
        if self.running:
            elapsed = self.elapsed_time + (datetime.now() - self.start_time).total_seconds()
        else:
            elapsed = self.elapsed_time
        
        seconds = round((elapsed % 60), 2)
        
        time_string = f"{seconds}"
        self.time_label.config(text=time_string)
        self.root.after(100, self.update_time)

root = tk.Tk()
app = StopwatchApp(root)
root.mainloop()