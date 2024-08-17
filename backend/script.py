import json
from typing import List

from anime_types import InputAnimeData, AnimeData

def process(data: List[InputAnimeData]) -> AnimeData:
    print(data)

    return {
        "username": "joe",
        "data": [],
        "timestamp": ""
    }

file_path = './dump.json'
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(data['data'])
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except json.JSONDecodeError:
    print(f"Error: File '{file_path}' contains invalid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
