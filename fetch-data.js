const fs = require('fs');

// আসল M3U8 বা লাইভ স্কোরের API URL (এখানে সঠিক API বা প্লেলিস্ট লিংক বসান)
const API_URL = 'https://www.tapmad.com/api/live-score'; 

async function updatePlaylist() {
  try {
    const response = await fetch(API_URL, {
      headers: {
        // ব্রাউজার হিসেবে রিকোয়েস্ট পাঠানোর জন্য User-Agent
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.text();

    // M3U8 ফরম্যাটে ডাটা সাজানো
    const fileContent = `#EXTM3U\n#EXTINF:-1, Live Stream\n${data}`;

    fs.writeFileSync('playlist.m3u8', fileContent);
    console.log('playlist.m3u8 সফলভাবে আপডেট হয়েছে!');
  } catch (error) {
    console.error('ত্রুটি:', error.message);
    process.exit(1);
  }
}

updatePlaylist();
