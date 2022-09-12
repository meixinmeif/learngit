import requests
import xmltodict
from requests import Response


def test_more_response():
    res = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    r = more_agreement(res)
    print(r)
    assert isinstance(r, dict)


def more_agreement(response: Response):
    res_data = response.text
    if res_data.startswith("<?xml"):
        final_dict = xmltodict.parse(res_data)

    elif res_data.startswith("!DOCTYPE html"):
        final_dict = 'html'

    else:
        final_dict = response.json()

    return final_dict


