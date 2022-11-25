Tools to import data from traceroute.org

## parser

[parse-traceroute.py](parse-traceroute.py) fetches traceroute.org website and outputs
json data with links by country

## page generator

[gen-pages.py](gen-pages.py) takes a [links.json](links.json) file as input
and from a [template](country.md.j2) generates a file per country in [../docs](../docs)
directory
