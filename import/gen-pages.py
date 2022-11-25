#!/usr/bin/env python3
"""
Generate country pages from json link data
"""
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)
template = env.get_template("country.md.j2")

with open("countries.json") as f:
    data = json.load(f)

    for country in data:
        with open(f"../docs/countries/{country}.md", "w") as dest:
            dest.write(template.render(country=country, links=data[country]))

with open("other.json") as f:
    data = json.load(f)

    for country in data:
        with open(f"../docs/other/{country}.md", "w") as dest:
            dest.write(template.render(country=country, links=data[country]))
