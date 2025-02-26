import json

# Loop to create files from quoraan_31.json to quoraan_114.json
for i in range(4, 115):  # From 31 to 114 inclusive
    # filename = f"Quoraan_{i}.java"
    filename = f"quoraan_{i}.json"

    # Example content for the JSON file (you can modify this part to fit your needs)
    content = {
        "title": "",
        "sections": [
            {
                "title": "بِسْمِ ۱للَّهِ ۱لرَّحْمَـٰنِ ۱لرَّحِيمِ",
                "content": [
                    ""
                ]
            }
        ]
    }

    # Write content to the JSON file with UTF-8 encoding
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)

    print(f"File {filename} created successfully.")
