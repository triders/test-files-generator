"""
Script to generate JSON document with random texts from Wikipedia,
ready to be imported into Lokalise. Keys are generated from paragraphs
and typically have lengths up to 1000 characters.
Dependencies:
- aiohttp==3.8.1
- beautifulsoup4==4.11.1
Usage (from project root):
$ python scripts/generate_lokalise_json.py --keys 100 --out example.json
$ python scripts/generate_lokalise_json.py --keys 100 --out example-ru.json --lang ru
"""

import asyncio
import json
import random
from argparse import ArgumentParser
from typing import cast

import aiohttp
from bs4 import BeautifulSoup, Tag


async def get_keys_from_wiki(lang_code: str) -> dict[str, str]:
    async with aiohttp.ClientSession() as session:
        url = f"https://{lang_code}.wikipedia.org/wiki/Special:Random"
        print(f"Fetching {url}...")
        resp = await session.get(url, verify_ssl=False)
        bs = BeautifulSoup(await resp.text(), "html.parser")

    result: dict[str, str] = {}

    content_el = bs.find(id="mw-content-text")
    for paragraph in content_el.find_all("p"):
        paragraph = cast(Tag, paragraph)
        text = paragraph.getText(" ", strip=True)
        if len(text) < 5:
            continue
        text_id = "-".join(random.choices(text.split(), k=5))
        result[text_id] = text

    return result


async def main(key_count: int, output: str, lang_code: str):
    result: dict[str, str] = {}
    while len(result) < key_count:
        result.update(await get_keys_from_wiki(lang_code))
        print(f"{len(result)} / {key_count} keys")

    print("Discarding extra keys...")
    while len(result) > key_count:
        result.pop(random.choice(list(result.keys())))

    text_lengths = [len(t) for t in result.values()]
    print(f"Shortest key: {min(text_lengths)} characters")
    print(f"Longest key: {max(text_lengths)} characters")
    with open(output, "w") as f:
        json.dump(result, f)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--keys", required=True, type=int, help="Number of keys to fetch")
    parser.add_argument("--out", required=True, help="Output file path")
    parser.add_argument(
        "--lang",
        default="en",
        help="Wikipedia language subdomain (e.g. 'lv' to fetch data in Latvian from lv.wikipedia.org)"
    )
    args = parser.parse_args()
    asyncio.run(main(args.keys, args.out, args.lang))