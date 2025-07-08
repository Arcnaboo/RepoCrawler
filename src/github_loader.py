import requests

def get_all_source_files(repo_full_name: str):
    owner, repo = repo_full_name.split("/")
    api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1"
    res = requests.get(api_url)
    data = res.json()

    for file in data["tree"]:
        path = file["path"]
        if path.endswith((".py", ".cpp", ".c", ".h", ".cu")) and "test" not in path.lower():
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"
            try:
                code = requests.get(raw_url).text
                yield {"path": path, "content": code}
            except Exception as e:
                print(f"⚠️ Failed to fetch {path}: {e}")
