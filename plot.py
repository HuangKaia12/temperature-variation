# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "matplotlib",
#   "requests"
# ]
# ///

import requests
import json
import pandas as pd

# 读取数据
df = pd.read_csv("data/hko-daily-mean-temperature-2026.csv")

# 计算一年当中的天数
df["day_of_year"] = pd.to_datetime({
    "year": df["year"],
    "month": df["month"],
    "day": df["day"]
}).dt.dayofyear

# 创建画布
fig, ax = plt.subplots(figsize=(14, 9), dpi=120)

# 绘制散点图
scatter = ax.scatter(
    data=df,
    x="day_of_year",
    y="year",
    c="daily_mean_temp",
    cmap="magma",
    alpha=0.8,
    s=60
)

# Y轴翻转：最上方旧年份(1890)，最下方新年份(2025)
ax.invert_yaxis()

# 图表标题与坐标轴标签
ax.set_title("Hong Kong Daily Mean Temperature Variation (Full Historical Dataset)", pad=16)
ax.set_xlabel("Day of Year", fontsize=11)
ax.set_ylabel("Year", fontsize=11)

# X轴月份刻度
ax.set_xticks([1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335])
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Y轴年份刻度 + 边界，防止贴边
ax.set_yticks([1890, 1920, 1940, 1950, 1980, 2010, 2025])
ax.set_ylim(2030, 1880)

# Gap注释，完全置于空白间隙正中
ax.text(
    x=240,
    y=1943,
    s="Gap: No observations\n1940‑1946 (WWII suspension)",
    ha="center",
    va="center",
    fontsize=9,
    color="black",
    bbox=dict(
        facecolor="white",
        alpha=0.85,
        edgecolor="gray",
        boxstyle="round,pad=0.35"
    )
)

# 右侧色条
cbar = plt.colorbar(scatter)
cbar.set_label("Mean Temperature (°C)")

plt.tight_layout()
plt.savefig("out/full_temp_plot.png")
plt.show()