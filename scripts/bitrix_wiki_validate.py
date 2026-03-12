#!/usr/bin/env python3
import argparse
import json
import os
import sys


REQUIRED_FIELDS = [
    "id",
    "type",
    "title",
    "source_url",
    "source_type",
    "tags",
]


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Bitrix wiki index JSON.")
    parser.add_argument("--index", required=True, help="Path to api/index.json")
    args = parser.parse_args()

    if not os.path.isfile(args.index):
        print("index not found")
        return 2

    data = load_json(args.index)
    entities = data.get("entities", [])
    errors = 0
    for i, e in enumerate(entities):
        for f in REQUIRED_FIELDS:
            if f not in e:
                errors += 1
                print(f"[{i}] missing field: {f}")
        if not isinstance(e.get("tags", []), list):
            errors += 1
            print(f"[{i}] tags must be list")
    if errors:
        print(f"validation failed: {errors} errors")
        return 1
    print("validation ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
