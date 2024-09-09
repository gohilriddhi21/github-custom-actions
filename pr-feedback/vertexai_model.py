import logging
import vertexai
from vertexai.generative_models import (
    GenerativeModel,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class VertexAIModel:
    """Model Class to interact with the Vertex AI Model."""
    def __init__(
        self,
        project: str = "",
        location: str = "",
        model: str = "gemini-1.5-pro",
    ):
        vertexai.init(project=project, location=location)
        client = GenerativeModel(model)
        self.client = client
        self.model = model

    def generate_text(self, prompt) -> str:
        """Generate response for the given prompt."""
        response = self.client.generate_content(prompt)
        return self.translate_response(response)

    def translate_response(self, response) -> str:
        """Translate the Vertex AI response to text."""
        try:
            selected_msg = response.candidates[0]
            return selected_msg.content.parts[0].text
        except Exception as e:
            logger.exception(f"An error occurred while translating Vertex AI response: {e}")
            raise e


if __name__ == "__main__":
    try:
        model = VertexAIModel(project="", location="")
        result = model.generate_text("Why is sky blue?")
        print(result)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")