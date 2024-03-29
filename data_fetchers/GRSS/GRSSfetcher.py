import requests
from bs4 import BeautifulSoup
import re
import json
from pathlib import Path
import datetime
import hashlib

# for testing in developoment
try:
    from quakes_api.settings import DATA_DIR
except ModuleNotFoundError:
    DATA_DIR = "../../data"


def create_timestamp(date, time=""):
    """
    Converts date and time string to UNIX timestamp
    The date is like: "2010/01/07"
    The time is like: "16:19:00.00"
    """
    # from datetime import datetime
    # from calendar import timegm

    # time = time.split(".")[0]
    # dt_string = date + " " + time
    # dt = datetime.strptime(dt_string, "%Y/%m/%d %H:%M:%S")
    # timestamp = timegm(dt.timetuple())

    date = str(date).replace("/", "-")
    # EDITED: remove time from date!
    # time = str(time).split(".")[0]

    # return date + " " + time
    return date


EXPORT_PATH = Path(DATA_DIR, "GRSS")
# create dir
EXPORT_PATH.mkdir(parents=True, exist_ok=True)


class GRSSFetcher:
    def __init__(self):
        self.URL = "https://grss.gig.eu/mapa-wstrzasow/"
        self.page = requests.get(self.URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.quakes = self.fetchData()

    def fetchData(self):
        for script in self.soup.find_all("script"):
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

        # teraz już są tam tylko wstrząsy. teraz zrobić tak, żeby było tylko potrzebne info
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

        return quakes

    def exportData(self):
        """
        Writes data to geojson file.
        """

        # teraz jeszcze trzeba przekonwertować to na geojson

        geojs = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        # "date": q["date"],
                        # "time": q["time"],
                        # "precise_time": q["date"] + q["time"],
                        "unique_id": hashlib.md5(
                            bytes(q["date"] + q["time"], encoding="utf-8")
                        ).hexdigest(),
                        "date": create_timestamp(q["date"], q["time"]),
                        "mag": q["mag"],
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(q["lng"]), float(q["lat"])],
                    },
                }
                for q in self.quakes
            ],
        }
        # df = self.fetchData()
        identifier = str(datetime.datetime.now()).replace(" ", "-")
        name = ""
        path = Path(EXPORT_PATH / f"GRSS_{identifier}_{name}.geojson")

        with open(path, "w") as outfile:
            json.dump(geojs, outfile)

        return path
