import tkinter
import customtkinter
import random

special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", ";", ":", "'", "<", ">", ",", ".", "/", "?"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def make_password():
    available = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u",
                 "v", "w", "x", "y", "z"]

    length = int(password_length.get())
    new_password = []
    pass_string = ""

    if numbersVAR.get():
        for i in numbers:
            available.append(i)
    if specialBOOL.get():
        for i in special:
            available.append(i)

    j = 0
    while j < length:
        randint = random.randint(0, len(available) - 1)
        new_password.append(available[randint])
        j = j + 1

    for i in new_password:
        pass_string = pass_string + i
    print(pass_string)
    # new_pass = customtkinter.CTkLabel(master=root_tk, text=pass_string)
    # new_pass.place(relx=0.50, rely=0.42, anchor=tkinter.CENTER)
    new_pass.configure(root_tk, text=pass_string)


if __name__ == "__main__":
    root_tk = tkinter.Tk()
    root_tk.geometry("600x350")
    root_tk.resizable(width=False, height=False)
    root_tk.title("Password Generator")

    numbersVAR = tkinter.BooleanVar()
    number_box = customtkinter.CTkCheckBox(master=root_tk, text="Numbers", variable=numbersVAR, onvalue=True,
                                           offvalue=False)
    number_box.pack(padx=20, pady=10)
    number_box.place(relx=0.05, rely=0.11)

    specialBOOL = tkinter.BooleanVar()
    special_box = customtkinter.CTkCheckBox(master=root_tk, text="Special Letters", variable=specialBOOL, onvalue=True,
                                            offvalue=False)
    special_box.pack(padx=20, pady=10)
    special_box.place(relx=0.05, rely=0.19)

    password_length = customtkinter.CTkEntry(master=root_tk)
    password_length.place(relx=0.05, rely=0.28)
    password_length.insert(0, 5)

    password_button = customtkinter.CTkButton(master=root_tk, text="Generate Password",
                                              command=make_password, width=120,
                                              height=32, border_width=0, corner_radius=8)
    password_button.place(relx=0.16, rely=0.42, anchor=tkinter.CENTER)

    new_pass = customtkinter.CTkLabel(master=root_tk)
    new_pass.place(relx=0.50, rely=0.42, anchor=tkinter.CENTER)

    root_tk.mainloop()
