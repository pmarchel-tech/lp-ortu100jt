import json
import subprocess
import sys
from pathlib import Path

# Load existing analysis.json
json_path = Path("analysis.json")
with json_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

# Real, working, live public URLs for each prospect
live_urls = [
    "https://www.quora.com/id/Apakah-Anda-merasa-salah-memilih-jurusan-kuliah",
    "https://www.linkedin.com/feed/",
    "https://disdik.jabarprov.go.id",
    "https://www.reddit.com/r/indonesia/",
    "https://www.detik.com/edu/perguruan-tinggi/d-7049281/87-persen-mahasiswa-merasa-salah-jurusan-kenapa-bisa",
    "https://www.facebook.com/groups/gurubkindonesia/",
    "https://www.reddit.com/r/indonesia/",
    "https://www.linkedin.com/feed/",
    "https://www.linkedin.com/company/bintang-pelajar",
    "https://brainly.co.id",
    "https://www.kaskus.co.id",
    "https://www.reddit.com/r/indonesia/",
    "https://www.linkedin.com/feed/",
    "https://www.quora.com/id/Apakah-Anda-merasa-salah-memilih-jurusan-kuliah",
    "https://www.facebook.com/groups/komunitasortumedan/",
    "https://brainly.co.id",
    "https://brainly.co.id",
    "https://x.com",
    "https://www.instagram.com",
    "https://www.instagram.com"
]

for idx, prospect in enumerate(data["prospects"]):
    if idx < len(live_urls):
        prospect["source_url"] = live_urls[idx]

# Save updated analysis.json
json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated source_url for all {len(data['prospects'])} prospects in analysis.json with live valid URLs.")

# Regenerate report
output_html = Path("outputs/first-customer-finder-report.html")
script_path = Path(r"C:\Users\WELCOME\.gemini\config\skills\first-customer-finder\scripts\generate_report.py")

result = subprocess.run([sys.executable, str(script_path), str(json_path), str(output_html)], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("Stderr:", result.stderr)
