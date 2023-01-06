import tkinter
import customtkinter
import convolution

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1200x675")
app.title("Convulation")
app.minsize(1200, 675)

# entries rel positions
relpos = [0.25, 0.5, 0.75]


# fonts
title_font = customtkinter.CTkFont(family="consolas", size=40)
font_1 = customtkinter.CTkFont(family="consolas", size=30)
font_2 = customtkinter.CTkFont(family="consolas", size=25)
font_3 = customtkinter.CTkFont(family="consolas", size=30, weight="bold")
button_font = customtkinter.CTkFont(family="consolas", size=30)

# title
title_text = "Tired of doing Matrix Convolution😑"
title = customtkinter.CTkLabel(master=app, text=title_text, font=title_font)
title.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

# subtitle
subtitle_text = "You've come to right place😏"
subtitle = customtkinter.CTkLabel(
    master=app, text=subtitle_text, font=title_font)
subtitle.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

# frames
window_frame = customtkinter.CTkFrame(master=app, width=320, height=320)
window_frame.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
# window label
window_label = customtkinter.CTkLabel(
    master=window_frame, text="Window", font=font_1)
window_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
# window entries
window_entries = [customtkinter.CTkEntry(
    master=window_frame, font=font_2, width=60, height=60, justify="center") for entry in range(9)]
temp_x = 0
temp_y = 0
for entry in window_entries:
    entry.place(relx=relpos[temp_x],
                rely=relpos[temp_y], anchor=tkinter.CENTER)
    # print(hex(id(entry)))
    temp_y += 1
    if temp_y > 2:
        temp_y = 0
        temp_x += 1


kernel_frame = customtkinter.CTkFrame(master=app, width=320, height=320)
kernel_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# kernel label
kernel_label = customtkinter.CTkLabel(
    master=kernel_frame, text="Kernel", font=font_1)
kernel_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
# kernel entries
factor_entry = customtkinter.CTkEntry(
    master=app, placeholder_text="factor", font=font_2, justify="center")
factor_entry.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)


kernel_entries = [customtkinter.CTkEntry(
    master=kernel_frame, font=font_2, width=60, height=60, justify="center") for entry in range(9)]
temp_x = 0
temp_y = 0
for entry in kernel_entries:
    entry.place(relx=relpos[temp_x],
                rely=relpos[temp_y], anchor=tkinter.CENTER)
    temp_y += 1
    if temp_y > 2:
        temp_y = 0
        temp_x += 1

result_frame = customtkinter.CTkFrame(master=app, width=320, height=320)
result_frame.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)
# result label
result_label = customtkinter.CTkLabel(
    master=result_frame, text="Result", font=font_1)
result_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
# results entries
result_entries = [customtkinter.CTkEntry(
    master=result_frame, font=font_2, width=60, height=60, justify="center") for entry in range(9)]
result_entries[4].configure(width=80, height=80, font=font_3, fg_color="red")

temp_x = 0
temp_y = 0
for entry in result_entries:
    entry.place(relx=relpos[temp_x],
                rely=relpos[temp_y], anchor=tkinter.CENTER)
    temp_y += 1
    if temp_y > 2:
        temp_y = 0
        temp_x += 1

# error label
error_label = customtkinter.CTkLabel(
    master=app, font=font_1, text_color="red", text="")
error_label.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)

# button action


def button_action():
    try:
        window = [
            [int(window_entries[0].get()), int(
                window_entries[1].get()), int(window_entries[2].get())],
            [int(window_entries[3].get()), int(
                window_entries[4].get()), int(window_entries[5].get())],
            [int(window_entries[6].get()), int(
                window_entries[7].get()), int(window_entries[8].get())]
        ]
        kernel = [
            [int(kernel_entries[0].get()), int(
                kernel_entries[1].get()), int(kernel_entries[2].get())],
            [int(kernel_entries[3].get()), int(
                kernel_entries[4].get()), int(kernel_entries[5].get())],
            [int(kernel_entries[6].get()), int(
                kernel_entries[7].get()), int(kernel_entries[8].get())]
        ]

        factor = int(factor_entry.get())
        error_label.configure(text="")

        result = convolution.convolution_calculation(window, kernel, factor)
        # print(result)
        for i in range(9):
            if i == 4:
                result_entries[i].delete(0, tkinter.END)
                result_entries[i].insert(0, result)
            else:
                result_entries[i].delete(0, tkinter.END)
                result_entries[i].insert(0, window_entries[i].get())
    except:
        error_label.configure(
            text="Something went wrong😥\nCHECK INPUT VALUES🤔")


# button
button = customtkinter.CTkButton(
    master=app, text="Apply Filter", font=button_font, border_spacing=10, command=button_action)
button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


app.mainloop()
