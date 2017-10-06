from __future__ import print_function
import requests
import csv
import re
import threading
import time
import pandas as pd
import string

setList = ["vavender", "primula", "seashell", "Livelong", "forgetmenot",
           "kiwano", "durian", "Cherry", "Strawberry", "leaf",
           "Cup of tee", "stripes", "Hydrangea", "dahila", "dogwood", "anemone", "carnation", "portrait", "chamomile",
           "Christmas", "banner", "lotus", "apple flower", "lips", "myosotis", "clematis", "skull", "cornus", "lily",
           "Bluebell", "viola", "dahlia", "gift box", "fish", "psychotria", "Fritillaria", "sakura",
           "chrysanthemum", "amarillis", "succulentus", "magnolia", "crocuses", "vector", "camellia", "Tropical Hawaii leaves",
           "aster", "iris", "petrikovka", "Wedding", "leaves", "peony",
           "cherry", "Abstract", "aquilegia", "lavender", "fruit", "kiwi and avocado", "rose", "poppies", "hyacinth",
           "roses", "sunflower", "bow", "Mushrooms", "fuchsia", "peonies", "tulip",
           "Valentines Day", "love", "arrow", "kosmeya", "cotton", "poppy", "orchid", "butterfly", "elephant",
           "wild animal", "parrot", "rosa", "ladybug", "beetle", "bronzovka", "Vector", "Cat", "bird", "feather",
           "Orchid", "Abstruct", "Amarillis", "Anemone", "AppleFlower", "Aquilegia", "Bird", "Butterflies", "Camellia",
           "cannabis", "Carnation", "carnegiea", "CherryFlower", "Chrysanthemum", "Chubushnik", "Clematis",
           "Cornus", "Crocuses", "Dahila", "daisy", "dandelion", "Dogwood", "dragonfly", "Eustoma", "ExoticFlower",
           "Feather", "Fish", "Forgetmenot", "fresia", "Fuchsia", "Gaillardia", "hibiscus", "immortelle",
           "Iris", "Kosmeya", "Lavender", "Lily", "London", "Love", "Magnolia", "Malus", "Myosotis", "Narcissus",
           "Olive", "Orchids", "other", "Paintbrush", "Peony", "PhotoPromotion", "Poppy", "Primula",
           "Rose", "Sakura", "Sarracenia", "Succulentus", "cactus", "Tulip",
           "Viola", "Weigela"]

