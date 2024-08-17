from typing import List
from anime_types import AnimeEntry, InputAnimeData

def _calc_based(data: InputAnimeData) -> int:
    return 0

def _calc_age(data: InputAnimeData) -> int:
    return 0

def _calc_degen(data: InputAnimeData) -> int:
    return 0

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
