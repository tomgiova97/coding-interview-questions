import json

def add_ids_to_json(input_file, output_file):
    # 1. Load the data from the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # 2. Iterate through the list and add the 'id' field
    # We use enumerate(data, start=1) to get both the index and the object
    for i, item in enumerate(data, start=1):
        item['id'] = i

    # 3. Save the modified data back to a file
    with open(output_file, 'w') as f:
        # indent=2 makes the file human-readable
        json.dump(data, f, indent=2)

# Usage
add_ids_to_json('coding-questions.json', 'questions_with_ids.json')