#!/usr/bin/env python3
import os
import re
from datetime import datetime, timezone
from pathlib import Path

FEED_TITLE = "Asher's Area'"
FEED_ID = "https://asherpayn.uk/atom.xml"
FEED_AUTHOR = "Asher Payn"
FEED_URL = "https://asherpayn.uk"
POSTS_DIR = Path("posts")
OUTPUT = Path("atom.xml")

def parse_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}, text
    meta = {}
    for line in match.group(1).splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            meta[k.strip()] = v.strip()
    body = text[match.end():].strip()
    return meta, body

def atom_date(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def escape_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

posts = []
for f in sorted(POSTS_DIR.glob("*.md"), reverse=True):
    text = f.read_text()
    meta, body = parse_frontmatter(text)
    if "title" in meta and "date" in meta and "url" in meta:
        posts.append(meta)

updated = atom_date(posts[0]["date"]) if posts else datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

entries = ""
for p in posts:
    summary = escape_xml(p.get("summary", ""))
    title = escape_xml(p["title"])
    url = escape_xml(p["url"])
    date = atom_date(p["date"])
    entries += f"""  <entry>
    <title>{title}</title>
    <link href="{url}"/>
    <id>{url}</id>
    <updated>{date}</updated>
    <summary>{summary}</summary>
    <author><name>{FEED_AUTHOR}</name></author>
    <icon>{FEED_URL}/icon.png</icon>
    <logo>{FEED_URL}/icon.png</logo>
  </entry>\n"""

feed = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>{escape_xml(FEED_TITLE)}</title>
  <link href="{FEED_URL}"/>
  <link rel="self" href="{FEED_ID}"/>
  <id>{FEED_ID}</id>
  <updated>{updated}</updated>
  <author><name>{FEED_AUTHOR}</name></author>
{entries}</feed>"""

OUTPUT.write_text(feed)
print(f"Generated {OUTPUT} with {len(posts)} entries.")
