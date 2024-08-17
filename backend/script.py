import json
from typing import List

from anime_types import AnimeEntry, InputAnimeData

def _process_entry(data: InputAnimeData) -> AnimeEntry:
    print(data)

    return {
        "name": "abc",
        "based": 75,
        "age": 15,
        "degen": 75,
        "normie": 90,
        "completion": 50,
        "ranked": 75,
    }

def process(data: List[InputAnimeData]) -> List[AnimeEntry]:
    """Process raw data from MAL into a list of entries for ZK Circuit"""
    return [_process_entry(entry) for entry in data]

file_path = './dump.json'
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    process(data['data'])
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except json.JSONDecodeError:
    print(f"Error: File '{file_path}' contains invalid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
