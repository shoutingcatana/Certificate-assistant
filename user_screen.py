import tkinter as tk


def slider_changed(value, i):
    # print(f"Wert:{value}")
    print(f"Regler:{i}")
    pass


def create_screen():
    # tk basics
    root = tk.Tk()
    root.title("Titel")
    root.geometry("400x400")
    root.resizable(False, False)
    criteria = ["Pünktlichkeit:", "Hausaufgaben erledigt:", "Mitarbeit:", "Konzentration:", "Kreativität:",
                "Soziales Engagement:"]
    text = criteria[0]
    note_results = []

    # create list of sliders and textes
    slider_list = []
    text_list = []
    for i in range(6):
        text = criteria[i]
        text_widget = tk.Text(root, height=1)
        text_widget.insert(tk.END, text)
        text_list.append(text_widget)
        # the i in the following tuple shows me which slider got changed
        slider = (tk.Scale(root, from_=0, to=10, orient="horizontal", command=lambda value: slider_changed(value, text)))
        slider_list.append(slider)

    # draw sliders and textes on the screen
    for i in range(6):
        slider_list[i].pack()
        text_list[i].pack()

    root.mainloop()