patter_frame = ["Hand drawn poster in watercolor with roses and flower on it",
                "Wildflower rose flower and bird",
                "Yellow marigold chrysanthemum petunia calendula rose flower frame",
                "Wildflower rose flower with birds",
                "Wildflower primula flower frame",
                "Wildflower crocuses promo sale web banner template",
                "Tropical Hawaii leaves palm tree and kiwano pattern",
                "Tropical Hawaii leaves palm tree, kiwi and avocado pattern",
                "Tropical Hawaii leaves palm tree and durian pattern",
                "Cherry healthy food pattern",
                "Exotic butterfly wild insect and roses pattern",
                "Cherry healthy food pattern",
                "Wildflower rosa flower pattern",
                "Wildflower rosa flower frame",
                "Cherry healthy food frame",
                "Wildflower crocuses promo sale web banner",
                "Wildflower tulip and  rose flowers",
                "Wildflower rose flower with bird colibri",
                "Yellow marigold chrysanthemum petunia calendula rose flower background frame",
                "Wildflower tulip flower and butterfly",
                "Wildflower rosa flower wreath",
                "Love handwrite with peony flower",
                "Relax hand writing on hibiscus rose flower",
                "Just for you hand writing on hibiscus rose flower",
                "Happy birthday hand writing on hibiscus rose flower",
                "Health hand writing on hibiscus rose flower background",
                "flower pattern",
                "tattoo concept with skull",
                "tattoo concept pattern",
                "wreath",
                "flower frame",
                "Abstract seamless pattern",
                "Tropical Hawaii leaves palm tree frame",
                "Tropical Hawaii leaves palm tree pattern",
                "Sky bird sparrow in a wildlife pattern",
                "Watercolor bird feather pattern",
                "Tropical Hawaii leaves palm tree and butterflies frame",
                "Happy Valentines Day love celebration frame",
                "Wildflower rose crocuses frame",
                "Tropical Hawaii leaves and flowers frame",
                "FB cover for social networks",
                "flower set",
                "flower heart",
                "flower splash",
                "Wildflower rose flower pattren",
                "Wildflower rose crocuses pattern",
                "Tropical Hawaii leaves and flowers pattern",
                "Tropical Hawaii leaves palm tree theme",
                "Wedding invitation",
                "Watercolor summer beach seashell tropical elements pattern",
                "Watercolor summer beach seashell tropical elements frame",
                "Exotic butterfly wild insect and feathers pattern"
                "Strawberry healthy food frame",
                "Strawberry healthy food pattern",
                "Tropical cactus leaves pattern",
                "Tropical cactus leaves frame",
                "Exotic durian healthy food pattern",
                "Exotic kiwano healthy food pattern",
                "Exotic zebra and elephant wild animals pattern",
                "Wildflower cherry flowers promo sale banner template",
                "Cat wild animal pattern",
                "Cat wild animal frame",
                "Strawberry healthy food frame",
                "Exotic butterfly wild insect and feathers pattern",
                "Exotic beetle bronzovka wild insect pattern"
                "Exotic elephant wild animal pattern",
                "Exotic kiwi and avocado healthy food pattern",
                "Exotic beetle bronzovka wild insect pattern",
                "flower banner",
                "promo sale banner template",
                "Exotic elephant wild animal pattern in a watercolor style",
                "promo sale web banner template",
                "ropical plants  pattern",
                "Tropical plants frame",
                "Exotic kivano healthy food pattern",
                "Exotic pitaya healthy food pattern",
                "Hand drawn poster",
                "Happy birthday card in watercolor illustration",
                "Watercolor heart with handwriting isolated",
                "Wildflower orpine flower in a watercolor style isolated",
                "Tropical flowers with butterflies framein",
                "Handmade card",
                "Painted wildflower flowers background pattern",
                "Wildflower flower bouquet in a watercolor style isolated",
                "Seamless watercolor flowers on a white background",
                "wreat",
                "Watercolor holiday colorful ribbons bow greeting illustration"
                "Exotic butterfly wild insect and tropical leaf pattern in a watercolor style",
                "Sky bird white macaw parrot pattern  in a wildlife by watercolor style",
                "Watercolor bird feather pattern from wing",
                "Sky bird white macaw parrot pattern  in a wildlife by watercolor style",
                "Watercolor bird feather pattern from wing",
                "Tropical Hawaii leaves pattern in a watercolor style",
                "Tropical Hawaii leaves palm tree pattern in a watercolor style",
                "Tropical Hawaii leaves pattern in a watercolor style",
                "Tropical Hawaii leaves palm tree and tropical flower pattern in a watercolor style",
                "Tropical Hawaii leaves palm tree and kiwano pattern in a watercolor style"
                "Tropical Hawaii leaves palm tree  and sea shell pattern in a watercolor style",
                "Tropical Hawaii leaves palm tree and durian pattern in a watercolor style",
                "Tropical Hawaii leaves palm tree, kiwi and avocado pattern in a watercolor style",
                "Wildflower rose flower pattern in a watercolor style isolated",
                "Watercolor holiday colorful ribbons pattern bow greeting",
                "Watercolor holiday colorful ribbons pattern bow greeting",
                "Exotic butterfly wild insect and tropical leaf pattern in a watercolor style",
                "Watercolor holiday coloful ribbon pattern bow greeting illustration",
                "Tropical Hawaii leaves palm tree  and sea shell pattern in a watercolor style",
                "Watercolor holiday colorful ribbon pattern bow greeting illustration",
                "Tropical Hawaii leaves palm tree  and sea shell pattern in a watercolor style",
                "Tropical Hawaii leaves palm tree and pitaya pattern in a watercolor style",
                "Tropical Hawaii leaves plants pattern  in a watercolor style",
                "Tropical Hawaii leaves plants pattern  in a watercolor style",
                "Watercolor holiday colorful ribbon pattern bow greeting illustration",
                "Tropical Hawaii leaves aloe tree pattern in a watercolor style",
                "Tropical Hawaii leaves aloe tree pattern in a watercolor style",
                "Wildflower rosa flower  pattern in a watercolor style",
                "Vector bird feather pattern from wing",
                "Hand drawn feather bird art pattern isolated on white background",
                "Wildflower rosa flower  pattern in a watercolor style",
                "Sky bird parrot pattern in a wildlife by watercolor style",
                "Wildflower rose flower  pattern in a watercolor style",
                "Sky bird parrot pattern in a wildlife by watercolor style",
                "Watercolor bird feather from wing pattern",
                "Wildflower rose pattern flower in a watercolor style isolated",
                "Tropical Hawaii leaves palm tree and butterflies pattern in a watercolor style isolated",
                "Sky bird white macaw parrot frame in a wildlife by watercolor style",
                "Watercolor bird feather frame from wing",
                "Sky bird white macaw parrot frame in a wildlife by watercolor style",
                "Tropical Hawaii leaves frame in a watercolor style",
                "Tropical Hawaii leaves plants frame  in a watercolor style",
                "Tropical Hawaii leaves aloe tree frame in a watercolor style",
                "Watercolor bird feather frame from wing",
                "Hibiscus rose flower background frame in watercolor drawing",
                "Yellow marigold rose flower background frame in watercolor drawing",
                "Hibiscus rose flower background frame in watercolor drawing",
                "banner"
                "Watercolor tattoo concept with skull element",
                ]


