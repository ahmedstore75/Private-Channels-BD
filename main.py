import requests

# M3U প্লেলিস্টের URL
PLAYLIST_URL = "https://raw.githubusercontent.com/sm-monirulislam/Tapmad_Auto_Update_Playlist/refs/heads/main/tapmad_sm.m3u"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
}


def fetch_and_generate():
    try:
        # M3U ডাটা ফেচ করা
        res = requests.get(PLAYLIST_URL, headers=headers)

        if res.status_code == 200:
            m3u_data = res.text

            # প্রাপ্ত ডাটা সরাসরি playlist.m3u8 ফাইলে সেভ করা
            with open("playlist.m3u8", "w", encoding="utf-8") as f:
                f.write(m3u_data)

            print("playlist.m3u8 সফলভাবে আপডেট হয়েছে!")
        else:
            print(f"HTTP Error: {res.status_code}")

    except Exception as e:
        print(f"Error fetching playlist: {e}")

        # কোনো ত্রুটি হলে ডিফল্ট প্লেলিস্ট তৈরি করা
        default_content = (
            "#EXTM3U\n#EXTINF:-1, Default Stream\nhttps://example.com/live.m3u8"
        )
        with open("playlist.m3u8", "w", encoding="utf-8") as f:
            f.write(default_content)
        print("ডিফল্ট ডাটা দিয়ে playlist.m3u8 সেভ করা হয়েছে।")


if __name__ == "__main__":
    fetch_and_generate()
