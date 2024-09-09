import google.generativeai as genai
import os

class GenAIModel:
    def __init__(self, 
                 model = 'gemini-1.5-flash'
    ):
        genai.configure(api_key=os.environ["AI_STUDIO_API_KEY"])
        self.client = genai.GenerativeModel(model)

    def generate_text(self, prompt) -> str:
        response = self.client.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    try:
        model = GenAIModel()
        result = model.generate_text("Why is sky blue?")
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
