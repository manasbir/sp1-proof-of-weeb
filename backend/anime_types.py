from typing import List, TypedDict, Optional

class AnimeEntry(TypedDict):
    name: str
    based: int
    age: int
    degen: int
    normie: int
    completion: int
    ranked: int

class AnimeData(TypedDict):
    username: str
    timestamp: str
    data: List[AnimeEntry]

class GenreData(TypedDict):
    id: int
    name: str

class NodeData(TypedDict):
    id: int
    title: str
    mean: float
    popularity: int
    nsfw: Optional[str]
    genres: List[GenreData]
    created_at: str

class ListStatusData(TypedDict):
    status: str
    score: int
    num_episodes_watched: int
    is_rewatching: bool

class InputAnimeData(TypedDict):
    node: NodeData
    list_status: ListStatusData

WHOLESOME_GENRES = set([
    "Kids",
    "Childcare",
    "Isekai",
    "Reincarnation",
    "Slice of Life",
    "Educational",
])

DEGEN_GENRES = set([
    "Girls Love",
    "Boys Love",
    "Ecchi",
    "Erotica",
    "Hentai",
    "Anthropomorphic",
    "Crossdressing",
    "Magical Sex Shift",
    "Harem",
    "Reverse Harem",
])
