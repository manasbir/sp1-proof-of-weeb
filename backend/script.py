import json
import re
import requests

from services import process

def test_process():
    file_path = './dump.json'
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(process(data['data']))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

animes = { "Neon Genesis Evangelion": 70, "Lain": 0, "Azumanga Daioh": 60, "jjk season 1": 60, "Jjk season 2": 100, "Durarara": 70, "Code Geass": 95, "Shimoneta": 20, "Keijo": 45, "High School DxD": 65, "Megalo Box": 85, "No Game No Life": 75, "No Game No Life: Zero": 85, "Date a Live": 10, "Gundam 00": 80, "ReLIFE": 70, "Princess Principal": 75, "Tsurezure Children": 45, "Akashic Records of Bastard Magic Instructor": 15, "Undefeated Bahamut Chronicle": 0, "Rewrite": 65, "Castle Town Dandelion": 35, "Space Patrol Luluco": 75, "Love Live!": 30, "Tengen Toppa Gurren Lagann": 100, "Amagi Brilliant Park": 25, "Cross Ange: Rondo of Angels and Dragons": 75, "Gundam Build Fighters": 90, "Log Horizon": 70, "The Irregular at Magic High School": 50, "Yugioh Zexal": 75, "Yugioh 5Ds": 85, "Gamers!": 75, "Zombieland Saga": 95, "Steins,Gate": 100, "Violet Evergarden": 17, "Angel Beats!": 40, "Promare": 100, "Space☆Dandy": 95, "Gunbuster 2": 90, "Magical Girl Lyrical Nanoha": 100, "Showa Genroku Rakugo Shinju": 70, "Perfect Blue": 77, "My Next Life as a Villainess: All Routes Lead to Doom!": 100, "Humanity Has Declined": 85, "New Game!": 60, "My Teen Romantic Comedy SNAFU ": 100, "Concrete Revolutio": 90, "Pui Pui Molcar": 10000000000, "Vivy -Fluorite Eye's Song-": 70, "SSSS.Gridman": 100, "Nodame Cantabile": 55, "Shirobako": 80, "SK8": 100, "Given": 75, "Revue Starlight": 100, "Girls und Panzer": 25, "Free": 25, "86": 65, "Science Fell in Love, So I Tried to Prove It": 5, "The Demon Girl Next Door": 30, "Yuru Camp": 40, "Symphogear": 100, "Uchuu Senkan Yamato 2199": 100, "SHINE POST": 100, "Fate Zero": 65, "Bungou Stray Dogs": 80, "Odd Taxi": 55, "Yowamushi Pedal": 100, "Saekano: How to Raise a Boring Girlfriend": 20, "Girls Band Cry": 100, "Bottom-Tier Character Tomozaki": 100, "Gushing over Magical Girls": 5, "Bang Brave Bang Bravern": 100, "High Card": 45, "Skip to Loafer": 80, "The 100 Girlfriends Who Really, Really, Really, Really, REALLY Love You": 0, "Uma Musume: Pretty Derby": 90, "Demon Slayer": 0, "The Eminence in Shadow": 20, "Scott Pilgrim Takes Off": 45, "The Masterful Cat Is Depressed Again Today": 50}
headers = { "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjZjYTIzOGE2ZDcyMzc5MGEwMTZkOTIxNGYzMTNmOGRhMjU1MGM3NGMyNDBjZWE4NjdlMjhjMWRiYzljNjc3MmE3ZmUzNzFmNjMyYTUxMzMyIn0.eyJhdWQiOiI4NTc5ZWVjYjg3MGM3Yjk1MTc0NzE3OTE3M2NmYjYzNCIsImp0aSI6IjZjYTIzOGE2ZDcyMzc5MGEwMTZkOTIxNGYzMTNmOGRhMjU1MGM3NGMyNDBjZWE4NjdlMjhjMWRiYzljNjc3MmE3ZmUzNzFmNjMyYTUxMzMyIiwiaWF0IjoxNzIzOTM3NjQ0LCJuYmYiOjE3MjM5Mzc2NDQsImV4cCI6MTcyNjYxNjA0NCwic3ViIjoiMTg4MTA5MjciLCJzY29wZXMiOltdfQ.Itw6GYA3ey5AgaUo3rnv_AJ2VspmifSQLSgUAr2EHKQl3rvYlVfEcg06z6eh4Axzrs_nn_CubIWAaCBcELTD5TalF1WygqpwhQK_lgQ25SQtxm8MzwqDXa-jjIrOzUzbThnQbITpdHaay84YOt0RSNf58jSdi8sjMaMlEKqrz4181fuNHUBNHZpDKVlahsrKUjVo4SV8MxaiIfKmU0XsunAFwtfVMn5yRR7eltSvtkqJrqmdQsfgi4H-6HxApZGUyjjoEU1bPhC3cVHVE-S_282H3NUBDQ3KGIieKD0ovkDTn-hmOJPW31893n1ShhzzvFV7wxdnWUUmhEmoDqkc8Q" }
def find_animes():
    for anime in animes:
        stripped = re.sub(r'\W+', '', anime)
        url = f"https://api.myanimelist.net/v2/anime?q={stripped}&limit=1"
        try:
            print(str(requests.get(url, headers=headers).json()['data'][0]['node']['id']) + ':', str(max(0, min(100, animes[anime]))) + ',')
        except:
            pass

# find_animes()
test_process()
