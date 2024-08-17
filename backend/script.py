import json

try:
    with open('./dump.json', 'r') as file:
        data = json.load(file)
    print(data['data'])
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except json.JSONDecodeError:
    print(f"Error: File '{file_path}' contains invalid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
