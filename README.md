![Hong Kong historical daily mean temperature heat‑scatter plot](./out/full_temp_plot.png)

## The phenomenon
Surface air temperature shows strong seasonal cycles every year, while long‑term records also reveal multi‑decadal climate variation in Hong Kong. This visualisation explores how daily mean temperature changes across seasons and over more than one century. We examine both repeating annual summer‑winter temperature cycles and historical gaps in meteorological observations caused by World War II.

## The source
Data comes from Hong Kong Observatory CLMTEMP open API. Each row represents one calendar day, containing year, month, day and daily‑mean air temperature in degrees Celsius. The full dataset spans 1890‑2025, with roughly 49 000 daily observations.

API endpoint: https://www.hko.gov.hk/tc/gts/CLMTEMP_API.htm

## What the picture shows
The horizontal axis represents day‑of‑year to show seasonal change, and vertical axis plots years, with older years placed at top and newer years at bottom. Colour encodes daily mean temperature, with warmer tones representing higher values. A text annotation highlights the 1940‑1946 observation gap during WWII. This visualisation discards precise calendar timestamps and short‑term weather events, focusing only on aggregated daily temperature patterns.

## Run it
This project uses uv for dependency management.

Install dependencies:
```bash
uv sync