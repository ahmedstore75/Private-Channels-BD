import json
import requests

# API URL
settings_url = (
    "https://backend-api.tapmad.com/api/getMobileAppSettings/V1/en/web"
)
header_url = "https://backend-api.tapmad.com/api/getUserPrefernceHeader"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
}


def fetch_and_generate():
    m3u_lines = ["#EXTM3U\n"]

    # 1. Fetch App Settings JSON
    try:
        res = requests.get(settings_url, headers=headers)
        if res.status_code == 200:
            data = res.json()

            # Save full JSON file
            with open("app_settings.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            # JSON ডাটা খুঁজে ভিডিও লিঙ্ক / চ্যানেল এক্সট্র্যাক্ট করার চেষ্টা
            channels = []
            if isinstance(data, dict):
                # JSON এর ভেতরে চ্যানেল বা ক্যাটাগরি ফিল্টার করা
                channels = data.get("channels", []) or data.get("data", [])
            elif isinstance(data, list):
                channels = data

            for item in channels:
                if isinstance(item, dict):
                    name = item.get("name") or item.get("title") or "Unknown Channel"
                    stream_url = (
                        item.get("stream_url")
                        or item.get("url")
                        or item.get("m3u8_url")
                    )

                    if stream_url:
                        m3u_lines.append(f"#EXTINF:-1, {name}\n{stream_url}\n")

    except Exception as e:
        print(f"Error fetching settings: {e}")

    # 2. Fetch User Preference Header JSON
    try:
        res2 = requests.get(header_url, headers=headers)
        if res2.status_code == 200:
            with open("user_preference.json", "w", encoding="utf-8") as f:
                json.dump(res2.json(), f, indent=4)
    except Exception as e:
        print(f"Error fetching preference: {e}")

    # 3. Save M3U Playlist
    with open("playlist.m3u8", "w", encoding="utf-8") as f:
        f.writelines(m3u_lines)

    print("Processing complete!")


if __name__ == "__main__":
    fetch_and_generate()
