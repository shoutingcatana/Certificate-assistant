import chatgpt
import user_screen


def create_prompt(criteria):
    prompt = f"""
Sei ein Lehrer: Schreibe zwei bis drei Sätze zu der Leistung eines Schülers   
anhand dieser Bewertungskriterien die auf einer Skale von 0 bis 10 getroffen wurden:

Pünktlichkeit:{criteria["Pünktlichkeit"]},
Hausaufgaben erledigt:{criteria["Hausaufgaben erledigt"]},
Mitarbeit:{criteria["Mitarbeit"]},
Konzentration:{criteria["Konzentration"]},
Kreativität{criteria["Kreativität"]}:,
Soziales Engagement:{criteria["Soziales Engagement"]}
"""

    return prompt


if __name__ == '__main__':
    # call api key
    with open("api.key.txt", "r") as api_key:
        API_KEY = api_key.read()
        # call chat gpt and tell him hsi role

    chat_gpt = chatgpt.ChatGPT(API_KEY, create_prompt)
    def update_func():
        print(create_prompt(user_screen.criteria))


    # create user interface with tkinter
    user_screen.create_screen(update_func)

    while (frage := input('\n> ')) != "X":
        antwort = chat_gpt.fragen(frage)
        print(antwort)




