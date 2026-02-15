#!/usr/bin/env python3
import json
import sys
from pathlib import Path

WEIGHTS = {
    "pain": 0.20,
    "wtp": 0.20,
    "frequency": 0.15,
    "distribution": 0.15,
    "feasibility": 0.10,
    "advantage": 0.10,
    "retention": 0.05,
    "risk_inverse": 0.05,
}


def score(item):
    total = 0.0
    for k, w in WEIGHTS.items():
        v = float(item.get(k, 0))
        if v < 0 or v > 5:
            raise ValueError(f"{item.get('name','unknown')}: field {k} must be 0..5")
        total += v * w
    return round(total * 20, 2)


def band(total):
    if total >= 80:
        return "BUILD_NOW"
    if total >= 65:
        return "VALIDATE_HARD"
    if total >= 50:
        return "HOLD"
    return "KILL"


def main():
    if len(sys.argv) < 2:
        print("Usage: score_ideas.py <ideas.json>")
        sys.exit(1)

    path = Path(sys.argv[1])
    ideas = json.loads(path.read_text())

    out = []
    for item in ideas:
        s = score(item)
        row = dict(item)
        row["score"] = s
        row["decision"] = band(s)
        out.append(row)

    out.sort(key=lambda x: x["score"], reverse=True)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
