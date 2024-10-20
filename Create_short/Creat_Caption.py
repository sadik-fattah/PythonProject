def text_srt(text_file, srt_file):
    with open(text_file, 'r') as file:
        lines = file.readlines()
    with open(srt_file, 'w') as srt:
        for i, line in enumerate(lines):
            start_time = f"{i // 2:02}:00:00,000"
            end_time = f"{(i // 2 + 1):02}:00:00,000"
            srt.write(f"{i + 1}\n")
            srt.write(f"{start_time} --> {end_time}\n")
            srt.write(line.strip() + "\n\n")


text_srt('script.txt', 'output.srt')