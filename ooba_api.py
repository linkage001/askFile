import requests
import json


class OobaApi:
    url = "http://127.0.0.1:5000/v1/completions"

    class templates:
        chat_ml = """<|im_start|> system
You are a helpful chatbot.<|im_end|>
<|im_start|> user
$$QUESTION$$<|im_end|>
<|im_start|> assistant
"""

    def complete(self, prompt: str, max_tokens=200) -> str:
        completion = ''

        data = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "stop": ["<|im_end|>"],
            # "preset": "llama.cpp"
        }

        response = requests.post(self.url, json=data)

        if response.status_code == 200:
            completions = response.json()['choices']
            for c in completions:
                completion = c
                break
        else:
            print(f"Error occurred: {response.text}")

        return completion['text']

    @staticmethod
    def format_question(question: str, template: str) -> str:
        prompt = template.replace('$$QUESTION$$', question)
        return prompt

    def ask(self, question: str, template: str = '', max_tokens=200) -> str:
        if template is None or template == '':
            template = self.templates.chat_ml
        prompt = self.format_question(question, template)
        completion = self.complete(prompt, max_tokens=max_tokens)
        return completion
