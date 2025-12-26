from ai_clients import get_gemini_free_response
from prompts import get_gemini_generation_prompt


def generate_answer_gemini(model, question_text):
    full_prompt = get_gemini_generation_prompt(question_text)
    return get_gemini_free_response(model, full_prompt)