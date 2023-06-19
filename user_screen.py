import tkinter as tk


def slider_changed(value, i):
    value = int(value)
    return value, i


def create_screen():
    # tk basics
    root = tk.Tk()
    root.title("Titel")
    root.geometry("400x400")
    root.resizable(False, False)
    criteria = ["Pünktlichkeit:", "Hausaufgaben erledigt:", "Mitarbeit:", "Konzentration:", "Kreativität:",
                "Soziales Engagement:"]

    # create list of sliders and textes
    slider_list = []
    text_list = []
    for i in range(6):
        text = criteria[i]
        text_widget = tk.Text(root, height=1)
        text_widget.insert(tk.END, text)
        text_list.append(text_widget)
        # the i in the following tuple shows me which slider got changed

        def create_lambda_function(index):
            return lambda value: slider_changed(value, index)

        note_results = create_lambda_function(i)
        slider = tk.Scale(root, from_=0, to=10, orient="horizontal", command=note_results)
        slider_list.append(slider)
        print(note_results)
        
    # draw sliders and textes on the screen
    for i in range(6):
        slider_list[i].pack()
        text_list[i].pack()


    root.mainloop()


