from email import header
import requests
import json

r = requests.Session()
commonHeaders = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language" : "vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Upgrade-Insecure-Requests" : "1",
    "Sec-Fetch-Dest" : "document",
    "Sec-Fetch-Mode" : "navigate",
    "Sec-Fetch-Site" : "none",
    "Sec-Fetch-User" : "?1",
    "Te" : "trailers",
    "Connection" : "close"
}
def getEvents():
    resp = r.get("https://ctftime.org/api/v1/events/?limit=3", headers=commonHeaders)
    events = json.loads(resp.text)
    details = []

    for event in events:
        detail = f"=== {event['title']} ===\n"
        detail += f"Organizers: {' - '.join([o['name'] for o in event['organizers']])}\n"
        detail += f"Site: {event['url']}\nStart: {event['start']}\nFinish: {event['finish']}\n"
        detail += "On-line" if event['onsite'] == False else "On-site"
        detail += f"\nFormat: {event['format']}\nRating weight: {event['weight']}\n"
        detail += f"Participants: {event['participants']}"
        detail += "\n"

        details.append(detail)
    return details


