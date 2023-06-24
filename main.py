import chatgpt
import user_screen
import better_user_interface
import openai


def create_prompt(criteria):
    prompt = f"""
Sei ein Lehrer: Schreibe zwei bis drei Sätze zu der Leistung eines Schülers 
anhand dieser Bewertungskriterien die auf einer Skale von 0 bis 10 getroffen wurden
und beschränke dich auf eine für ein 
Zeugnis vernünftige länge. Erwähne nicht die Skala oder die dir gegebenen Zahlen:

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

    def update_func():
        prompt = create_prompt(user_screen.criteria)
        # chat_gpt = chatgpt.ChatGPT(API_KEY, prompt)
        openai.api_key = API_KEY
        dialog = [{"role": "system", "content": prompt}]
        ergebnis = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=dialog
        )
        antwort = ergebnis.choices[0].message.content
        return antwort

    # create user interface with tkinter
    better_user_interface.create_screen(update_func)





