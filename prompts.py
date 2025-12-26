def get_gemini_generation_prompt(question_text):
    return f"""
            Act as an expert Senior Software Engineer. Your task is to provide a comprehensive answer to the following coding interview question:

            QUESTION: "{question_text}"

            INSTRUCTIONS:
            1. Provide the answer entirely in LaTeX format.
            2. Start directly with the explanation. Do not repeat the question or provide a top-level section title.
            3. Use \textbf{{}} for key terms and \texttt{{}} for code-related keywords or variable names.
            4. If an example is helpful, include a code block using the \begin{{lstlisting}} environment (assume the 'listings' package is available).
            5. Do not include any introductory or concluding remarks like "Here is the answer" or "I hope this helps." Return ONLY the LaTeX string.
            6. Use clear, not too complicated, pedagogical language suitable for a study guide.
            7. Ensure all special LaTeX characters (like _, &, %) are properly escaped unless they are inside a code environment.

            ANSWER:
            """
