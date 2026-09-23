import requests
from config import settings

TOKEN = settings.COC_API_KEY
tag = "#80YQJ0RQQ"

headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.get(f"https://api.clashofclans.com/v1/players/%23{tag[1:]}", headers=headers)

with open("backend/coc-api-test2.json", "w") as f:
    f.write(response.text)

print("successfully wrote to file")