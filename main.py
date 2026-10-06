import json
import requests

# এখানে আসল JSON API বা JSON ফাইলের URL বসাতে হবে (.m3u এর লিংক নয়)
SETTINGS_URL = "https://example.com/api/settings.json"
HEADER_URL = "https://example.com/api/header.json"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_and_generate():
    m3u_lines = ["#EXTM3U\n"]

    # ১. App Settings JSON থেকে চ্যানেল এক্সট্র্যাক্ট করা
    try:
        res = requests.get(SETTINGS_URL, headers=headers)
        if res.status_code == 200:
            data = res.json()

            # ব্যাকআপের জন্য ব্যাকএন্ড JSON সেভ করা
            with open("app_settings.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            # JSON ডাটা থেকে চ্যানেল লিস্ট খুঁজে বের করা
            channels = []
            if isinstance(data, dict):
                channels = data.get("channels", []) or data.get("data", [])
            elif isinstance(data, list):
                channels = data

            # প্রতিটা চ্যানেল পার্স করে M3U স্ট্রাকচারে আনা
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

    # ২. Preference JSON সেভ করা (যদি প্রয়োজন থাকে)
    try:
        res2 = requests.get(HEADER_URL, headers=headers)
        if res2.status_code == 200:
            with open("user_preference.json", "w", encoding="utf-8") as f:
                json.dump(res2.json(), f, indent=4)
    except Exception as e:
        print(f"Error fetching preference: {e}")

    # ৩. ডাটা না পাওয়া গেলে অন্তত একটা ডিফল্ট চ্যানেল যোগ করা
    if len(m3u_lines) == 1:
        m3u_lines.append("#EXTINF:-1, Default Stream\nhttps://example.com/live.m3u8\n")

    # ৪. ফাইল এক্সটেনশন .m3u হিসেবে সেভ করা
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.writelines(m3u_lines)

    print("playlist.m3u সফলভাবে তৈরি হয়েছে!")


if __name__ == "__main__":
    fetch_and_generate()
