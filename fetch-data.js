const fs = require('fs');

// আপনার M3U/M3U8 প্লেলিস্টের লিংক
const API_URL = 'https://raw.githubusercontent.com/sm-monirulislam/Tapmad_Auto_Update_Playlist/refs/heads/main/tapmad_sm.m3u'; 

async function updatePlaylist() {
  try {
    const response = await fetch(API_URL, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // রেসপন্স থেকে M3U ডাটা টেক্সট হিসেবে পড়া
    const playlistContent = await response.text();

    // প্রাপ্ত প্লেলিস্ট ডাটা সরাসরি 'playlist.m3u8' ফাইলে রাইট করা
    fs.writeFileSync('playlist.m3u8', playlistContent);
    console.log('playlist.m3u8 সফলভাবে আপডেট হয়েছে!');

  } catch (error) {
    console.error('ত্রুটি:', error.message);
    
    // কোনো ত্রুটি হলে বা লিংক কাজ না করলে ডিফল্ট ফাইল তৈরি হবে
    const defaultContent = `#EXTM3U\n#EXTINF:-1, Default Stream\nhttps://example.com/live.m3u8`;
    fs.writeFileSync('playlist.m3u8', defaultContent);
    console.log('ডিফল্ট ডাটা দিয়ে playlist.m3u8 সেভ করা হয়েছে।');
  }
}

updatePlaylist();
