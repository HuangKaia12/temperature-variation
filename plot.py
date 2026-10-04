# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///
import json
import matplotlib.pyplot as plt
from datetime import datetime
import os

def main():
    json_path = "data/clmtemp.json"
    if not os.path.exists(json_path):
        raise FileNotFoundError("Run uv run fetch.py first")

    with open(json_path,"r",encoding="utf-8") as f:
        raw = json.load(f)

    fields = raw["fields"]
    print("==== REAL FIELDS ====")
    print(fields)
    print("====================")
    rows = raw["data"]

    day_of_year = []
    temp_sizes = []
    year_pos = []
    skipped = 0

    for r in rows:
        try:
            y = int(r[0])
            m = int(r[1])
            d = int(r[2])
            t = float(r[3])
            dt = datetime(y,m,d)
            day_of_year.append(dt.timetuple().tm_yday)
            year_pos.append(y)
            temp_sizes.append(t*4)
        except Exception:
            skipped +=1

    print(f"Valid points:{len(day_of_year)}, skipped:{skipped}")

    fig, ax = plt.subplots(figsize=(12,6),dpi=150)
    ax.set_facecolor("#070720")
    fig.patch.set_facecolor("#070720")

    ax.scatter(
        day_of_year, year_pos,
        s=temp_sizes,
        c=temp_sizes,
        cmap="magma",
        alpha=0.7,
        edgecolors="none"
    )
    ax.axis("off")

    os.makedirs("out",exist_ok=True)
    out_file = "out/thermal_variation.png"
    plt.savefig(out_file, bbox_inches="tight", pad_inches=0)
    plt.close()
    print(f"Output: {out_file}")

if __name__ == "__main__":
    main()