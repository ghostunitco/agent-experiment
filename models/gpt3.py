import openai
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

class GPT3:
    def __init__(self):
        openai.api_key = config['gpt3']['api_key']

    def generate_text(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].text
