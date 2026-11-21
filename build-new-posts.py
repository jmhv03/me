import json, pathlib, re

root = pathlib.Path("new-posts")
exts = {".jpg", ".jpeg", ".png", ".webp", ".mp4", ".mov", ".webm", ".m4v"}
natural = lambda p: [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]
posts = []

for d in sorted(root.iterdir(), reverse=True):
    if not d.is_dir():
        continue
    cap = d / "caption.txt"
    media = sorted((f for f in d.iterdir() if f.suffix.lower() in exts), key=natural)
    if not media:
        continue
    posts.append({
        "date": d.name[:10],
        "caption": cap.read_text(encoding="utf-8").strip() if cap.exists() else "",
        "images": [f"new-posts/{d.name}/{f.name}" for f in media],
    })

pathlib.Path("new-posts.json").write_text(
    json.dumps(posts, indent=2, ensure_ascii=False), encoding="utf-8")
