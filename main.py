import time

from bs4 import BeautifulSoup
import requests
import pandas as pd
import feedparser
from classs import news
import json

pd.set_option('display.max_colwidth', 500)
api_key = "AIzaSyAKY_4kNJ0xHBgVCE6k9ZgSX-njXno1BTQ"
API_URL = "https://api-inference.huggingface.co/models/CAMeL-Lab/bert-base-arabic-camelbert-msa-ner"
headers = {"Authorization": "Bearer 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"}


def main():
    the_word = ["الأعاصير", "إطلاق نار", "إصابة", "حوادث", "زلازل", "حريق", "إرهاب", "الجرائم", "بحادثي", "وفاتان",
                "حرب","إصابات","وفاة"]
    Feed = feedparser.parse('https://www.royanews.tv/rss')
    # print(Feed)
    DataList = []
    ImportnatnList = []
    #
    # for i in Feed.entries:
    #     t = str(i).split("author")[3]
    #     t = t.split("title")[2]
    #     links = t.split("base")[1]
    #     links = links.split("href")[1]
    #     links = links.split("}")[0]
    #     links = links.split("'")[2]
    #     title = t.split("value")[1]
    #     title = title.split("}")[0]
    #
    #     # title=title.split(":")[1]
    #
    #     title = title.split("'")[2]
    #
    #     DataList.append(news(title, links))

    index = 0
    for i in Feed.entries:
        t = str(i).split("author")[3]
        t = t.split("title")[2]
        links = t.split("base")[1]
        links = links.split("href")[1]
        links = links.split("}")[0]
        links = links.split("'")[2]
        title = t.split("value")[1]
        title = title.split("}")[0]
        # title=title.split(":")[1]
        title = title.split("'")[2]
        DataList.append(news(title, links))
        index + 1

    for i in DataList:
        print(i.GetTitle() + "\n")

    searchcount = 0
    for i in DataList:
        for word in the_word:
            if i.GetTitle().__contains__(word):
                important_link = i.GetLink()
                # print("the title " + i.GetTitle() + " important link " + important_link)
                ImportnatnList.append(news(i.GetTitle(), i.GetLink()))
                searchcount = searchcount + 1

    if searchcount == 0:
        print("no news found")
    else:
        extract(ImportnatnList)

    for i in ImportnatnList:
        location=i.Getlocation()
        if location!="":
            location=location.split(',')
            location=list(dict.fromkeys(location))
            location.remove('')
            print(str(location))

            # print("after "+str(location))

            for l in location:
                print("geting location for "+l)
                print(get_boundary_coordinates(l))


def extract(ls):
    for i in ls:
        print(i.GetTitle() + " \n")
        url = i.GetLink()

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # find all sections in the HTML
        sections = soup.find_all("section")

        # check if there are at least two sections
        if len(sections) >= 4:
            second_section = sections[4]
            second_section_contents = second_section.get_text()
            second_section_contents = "\n".join(
                [line.strip() for line in second_section_contents.split("\n") if line.strip()])
            # print(second_section_contents)
            i.Setdescription(second_section_contents)
        else:
            print("There are not enough sections on the webpage")
    ExtractLocation(ls)


def extract_static(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # find all sections in the HTML
    sections = soup.find_all("div", {"class": "article"})

    # check if there are at least two sections

    for data in sections:
        second_section_contents = data.get_text()
        second_section_contents = "\n".join(
            [line.strip() for line in second_section_contents.split("\n") if line.strip()])
        print("article :" + second_section_contents + "\n")


def get_boundary_coordinates(place_name):
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key={api_key}"
    response = requests.get(geocode_url)
    response_json = response.json()
    results = response_json["results"]
    if len(results) == 0:
        return None
    result = results[0]
    geometry = result["geometry"]
    bounds = geometry.get("bounds")
    if bounds is None:
        viewport = geometry["viewport"]
        southwest = viewport["southwest"]
        northeast = viewport["northeast"]
        boundary_coordinates = [(southwest["lat"], southwest["lng"]), (northeast["lat"], northeast["lng"])]
    else:
        southwest = bounds["southwest"]
        northeast = bounds["northeast"]
        boundary_coordinates = [(southwest["lat"], southwest["lng"]), (northeast["lat"], northeast["lng"]),
                                (northeast["lat"], southwest["lng"]), (southwest["lat"], northeast["lng"])]
    return boundary_coordinates


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    estimatedTime = 0
    if 'estimated_time' in response:
        estimatedTime = response['estimated_time']
        print(estimatedTime)
    if estimatedTime > 0:
        print("sleeping "+estimatedTime)
        time.sleep(estimatedTime)
        response = requests.post(API_URL, headers=headers, json=payload)

    return response.json()


def ExtractLocation(ls):
    theLocation=""
    for i in ls:
        if i.Getdescription() != '':
            response = query(i.Getdescription())
            for index in range(len(response)):
                if response[index]['entity_group']=='LOC':
                    theLocation=theLocation+response[index]['word']+","
        if theLocation != "":
            i.SetLocation(theLocation)
            i.SettimeStamp(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))
        theLocation=""

    for i in ls:
        # print(i.getIntoList([965156.615561,6546465.15165,154.6516,1651.123]))
        print(i)

if __name__ == '__main__':
    main()
    # extract_static(input("url:"))
