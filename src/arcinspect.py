from github_loader import get_all_source_files
from llama_summarizer import summarize_code
import json

if __name__ == "__main__":
    repo = input("🔍 Enter GitHub repo (format: owner/repo): ").strip()
    output = {}

    for file in get_all_source_files(repo):
        print(f"📄 Processing: {file['path']}")
        summary = summarize_code(file["path"], file["content"])
        output[file["path"]] = summary

    outname = repo.replace("/", "_") + "_summary.json"
    with open(outname, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Summary written to {outname}")
