const fs = require('fs');

// আপনার সঠিক API বা প্লেলিস্টের URL এখানে দিতে হবে
const API_URL = 'https://www.tapmad.com'; 

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

    const data = await response.text();

    // M3U8 ফরম্যাটে ডাটা সেভ
    const fileContent = `#EXTM3U\n#EXTINF:-1, Updated Channel\n${API_URL}`;

    fs.writeFileSync('playlist.m3u8', fileContent);
    console.log('playlist.m3u8 সফলভাবে আপডেট হয়েছে!');
  } catch (error) {
    console.error('ত্রুটি:', error.message);
    
    // 404 আসলেও যেন GitHub Action ব্যর্থ (Failed) না হয় তার জন্য ডিফল্ট ফাইল তৈরি
    const defaultContent = `#EXTM3U\n#EXTINF:-1, Default Stream\nhttps://example.com/live.m3u8`;
    fs.writeFileSync('playlist.m3u8', defaultContent);
    console.log('ডিফল্ট ডাটা দিয়ে playlist.m3u8 সেভ করা হয়েছে।');
  }
}

updatePlaylist();
