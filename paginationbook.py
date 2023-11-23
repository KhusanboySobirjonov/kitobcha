import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import datetime
from tktooltip import ToolTip


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kitobcha")
        self.geometry("440x540")
        self.resizable(False, False)
        Frame(self).pack()
        self.config(bg="white")
        self.mainloop()


class Frame(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root, width=440, height=540, fg_color="#A0CCDA")
        self.pack_propagate(False)
        font_style = ("Helvetica", 12)

        entry1 = ctk.CTkEntry(self, width=200, height=30, justify="right", border_width=1, border_color="#231F20",
                              placeholder_text="Sahifalar sonini kiriting", font=font_style)
        entry1.place(x=20, y=20)

        combo1 = ctk.CTkComboBox(self, width=60, height=30, values=['1', '2'], border_width=1,
                                 border_color="#231F20", font=font_style)
        combo1.place(x=240, y=20)
        ToolTip(combo1, "1 ta sahifada nechta bet bo'lishi")

        button1 = ctk.CTkButton(self, width=100, height=30, text="Bajarish")
        button1.place(x=320, y=20)
        ToolTip(button1, "Dasturni ishga tushirish")

        textbox1 = ctk.CTkTextbox(self, width=340, height=120, state="disabled", border_width=1, border_color="#231F20")
        textbox1.place(x=20, y=70)

        copy_button1 = ctk.CTkButton(self, width=50, height=60, text="Nusxa\nolish",
                                     command=lambda: self.copy_clipboard(textbox1.get("1.0", "end-1c")))
        copy_button1.place(x=370, y=70)
        ToolTip(copy_button1, "Nusxalash")

        text1 = ctk.CTkLabel(self, text="Tashqi\ntomon")
        text1.place(x=375, y=140)

        textbox2 = ctk.CTkTextbox(self, width=340, height=120, state="disabled", border_width=1, border_color="#231F20")
        textbox2.place(x=20, y=210)

        text2 = ctk.CTkLabel(self, text="Ichki\ntomon")
        text2.place(x=375, y=280)

        copy_button2 = ctk.CTkButton(self, width=50, height=60, text="Nusxa\nolish",
                                     command=lambda: self.copy_clipboard(textbox2.get("1.0", "end-1c")),)
        copy_button2.place(x=370, y=210)
        ToolTip(copy_button2, "Nusxalash")

        program_guide = """    Dasturni ishlatish tartibi :
 1. Sahifalar sonini kiriting.
 2. Bitta sahifada nechta bet joylashishini belgilang.
 3. Bajarish tugmasini bosing.
 4. Chiqqan natijalarni nusxalab oling.
 5. Endi esa printerda shu betlarni chiqarsangiz ma'lumotlarni kitobcha shakliga keltira olasiz.
        """

        textbox3 = ctk.CTkTextbox(self, width=400, height=140, border_width=1, border_color="#231F20")
        textbox3.place(x=20, y=350)

        textbox3.insert("1.0", program_guide)
        textbox3.configure(state="disabled")

        label = ctk.CTkLabel(self, text=f"© Andijon {datetime.date.today().year}")
        label.place(x=180, y=500)

        button1.configure(command=lambda: self.use_page(textbox1, textbox2, combo1.get(), entry1.get()))

    def copy_clipboard(self, content):
        if content:
            self.clipboard_clear()
            self.clipboard_append(content)
            self.update()
            messagebox.showinfo("Bajarildi", "Matn vaqtinchalik xotiraga nusxalandi!")
        else:
            messagebox.showwarning("Ogohlantirish", "Nusxalash uchun hech narsa yo'q.")

    def use_page(self, text1, text2, value, page_count):
        text1.configure(state='normal')
        text2.configure(state='normal')
        text1.delete("1.0", tk.END)
        text2.delete("1.0", tk.END)
        if not page_count.isdigit():
            messagebox.showwarning("Ogohlantirish", "Sahifalar soni butun son bo'lishi kerak")
            return
        page_count = int(page_count)
        left = []
        right = []
        a = 0
        if value == '1':
            a = (page_count + 1) // 2
            left = list(range(1, page_count+1, 2))
            right = list(range(2, page_count+1, 2))
        else:
            a = (page_count + 3) // 4
            n = a * 4
            for i in range(a):
                left.extend([n - 2 * i, 2 * i + 1])
                right.extend([2 * i + 2, n - 2 * i - 1])

        messagebox.showinfo("Bajarildi", f"Umumiy {a} ta qog'oz ishlatilinadi. Kitobni chop etish uchun.")

        text1.insert("1.0", ','.join(str(i) for i in left))
        text2.insert("1.0", ','.join(str(i) for i in right))
        text1.configure(state='disabled')
        text2.configure(state='disabled')