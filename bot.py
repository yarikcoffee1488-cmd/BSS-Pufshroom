import os
import requests
import time
from datetime import datetime, timezone, timedelta

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

sent = set()

while True:
    now = datetime.now(timezone.utc) + timedelta(hours=2)

    if now.minute in (15, 45):
        key = now.strftime("%Y-%m-%d %H:%M")

        if key not in sent:
            requests.post(WEBHOOK, json={
                "content": "@everyone 🍄 PUFFSHROOMS TIME!\nГрибы в Bee Swarm Simulator должны появиться!"
            })
            sent.add(key)

    time.sleep(20)
