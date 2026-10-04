import requests
import json
import csv

def main():
    print("Fetch HKO CLMTEMP json (daily mean temperature)")
    url = "https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=CLMTEMP&station=HKO&rformat=json"
    resp = requests.get(url, timeout=20)

    if resp.status_code != 200:
        raise Exception(f"API请求失败，status code: {resp.status_code}")

    raw_data = resp.json()

    with open("data/cltemp.json", "w", encoding="utf‑8") as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=2)
    print("Saved -> data/cltemp.json")

    fields = raw_data["fields"]
    records_list = raw_data["data"]
    out_rows = []

    for row in records_list:
        row_dict = dict(zip(fields, row))
        val = row_dict["數值/Value"]
        if val == "***":
            continue
        out_rows.append({
            "year": int(row_dict["年/Year"]),
            "month": int(row_dict["月/Month"]),
            "day": int(row_dict["日/Day"]),
            "daily_mean_temp": float(val)
        })

    # 这里！！！文件名不要带空格
    csv_path = "data/hko-daily-mean-temperature-2026.csv"
    with open(csv_path, "w", newline="", encoding="utf‑8") as fout:
        writer = csv.DictWriter(fout, fieldnames=["year", "month", "day", "daily_mean_temp"])
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"Saved -> {csv_path}, total valid records: {len(out_rows)}")

if __name__ == "__main__":
    main()