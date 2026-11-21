import json, pathlib

root = pathlib.Path("new-posts")
exts = {".jpg", ".jpeg", ".png", ".webp"}
posts = []

for d in sorted(root.iterdir(), reverse=True):
    if not d.is_dir():
        continue
    cap = d / "caption.txt"
    posts.append({
        "date": d.name[:10],
        "caption": cap.read_text(encoding="utf-8").strip() if cap.exists() else "",
        "images": [f"new-posts/{d.name}/{f.name}"
                   for f in sorted(d.iterdir()) if f.suffix.lower() in exts],
    })

pathlib.Path("new-posts.json").write_text(
    json.dumps(posts, indent=2, ensure_ascii=False), encoding="utf-8")
