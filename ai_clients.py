from google import genai
from openai import OpenAI
import json
from auth_credentials import GEMINI_API_KEY, GEMINI_FREE_API_KEY, CHAT_GPT_API_KEY

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

gemini_free_client = genai.Client(api_key=GEMINI_FREE_API_KEY)

chat_gpt_client = OpenAI(api_key=CHAT_GPT_API_KEY)


def get_gemini_free_response(model, generation_prompt):

    response = gemini_free_client.models.generate_content(
        model=model,
        contents=generation_prompt,
    )

    if (response.text is None):
        print(f"GEMINI API for model {model} is not available.")
        return
    
    return response.text.strip()


def get_chat_gpt_response(model, generation_prompt, response_format):

    completion = chat_gpt_client.chat.completions.create(
        model=model,
        store=True,
        messages=[{"role": "user", "content": generation_prompt}],
        response_format=response_format,
    )

    return json.loads(completion.choices[0].message.content)
