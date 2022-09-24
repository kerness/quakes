import requests
from bs4 import BeautifulSoup
import re
import json


url = "https://grss.gig.eu/mapa-wstrzasow/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


for script in soup.find_all("script"):
    pattern = r"var map5"
    if m := re.search(pattern, script.text, re.M | re.S):
        var_map5 = script
        break

json_string = var_map5.text[63:-24]


json_object = json.loads(json_string)


entries_to_remove = (
    "map_options",
    "listing",
    "map_property",
    "shapes",
    "filters",
    "marker_category_icons",
)
for entry in entries_to_remove:
    json_object.pop(entry, None)


# usunąc inne kategorie niż wstrząsy

# with open("map.json", "w") as outfile:
#     json.dump(json_object, outfile)


places = json_object["places"]


newlist1 = [
    x
    for x in places
    if x["categories"][0]["name"]
    not in ["Stanowiska pr\u0119dko\u015bciowe", "Stanowiska przyspieszeniowe"]
]


s_przyspieszeniowe = 0
s_predkosciowe = 0


for place in newlist1:

    if place["categories"][0]["name"] == "Stanowiska pr\u0119dko\u015bciowe":
        s_predkosciowe = s_predkosciowe + 1

    elif place["categories"][0]["name"] == "Stanowiska przyspieszeniowe":
        s_przyspieszeniowe = s_przyspieszeniowe + 1


## teraz już są tam tylko wstrząsy. teraz zrobić tak, żeby było tylko potrzebne info
# więc pozostawiam TYLKO title i location

quakes = [
    {
        "date": x["title"].split(" ")[0],
        "time": x["title"].split(" ")[1],
        "lat": x["location"]["lat"],
        "lng": x["location"]["lng"],
        "mag": x["location"]["extra_fields"]["magnituda"],
    }
    for x in newlist1
]

# teraz jeszcze trzeba przekonwertować to na geojson

geojs = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "date": q["date"],
                "time": q["time"],
                "mag": q["mag"],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [float(q["lng"]), float(q["lat"])],
            },
        }
        for q in quakes
    ],
}

with open("grss.geojson", "w") as outfile:
    json.dump(geojs, outfile)