def getSetByTitle():
    dataFrameIN = pd.read_csv("../NewParsers/DF_TotalUplodedImages.csv")
    setsFile = open("Sets.csv", "w")
    wr = csv.writer(setsFile)
    heder = ["ID", "Set", "Title"]
    wr.writerow(heder)
    listTitle = dataFrameIN.Title
    listID = dataFrameIN.ID
    for id, title in zip(listID, listTitle):
        if type(title) == float:
            print(id, title)
        listALL = []
        list = []
        _set_ = ""
        for set in setList:
            if set in title:
                list.append(set)
        for token in patter_frame:
            if token in title:
                if "frame" in token and "pattern" in token:
                    _set_ = "pattern"
                elif "frame" in token:
                    _set_ = "frame"
                elif "pattern" in token:
                    _set_ = "pattern"
                elif "banner" in token:
                    _set_ = "frame"
                else:
                    _set_ = "frame"
                break
        if str(id) == "505699084" or str(id) == "483647827" or str(id) == "497764732" or str(id) == "505698898" or str(
                id) == "505699012" or str(id) == "495922915" or str(id) == "505699210" or str(id) == "505699219" or str(
            id) == "465449219" or str(id) == "485515453" or str(id) == "482079334" or str(id) == "654157573":
            _set_ = "frame"
        if str(id) == "519000031" or str(id) == "517372495" or str(id) == "479754829":
            _set_ = "pattern"
        if str(id) == "465403352":
            _set_ = "paint"
        if len(_set_) == 0:
            if len(list) == 1 and (list[0] == "roses" or list[0] == "roses" or list[0] == "rosa" or list[0] == "rose" or list[0] == "Rose"):
                _set_ = "rose"
            elif len(list) == 2 and list[0] == "bird" and list[1] == "feather":
                _set_ = "feather"
            elif len(list) == 2 and list[0] == "leaf" and list[1] == "butterfly":
                _set_ = "butterfly"
            elif len(list) == 2 and list[0] == "parrot" and list[1] == "bird":
                _set_ = "birds"
            elif "vector" in title or "Vector" in title:
                _set_ = "vector"
            elif "Happy Valentines Day love celebration arrow in a watercolor style isolated" in title or "Watercolor holiday ribbon on arrow bow greeting" in title:
                _set_ = "arrow"
            elif "Wildflower primula flower in a watercolor style isolated" in title:
                _set_ = "primula"
            elif "Wildflower rosa flower in a watercolor style isolated" in title:
                _set_ = "rosa"
            elif "Cherry healthy food in a watercolor style isolated" in title:
                _set_ = "cherry"
            elif "Abstract watercolor paper splash shapes isolated" in title:
                _set_ = "abstract"
            elif "leaf-beetle" in title:
                _set_ = "beetle"
            elif "Sky bird sparrow in a wildlife by watercolor style isolated" in title:
                _set_ = "bird"
            elif "Wildflower rose flower in a watercolor style isolated" in title:
                _set_ = "rose"
            elif "Happy Valentines Day love celebration in a watercolor style isolated" in title:
                _set_ = "love"
            elif "Watercolor bird feather from wing isolated" in title:
                _set_ = "feather"
            elif "Wildflower rose crocuses in a watercolor style isolated" in title:
                _set_ = "crocuses"
            elif "Tropical Hawaii leaves and flowers in a watercolor style isolated" in title:
                _set_ = "Tropical Hawaii leaves"
            elif "Wildflower lily flower in a watercolor style isolated" in title:
                _set_ = "lily"
            elif "Tropical Hawaii leaves" in title:
                _set_ = "Tropical Hawaii leaves"
            elif " Wildflower tulip flower in a watercolor style isolated" in title:
                _set_ = "tulip"
            elif "Wildflower daisy chamomile flower in a watercolor style isolated" in title:
                _set_ = "chamomile"
            elif "Wildflower chamomile flower leaf in a watercolor style isolated" in title:
                _set_ = "chamomile"
            elif "Wildflower viola leaves flower in a watercolor style isolated" in title:
                _set_ = "viola"
            elif "Tropical Hawaii leaves palm tree" in title or "Tropical plants  in a watercolor style isolated" in title:
                _set_ = "Tropical Hawaii leaves"
            elif "Wildflower myosotis arvensis flower in a watercolor style isolated" in title:
                _set_ = "myosotis"
            elif "Wildflower orchid flower leaf in a watercolor style isolated" in title:
                _set_ = "orchid"
            elif "portrait" in title:
                _set_ = "PhotoPromotion"
            elif "Wildflower vavender flower in a watercolor style isolated" in title:
                _set_ = "lavender"
            elif "Wildflower tulip flower in a watercolor style isolated" in title:
                _set_ = "tulip"
            elif "Wildflower iris flower leaf in a watercolor style isolated" in title:
                _set_ = "iris"
            elif "Wildflower tea rose flower in a watercolor style isolated" in title:
                _set_ = "rose"
            elif "Ribbons colorful set" in title:
                _set_ = "ribbon"
            elif "Watercolor summer beach seashell tropical elements" in title:
                _set_ = "seashell"
            elif "Wildflower poppy flower leaf in a watercolor style isolated" in title:
                _set_ = "poppy"
            elif "Cat wild animal in a watercolor style isolated" in title:
                _set_ = "Cat"
            elif "Exotic durian healthy food in a watercolor style isolated" in title:
                _set_ = "durian"
            elif "Exotic kiwano healthy food in a watercolor style isolated" in title:
                _set_ = "kiwi"
            elif "Tropical cactus leaves in a watercolor style isolated" in title:
                _set_ = "cactus"
            elif "Strawberry healthy food in a watercolor style isolated" in title:
                _set_ = "strawberry"
            elif "Wildflower orchid flower in a watercolor style isolated" in title:
                _set_ = "orchid"
            elif "Exotic beetle bronzovka wild insect in a watercolor style isolated" in title:
                _set_ = "beetle"
            elif "Wildflower roses flower in a watercolor style isolated" in title:
                _set_ = "rose"
            elif "Wildflower Blue aquilegia flower leaf in a watercolor style isolated" in title:
                _set_ = "aquilegia"
            elif "Wildflower Gaillardia flower leaf in a watercolor style isolated" in title:
                _set_ = "gaillardia"
            elif "Wildflower Peony flower in a watercolor style isolated" in title:
                _set_ = "peony"
            elif "Fb cover" in title:
                _set_ = "frame"
            elif len(list) == 1 and ("Abstract fractal" in title or "Abstract painting art" in title):
                _set_ = "abstract"
            elif len(list) == 1 and "bow" in title:
                _set_ = "ribbon"
            elif len(list) == 1 and "frame" in title:
                _set_ = "frame"
            elif len(list) == 1 and "pattern" in title:
                _set_ = "patter"
            elif len(list) == 0 and "Tropical Hawaii coco" in title:
                _set_ = "coco"
            elif len(list) == 0 and "Watercolor colorful texture illustration" in title:
                _set_ = "abstract"
            elif len(list) == 0 and "Exotic pitaya healthy food in a watercolor style isolated" in title:
                _set_ = "pitaya"
            elif len(list) == 0 and "Hand drawn botanical art isolated on white background" in title:
                _set_ = "vector"
            elif len(list) == 0 and "Exotic kiwi healthy food ispican a watercolor style isolated" in title:
                _set_ = "kiwi"
            elif len(list) == 0 and "Exotic avocado healthy food in a watercolor style isolated" in title:
                _set_ = "avocado"
            elif len(list) == 0 and "Watercolor sailing ship" in title or "Watercolor city" in title:
                _set_ = "paint"
            elif len(list) == 0 and "Wildflowers frame in a watercolor style isolated" in title:
                _set_ = "frame"
            elif len(list) == 0 and "spica" in title or "wheat" in title or "orpine" in title:
                _set_ = "wheat"
            elif len(list) == 0 and "Wildflowers frame" in title:
                _set_ = "frame"
            elif len(list) == 0 and "Exotic kiwi healthy food in a watercolor style isolated" in title:
                _set_ = "kiwi"
            elif len(list) == 1:
                _set_ = list[0]
            elif len(list) == 2 and list[0] == "leaf":
                _set_ = list[1]
            elif len(list) == 2 and list[0] == "elephant" and list[1] == "wild animal":
                _set_ = "elephant"
            elif len(list) == 2 and list[0] == "viola" and list[1] == "leaves":
                _set_ = "viola"
            elif len(list) == 2:
                _set_ = "frame"
            elif str(id) == "657462808" or str(id) == "658008202" or str(id) == "658008091" or str(id) == "658008091" or str(
                    id) == "657462907" or str(id) == "657461881" or str(id) == "657461953" or str(id) == "658007902" or str(
                id) == "658008091" or str(id) == "658007902" or str(id) == "657462808" or str(id) == "657462907" or str(
                id) == "658008091" or str(id) == "658007902" or str(id) == "658008091" or str(id) == "657461953" or str(
                id) == "657462916" or str(id) == "654157648" or str(id) == "657461788" or str(id) == "654157591" or str(
                id) == "699633562":
                _set_ = "anemone"
            elif str(id) == "658008277" or str(id) == "658008061" or str(id) == "657461035":
                _set_ = "aquilegia"
            elif str(id) == "480328699":
                _set_ = "gomphrena"
            elif str(id) == "657461926":
                _set_ = "cornus"
            elif str(id) == "594844835" or str(id) == "659664631" or str(id) == "655247827" or str(id) == "658008109":
                _set_ = "orchid"
            elif str(id) == "659664694" or str(id) == "662051989" or str(id) == "657461170":
                _set_ = "peony"
            elif str(id) == "657462001":
                _set_ = "poppy"
            elif len(list) == 0 and len(_set_) == 0:
                _set_ = "_NONE_TYPE_(Wildflower flower)"
        # if "Exotic kiwi healthy food in a xwatercolor style isolated" in title:
        #     print(id, "   ", _set_, "   ", list, "   ", title)
        listALL.extend([str(id), _set_, title])
        wr.writerow(listALL)

        # elif len(_set_) == 1:
        #     print(id, "   ", _set_, "   ", list, "   ", title)


def main():
    getSetByTitle()


main()
