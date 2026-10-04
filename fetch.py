# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
import requests
import json
import os

def main():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=CLMTEMP&station=HKO&rformat=json&year=2023"
    out_path = "data/clmtemp.json"
    os.makedirs("data", exist_ok=True)

    print("Fetch HKO CLMTEMP json (daily mean temperature)")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    with open(out_path,"w",encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved → {out_path}")

if __name__ == "__main__":
    main()