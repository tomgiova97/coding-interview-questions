import json

FILE_PATH = "coding-questions.json"


def get_first_unanswered_question():
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    # Use next() with a generator expression
    # The second argument (None) is returned if no match is found
    first_unanswered_question = next(
        (item for item in data if item.get("answer") is None), None
    )

    return first_unanswered_question


def replace_question_object_by_id(target_id, updated_question_object):
    # 1. Load the existing data
    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    found = False
    # 2. Iterate and find the match
    for i, item in enumerate(data):
        if item.get("id") == target_id:
            # Update the dictionary at this index
            # We ensure the ID stays the same even if the new_content doesn't have it
            data[i] = updated_question_object
            found = True
            break

    if found:
        # 3. Save the updated list back to the file
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Successfully updated object with ID {target_id}.")
    else:
        print(f"Error: ID {target_id} not found in the file.")


import json


def json_to_latex(output_file):
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    latex_content = r"""\documentclass{article}
                    \usepackage[utf8]{inputenc}
                    \usepackage[margin=1in]{geometry}
                    \usepackage{listings}
                    \usepackage{xcolor}
                    \usepackage{hyperref}

                    % --- Custom Colors for Code ---
                    \definecolor{backcolour}{rgb}{0.95,0.95,0.92}
                    \lstset{
                        backgroundcolor=\color{backcolour},
                        basicstyle=\ttfamily\footnotesize,
                        breaklines=true,
                        frame=single,
                        keywordstyle=\color{blue}
                    }

                    \title{Full-Stack Interview Guide}
                    \author{Gemini Study Partner}
                    \date{\today}

                    \begin{document}
                    \maketitle
                    \tableofcontents
                    \newpage
                    """

    for item in data:
        # We use the JSON 'question' to create a Table of Contents entry
        # but we use \section* to avoid redundant titles if the AI provided one.
        # Alternatively, we just use \section and trim the AI's first line.
        
        # Strip potential leading/trailing whitespace from AI answer
        answer_body = item['answer'].strip() if item['answer'] else "Pending answer..."
        
        # If the AI answer already contains a \section, we don't add another one
        if "\\section" not in answer_body:
            latex_content += f"\\section{{{item['question']}}}\n"
        
        latex_content += f"{answer_body}\n\n"
        latex_content += r"\clearpage" # Starts each question on a new page

    latex_content += r"\end{document}"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)