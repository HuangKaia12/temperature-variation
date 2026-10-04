# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib","requests"]
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

    rows = raw["data"]

    day_of_year = []
    temp_values = []
    temp_sizes = []
    year_pos = []
    skipped = 0

    # loop over dataset (required for assignment)
    for r in rows:
        try:
            y = int(r[0])
            m = int(r[1])
            d = int(r[2])
            t = float(r[3])
            dt = datetime(y,m,d)
            day_of_year.append(dt.timetuple().tm_yday)
            year_pos.append(y)
            temp_values.append(t)
            temp_sizes.append(t * 2.8)
        except Exception:
            skipped +=1

    print(f"Valid points:{len(day_of_year)}, skipped:{skipped}")

    fig, ax = plt.subplots(figsize=(12,6),dpi=150)
    bg_color = "#070720"
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    scatter = ax.scatter(
        day_of_year, year_pos,
        s=temp_sizes,
        c=temp_values,   # 颜色使用原始温度，不是放大后的size
        cmap="magma",
        alpha=0.72,
        edgecolors="none"
    )

    ax.set_title("Hong Kong Daily Mean Temperature Variation", color="white", fontsize=13, pad=14)
    ax.set_xlabel("Day of Year", color="white", labelpad=10)
    ax.set_ylabel("Year", color="white", labelpad=10)

    month_ticks = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    month_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    ax.set_xticks(month_ticks)
    ax.set_xticklabels(month_labels, color="white", fontsize=9)

    ax.tick_params(axis="y", colors="white", labelsize=9)
    ax.tick_params(axis="x", colors="white")

    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label("Mean Temperature (°C)", color="white", fontsize=9)
    cbar.ax.yaxis.label.set_color('white')
    plt.setp(cbar.ax.get_yticklabels(), color='white', fontsize=8)

    ax.text(0.98, 0.02, "Data source: HKO CLMTEMP Open API",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="#cccccc")

    os.makedirs("out", exist_ok=True)
    out_file = "out/thermal_variation.png"
    plt.tight_layout()
    plt.savefig(out_file, bbox_inches="tight", pad_inches=0.4)
    plt.close()
    print(f"Output: {out_file}")

if __name__ == "__main__":
    main()