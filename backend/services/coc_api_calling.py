
import requests
from backend.config import settings
from fastapi import HTTPException

TOKEN = settings.COC_API_KEY

def call_coc_api(player_tag : str):
    try:
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(f"https://api.clashofclans.com/v1/players/%23{player_tag[1:]}", headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="COC API response failed")
            
        return response.json()
    except requests.exceptions.SSLError as e:
        raise HTTPException(status_code=400, detail=f"SSL certificate verification failed: {e}")


    except requests.exceptions.ConnectionError as e:
        raise HTTPException(status_code=400, detail=f"Connection error: {e}")

    except requests.exceptions.Timeout as e:
        raise HTTPException(status_code=400, detail=f"Request timed out: {e}")

    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=400, detail=f"HTTP error: {e}")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Request failed: {e}")
