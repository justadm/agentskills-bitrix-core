#!/usr/bin/env python3
import argparse
import json
import os


def load_index(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build wiki landing pages from index.")
    parser.add_argument("--root", required=True, help="Wiki root folder")
    parser.add_argument("--methods-compact", action="store_true", help="Compact methods.json by dropping examples/errors")
    args = parser.parse_args()

    api_index = os.path.join(args.root, "api", "index.json")
    data = load_index(api_index)

    pages = []
    by_type = {}
    tags_index = {}
    by_section = {}
    for entity in data.get("entities", []):
        pages.append(f"- {entity.get('type')}: {entity.get('title')} ({entity.get('source_url')})")
        etype = entity.get("type", "guide")
        by_type.setdefault(etype, []).append(entity)
        for tag in entity.get("tags", []):
            tags_index.setdefault(tag, []).append(entity.get("id"))
        if entity.get("tags"):
            section = entity.get("tags")[0]
            by_section.setdefault(section, []).append(entity)

    summary = "# Wiki Index\n\n" + "\n".join(pages) + "\n"
    write_text(os.path.join(args.root, "wiki", "INDEX.md"), summary)
    write_text(
        os.path.join(args.root, "api", "index_by_type.json"),
        json.dumps({"version": data.get("version", "1.0"), "by_type": by_type}, ensure_ascii=False, indent=2),
    )
    write_text(
        os.path.join(args.root, "api", "tags.json"),
        json.dumps({"version": data.get("version", "1.0"), "tags": tags_index}, ensure_ascii=False, indent=2),
    )
    write_text(
        os.path.join(args.root, "api", "index_by_section.json"),
        json.dumps({"version": data.get("version", "1.0"), "by_section": by_section}, ensure_ascii=False, indent=2),
    )
    # Write per-section files
    for section, entities in by_section.items():
        path = os.path.join(args.root, "api", f"section_{section}.json")
        write_text(path, json.dumps({"version": data.get("version", "1.0"), "section": section, "entities": entities}, ensure_ascii=False, indent=2))

    # Methods-only index
    methods = [e for e in data.get("entities", []) if e.get("type") == "method"]
    if args.methods_compact:
        compact_methods = []
        for e in methods:
            e2 = dict(e)
            e2.pop("examples", None)
            e2.pop("errors", None)
            compact_methods.append(e2)
        methods = compact_methods
    write_text(
        os.path.join(args.root, "api", "methods.json"),
        json.dumps({"version": data.get("version", "1.0"), "entities": methods}, ensure_ascii=False, indent=2),
    )

    # Compact index without heavy fields
    compact = []
    for e in data.get("entities", []):
        compact.append(
            {
                "id": e.get("id"),
                "type": e.get("type"),
                "title": e.get("title"),
                "summary": e.get("summary", ""),
                "source_url": e.get("source_url"),
                "tags": e.get("tags", []),
                "meta": e.get("meta", {}),
            }
        )
    write_text(
        os.path.join(args.root, "api", "index_compact.json"),
        json.dumps({"version": data.get("version", "1.0"), "entities": compact}, ensure_ascii=False, indent=2),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
