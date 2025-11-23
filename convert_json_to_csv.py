#!/usr/bin/env python3
import json
import csv
import os

INPUT = os.path.join(os.path.dirname(__file__), 'Option_TradingConditions.json')
OUTPUT = os.path.join(os.path.dirname(__file__), 'Option_TradingConditions.csv')


def flatten(obj, parent_key='', sep='.'):
    items = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten(v, new_key, sep=sep))
            elif isinstance(v, list):
                # If list contains only scalars, join them; if list contains dicts, enumerate and flatten each
                if all(not isinstance(i, dict) for i in v):
                    items[new_key] = '|'.join(map(str, v))
                else:
                    for idx, el in enumerate(v):
                        items.update(flatten(el, f"{new_key}[{idx}]", sep=sep))
            else:
                items[new_key] = v
    else:
        items[parent_key] = obj
    return items


def main():
    with open(INPUT, 'r', encoding='utf-8') as f:
        doc = json.load(f)

    # Expecting top-level key 'results' containing a list
    rows = doc.get('results') if isinstance(doc, dict) and 'results' in doc else (doc if isinstance(doc, list) else [])

    if not rows:
        print('No rows found in JSON. Exiting.')
        return

    flat_rows = [flatten(r) for r in rows]
    # Collect all fieldnames
    fieldnames = []
    for r in flat_rows:
        for k in r.keys():
            if k not in fieldnames:
                fieldnames.append(k)

    # Write CSV
    with open(OUTPUT, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in flat_rows:
            writer.writerow(r)

    print(f'Wrote {len(flat_rows)} rows to {OUTPUT}')


if __name__ == '__main__':
    main()
