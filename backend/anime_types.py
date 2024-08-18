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

BASED_DICT = {
    3785: 70,
    339: 0,
    1593: 60,
    40028: 60,
    25777: 100,
    23199: 70,
    2904: 95,
    29786: 20,
    32686: 45,
    11617: 65,
    36563: 85,
    19815: 75,
    33674: 85,
    15583: 10,
    84: 80,
    35466: 70,
    721: 75,
    34902: 45,
    32951: 15,
    30749: 0,
    31716: 65,
    28387: 35,
    32681: 75,
    2001: 100,
    1082: 25,
    25731: 75,
    40942: 90,
    23321: 70,
    20785: 50,
    10015: 75,
    3972: 85,
    34280: 75,
    37976: 95,
    11577: 100,
    37987: 17,
    35994: 40,
    35848: 100,
    20057: 95,
    1911: 90,
    36266: 100,
    28735: 70,
    28621: 77,
    42282: 100,
    10357: 85,
    31953: 60,
    14813: 100,
    31147: 90,
    44235: 100,
    46095: 70,
    35847: 100,
    1698: 55,
    25835: 80,
    49363: 100,
    37970: 100,
    14131: 25,
    18507: 25,
    38992: 5,
    39071: 30,
    34798: 40,
    11751: 100,
    23249: 100,
    32526: 100,
    11741: 65,
    31478: 80,
    50653: 55,
    24277: 100,
    30727: 20,
    40530: 100,
    36266: 5,
    28497: 100,
    49154: 45,
    50416: 80,
    54714: 0,
    35249: 90,
    38000: 0,
    48316: 20,
    14653: 45,
    51916: 50,
}
