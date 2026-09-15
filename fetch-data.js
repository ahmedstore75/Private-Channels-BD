const fs = require('fs');

// আসল API লিংক (প্রয়োজন অনুযায়ী লিংক ও হেডার পরিবর্তন করতে পারেন)
const API_URL = 'https://cdn.sportmonks.com/images/cricket/leagues/'; 

async function updatePlaylist() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error('API থেকে ডাটা পাওয়া যায়নি');

    const data = await response.text(); // বা response.json()

    // M3U8 বা ডাটা ফরম্যাট সাজিয়ে ফাইলেই রাইট করা
    const fileContent = `#EXTM3U\n#EXTINF:-1, Live Match Data\n${data}`;

    fs.writeFileSync('playlist.m3u8', fileContent);
    console.log('playlist.m3u8 সফলভাবে আপডেট হয়েছে!');
  } catch (error) {
    console.error('ত্রুটি:', error.message);
    process.exit(1);
  }
}

updatePlaylist();
