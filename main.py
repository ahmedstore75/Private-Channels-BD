import requests

# M3U প্লেলিস্টের URL
PLAYLIST_URL = "https://raw.githubusercontent.com/sm-monirulislam/Tapmad_Auto_Update_Playlist/refs/heads/main/tapmad_sm.m3u"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
}


def update_playlist():
    try:
        res = requests.get(PLAYLIST_URL, headers=headers)

        if res.status_code == 200:
            # m3u ফাইলের কনটেন্ট সরাসরি সেভ করা
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(res.text)
            print("playlist.m3u সফলভাবে তৈরি হয়েছে!")
        else:
            raise Exception(f"HTTP Error: {res.status_code}")

    except Exception as e:
        print(f"ত্রুটি: {e}")

        # ফেচিং এ সমস্যা হলে ডিফল্ট m3u ফাইল সেভ হবে
        default_content = (
            "#EXTM3U\n#EXTINF:-1, Default Stream\nhttps://example.com/live.m3u8"
        )
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(default_content)
        print("ডিফল্ট ডাটা দিয়ে playlist.m3u সেভ করা হয়েছে।")


if __name__ == "__main__":
    update_playlist()
