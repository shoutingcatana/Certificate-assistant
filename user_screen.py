import tkinter as tk

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
        print(criteria)
    return save_values


def create_screen(update_func):
    # tk basics
    root = tk.Tk()
    root.title("Titel")
    root.geometry("600x600")
    root.resizable(False, False)

    # create list of sliders and textes
    slider_list = []
    text_list = []
    for name, value in criteria.items():
        text_widget = tk.Text(root, height=1)
        text_widget.insert(tk.END, name)
        text_list.append(text_widget)
        # the i in the following tuple shows me which slider got changes

        note_results = create_lambda_function(name)
        slider = tk.Scale(root, from_=0, to=10, orient="horizontal", command=note_results)
        slider_list.append(slider)

    # draw sliders and textes on the screen
    for i in range(6):
        text_list[i].pack()
        slider_list[i].pack()

    # create button
    button = tk.Button(command=update_func, text="Neuer Text")
    button.pack()


    root.mainloop()


