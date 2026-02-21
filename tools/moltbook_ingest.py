#!/usr/bin/env python3
import os, json, datetime, urllib.request, urllib.parse
from pathlib import Path


def load_env_file(path: Path):
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


root = Path("/root/.openclaw/workspace/saas-os")
load_env_file(root / ".secrets" / "moltbook.env")

BASE = os.getenv("MOLTBOOK_API_BASE", "https://www.moltbook.com/api/v1")
KEY = os.getenv("MOLTBOOK_API_KEY", "")
if not KEY:
    raise SystemExit("MOLTBOOK_API_KEY is required (set env or .secrets/moltbook.env)")

TZ_OFFSET_HOURS = 4  # Asia/Dubai
now = datetime.datetime.utcnow() + datetime.timedelta(hours=TZ_OFFSET_HOURS)
date_str = now.strftime("%Y-%m-%d")

raw_dir = root / "00_inbox"
out_dir = root / "05_experiments" / "moltbook"
raw_dir.mkdir(parents=True, exist_ok=True)
out_dir.mkdir(parents=True, exist_ok=True)

headers = {"Authorization": f"Bearer {KEY}", "Accept": "application/json"}

def fetch(path, params):
    url = f"{BASE}{path}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))

def as_list(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for k in ("posts", "items", "data", "results"):
            if isinstance(payload.get(k), list):
                return payload[k]
    return []

def score_post(p):
    title = (p.get("title") or "").strip()
    content = (p.get("content") or "").strip()
    comments = p.get("comment_count") or p.get("comments_count") or p.get("num_comments") or 0
    upvotes = p.get("upvotes") or p.get("score") or p.get("votes") or 0
    sub = p.get("submolt") or p.get("community") or ""

    s = 0.0
    s += min(float(upvotes), 200.0) * 0.35
    s += min(float(comments), 80.0) * 0.9
    s += min(len(title), 140) * 0.08
    s += min(len(content), 2500) * 0.02

    text = (title + "\n" + content).lower()
    signal_words = [
        "revenue", "churn", "pricing", "compliance", "lawsuit", "conversion",
        "seo", "ai", "automation", "payout", "deliverability", "onboarding",
        "retention", "acquisition", "mrr", "ltv", "cac", "workflow", "manual"
    ]
    s += sum(2.5 for w in signal_words if w in text)

    junk_words = ["meme", "lol", "shitpost", "gm", "good morning", "karma"]
    s -= sum(4 for w in junk_words if w in text)

    if sub in ("general", "introductions"):
        s -= 1.5

    return round(s, 2)

all_posts = []
for sort in ("hot", "top", "new", "rising"):
    payload = fetch("/posts", {"sort": sort, "limit": 60})
    all_posts.extend(as_list(payload))

# de-dup by id/url/title
seen = set()
unique = []
for p in all_posts:
    pid = p.get("id") or p.get("post_id") or p.get("uuid") or ""
    key = pid or (p.get("url") or "") or (p.get("title") or "")
    if not key or key in seen:
        continue
    seen.add(key)
    p["_score"] = score_post(p)
    unique.append(p)

unique.sort(key=lambda x: x.get("_score", 0), reverse=True)
selected = unique[:200]
top20 = selected[:20]
top5 = selected[:5]

raw_path = raw_dir / f"moltbook-raw-{date_str}.jsonl"
with raw_path.open("w", encoding="utf-8") as f:
    for p in selected:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")

report_path = out_dir / f"moltbook-top-{date_str}.md"
with report_path.open("w", encoding="utf-8") as f:
    f.write(f"# Moltbook Top Signals — {date_str}\n\n")
    f.write(f"Collected: {len(all_posts)} | Unique: {len(unique)} | Selected: {len(selected)}\n\n")
    f.write("## Top 5 (actionable)\n")
    for i, p in enumerate(top5, 1):
        title = (p.get("title") or "(no title)").replace("\n", " ")
        url = p.get("url") or p.get("permalink") or ""
        sub = p.get("submolt") or p.get("community") or "unknown"
        f.write(f"{i}. **{title}**  \\n")
        f.write(f"   score: `{p.get('_score',0)}` | submolt: `{sub}`")
        if url:
            f.write(f" | [link]({url})")
        f.write("\n")

    f.write("\n## Top 20 shortlist\n")
    for i, p in enumerate(top20, 1):
        title = (p.get("title") or "(no title)").replace("\n", " ")
        f.write(f"{i}. {title} — score `{p.get('_score',0)}`\n")

print(str(report_path))
print(str(raw_path))
