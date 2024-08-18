from typing import List
from datetime import datetime
from anime_types import BASED_DICT, DEGEN_GENRES, WHOLESOME_GENRES, AnimeEntry, InputAnimeData

def _calc_based(data: InputAnimeData) -> int:
    node_data = data["node"]
    anime_id = node_data["id"]
    if anime_id in BASED_DICT:
        return BASED_DICT[anime_id]

    return 50

def _calc_age(data: InputAnimeData) -> int:
    node_data = data["node"]
    created_at = node_data["created_at"]
    parsed_date = datetime.fromisoformat(created_at)
    current_date = datetime.now()
    years_since = current_date.year - parsed_date.year

    return min(100, round(years_since * 3.33))

def _calc_degen(data: InputAnimeData) -> int:
    node_data = data["node"]
    base_value = 0
    if "nsfw" in node_data:
        nsfw = node_data["nsfw"]

        if nsfw == 'gray':
            base_value = 50
        if nsfw == "black":
            base_value = 100

    for genre in node_data["genres"]:
        name = genre["name"]
        if name in WHOLESOME_GENRES:
            base_value -= 5
        if name in DEGEN_GENRES:
            base_value += 5

    return min(max(base_value, 0), 100)

def _calc_normie(data: InputAnimeData) -> int:
    return 0

def _calc_completion(data: InputAnimeData) -> int:
    return 0

def _calc_ranked(data: InputAnimeData) -> int:
    return 0

def _process_entry(data: InputAnimeData) -> AnimeEntry:
    return {
        "name": data["node"]["title"],
        "based": _calc_based(data),
        "age": _calc_age(data),
        "degen": _calc_degen(data),
        "normie": _calc_normie(data),
        "completion": _calc_completion(data),
        "ranked": _calc_ranked(data),
    }

def process(data: List[InputAnimeData]) -> List[AnimeEntry]:
    """Process raw data from MAL into a list of entries for ZK Circuit"""
    return [_process_entry(entry) for entry in data]
