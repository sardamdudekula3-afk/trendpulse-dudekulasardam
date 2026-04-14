import requests
import time
import json
import os
from datetime import datetime

# Categories and keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

headers = {"User-Agent": "TrendPulse/1.0"}

# Get top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url, headers=headers)

story_ids = response.json()[:500]

data = []

# Function to assign category
def get_category(title):
    title = title.lower()
    for cat, keywords in categories.items():
        for word in keywords:
            if word in title:
                return cat
    return "other"

# Fetch each story
for story_id in story_ids:
    try:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        res = requests.get(story_url, headers=headers)
        story = res.json()

        if story and "title" in story:
            item = {
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": get_category(story.get("title")),
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", ""),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            data.append(item)

        if len(data) >= 125:
            break

    except:
        print("Error fetching story", story_id)
        continue

# Create folder
os.makedirs("data", exist_ok=True)

# Save file
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print(f"Collected {len(data)} stories. Saved to {filename}")
