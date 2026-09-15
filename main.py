import json
import requests

# API URLs
settings_url = (
    "https://backend-api.tapmad.com/api/getMobileAppSettings/V1/en/web"
)
header_url = "https://backend-api.tapmad.com/api/getUserPrefernceHeader"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
}


def fetch_and_save():
    # 1. Fetch App Settings JSON
    try:
        res1 = requests.get(settings_url, headers=headers)
        if res1.status_code == 200:
            with open("app_settings.json", "w", encoding="utf-8") as f:
                json.dump(res1.json(), f, indent=4)
            print("app_settings.json saved successfully.")
    except Exception as e:
        print(f"Error fetching app settings: {e}")

    # 2. Fetch User Preference Header JSON
    try:
        res2 = requests.get(header_url, headers=headers)
        if res2.status_code == 200:
            with open("user_preference.json", "w", encoding="utf-8") as f:
                json.dump(res2.json(), f, indent=4)
            print("user_preference.json saved successfully.")
    except Exception as e:
        print(f"Error fetching user preference: {e}")

    # 3. Create a basic M3U playlist file structure
    m3u_content = "#EXTM3U\n#EXTINF:-1, Tapmad Settings Data\napp_settings.json\n"
    with open("playlist.m3u8", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("playlist.m3u8 created.")


if __name__ == "__main__":
    fetch_and_save()
