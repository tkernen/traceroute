"""
Parse traceroute.org and return json with links by country
"""
import urllib.request
from lxml import html, etree  # type: ignore[import]
import xml.etree.ElementTree as ET
import json
from typing import Dict, List

with urllib.request.urlopen("http://www.traceroute.org") as f:
    # with open("traceroute.html", encoding='utf-8') as f:
    htmldoc = html.fromstring(f.read())
root = ET.fromstring(etree.tostring(htmldoc))

countries = [x.text for x in root.findall("./body//table")[0].findall(".//td/a/span")]

links: Dict[str, List[Dict[str, str]]] = {}

started = 0
country = None
for x in root.findall("./body/"):
    # when to start looking for countries
    if started == 0 and x.tag == "hr":
        started = 1
        country = None
    # that comes prior to a country
    if started and x.tag == "h3":
        if x[0].tag == "a":
            country = x[0].attrib['name']
            links[country] = []
    # all links in a country
    if country and x.tag == "ul":
        for link in x.findall("./li/a"):
            if link.text and link.attrib['href']:
                links[country].append({"text": link.text, "url": link.attrib['href']})

print(json.dumps(links, indent=2))
