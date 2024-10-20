import asyncio
import edge_tts

import asyncio
import edge_tts

file_path = "script.txt"
with open(file_path, 'r') as file:
    text = file.read()
async def text_to_mp3(text, output_file):
    tts = edge_tts.Communicate(text,
                               voice="en-US-ChristopherNeural",
                               rate="+0%")
    await tts.save(output_file)
if __name__ == "__main__":
    output_file = "output.mp3"
    asyncio.run(text_to_mp3(text, output_file))
    print(f"MP3 file saved as {output_file}")


