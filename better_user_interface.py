import tkinter
import main

import customtkinter


criteria = {
    "Pünktlichkeit": 0,
    "Hausaufgaben erledigt": 0,
    "Mitarbeit": 0,
    "Konzentration": 0,
    "Kreativität": 0,
    "Soziales Engagement": 0,
}


def create_lambda_function(name):
    def save_values(value):
        criteria[name] = value
    return save_values


def chat_gpt_response(response):
    global answer
    answer = response
    print(answer)
    return answer


answer = "text"


def create_screen(update_func):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.geometry("600x600")
    root.title("Certificate Assistent")

    slider_list = []
    entry_list = []
    for name, value in criteria.items():
        note_results = create_lambda_function(name)
        slider = customtkinter.CTkSlider(root, from_=0, to=10, command=note_results)
        entry = customtkinter.CTkEntry(root, placeholder_text=name)
        entry_list.append(entry)
        slider_list.append(slider)

    for i in range(len(slider_list)):
        entry_list[i].grid(row=i, column=0, padx=10, pady=10, sticky="e")
        slider_list[i].grid(row=i, column=1, padx=10, pady=10, sticky="w")

    # Zentriere das Grid in der Mitte des Bildschirms
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # create a button
    button = customtkinter.CTkButton(root, text="Run", command=update_func)
    button.grid(row=6, columnspan=2, pady=10)

    textbox = customtkinter.CTkTextbox(root)

    textbox.insert("0.0", answer)  # insert at line 0 character 0
    textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
    # textbox.delete("0.0", "end")  # delete all text
    textbox.configure(state="disabled")  # configure textbox to be read-only

    textbox.grid(row=7, columnspan=2, padx=10, pady=10, sticky="nsew")

    root.mainloop()

