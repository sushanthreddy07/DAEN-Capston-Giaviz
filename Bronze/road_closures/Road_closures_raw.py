import requests
import pandas as pd
from pandas import json_normalize
import itertools
import json
from datetime import datetime
import os

# ----------------------------
# Config
# ----------------------------
URL = "https://data.511-atis-ttrip-prod.iteriscloud.com/smarterRoads/other/vDOTRoadClosures/current/RoadClosures_current.json"
TOKEN = "$2b$10$PV4h67dDHewvUmQUSw.4EehnJ2kMRXNxo0M2/edpg2Q9/1KvHQnk2"

BRONZE_DIR = "./bronze/vdot_incidents"
os.makedirs(BRONZE_DIR, exist_ok=True)

# ----------------------------
# Helpers
# ----------------------------
def preview(obj, max_chars=800):
    try:
        s = json.dumps(obj, ensure_ascii=False)[:max_chars]
        return s + ("..." if len(s) == max_chars else "")
    except Exception:
        return str(obj)[:max_chars]

def looks_like_record(d: dict) -> bool:
    if not isinstance(d, dict):
        return False
    keys = set(d.keys())
    expected = {"orci:event_id", "orci:type_event", "orci:status", "road_closure"}
    return bool(keys & expected)

def find_records(payload):
    container = payload
    if isinstance(payload, dict):
        for k in ("roadClosures", "RoadClosures", "data", "items", "records"):
            if k in payload:
                container = payload[k]
                break

    if isinstance(container, list):
        recs = [r for r in container if isinstance(r, dict)]
        return recs, f"Found list with {len(recs)} dict records."

    if isinstance(container, dict):
        values = list(container.values())
        if values and all(isinstance(v, dict) for v in values):
            recs = [{"record_id": k, **v} for k, v in container.items()]
            return recs, f"Found dict keyed by IDs with {len(recs)} records."
        if looks_like_record(container):
            return [container], "Found a single record dict."

    return [], "No record-like container found."

# ----------------------------
# Main pipeline
# ----------------------------
def main():
    # Fetch API
    r = requests.get(URL, params={"token": TOKEN}, headers={"Accept": "application/json"}, timeout=60)
    r.raise_for_status()
    data = r.json()

    print("Top-level type:", type(data).__name__)
    if isinstance(data, dict):
        print("Top-level keys:", list(itertools.islice(data.keys(), 0, 30)))
    print("Top-level preview:", preview(data))

    # Extract records
    records, how = find_records(data)
    print(how)

    if not records:
        print("⚠️ No records found (could mean no current closures).")
        return

    # Flatten JSON
    df = json_normalize(records, sep="_")
    print("Row count:", len(df))
    print("Column count:", len(df.columns))
    print("Sample columns:", list(itertools.islice(df.columns, 0, 20)))

    # Save all closures → Bronze
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    all_file = os.path.join(BRONZE_DIR, f"road_closures_all_{timestamp}.csv")
    df.to_csv(all_file, index=False)
    print(f"✅ Saved all closures: {all_file}")

    # ----------------------------
    # Filter Fairfax County only
    # ----------------------------
    if "orci:to_intersection" in df.columns and "orci:from_intersection" in df.columns:
        df_fairfax = df[
            df["orci:to_intersection"].str.contains("Fairfax County", case=False, na=False)
            | df["orci:from_intersection"].str.contains("Fairfax County", case=False, na=False)
        ]

        fairfax_file = os.path.join(BRONZE_DIR, f"road_closures_fairfax_{timestamp}.csv")
        df_fairfax.to_csv(fairfax_file, index=False)
        print(f"✅ Saved Fairfax-only closures: {fairfax_file} ({len(df_fairfax)} rows)")
    else:
        print("⚠️ Could not find intersection columns. Check df.columns manually.")

if __name__ == "__main__":
    main()
