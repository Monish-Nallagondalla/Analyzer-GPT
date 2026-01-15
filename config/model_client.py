import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import OPENAI_API_KEY , MODEL 

load_dotenv()

api_key = os.getenv(OPENAI_API_KEY)


def get_model_client():
    if not api_key:
        raise ValueError(f"Please set the {OPENAI_API_KEY} environment variable.")

        model_client = OpenAIChatCompletionClient(
            api_key=api_key,
            model=MODEL,
        )
        return model_client
    