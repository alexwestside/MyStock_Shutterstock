from __future__ import print_function
import requests
import csv
import re
import threading
import time
import pandas as pd

setList = ["FB cover", "Hand drawn poster", "vavender", "primula", "seashell", "texture illustration", "healthy food",
           "kiwano", "durian", "Cherry", "Strawberry", "Wildflowers frame", "flower frame", "flower pattern", "leaf",
           "Cup of tee", "stripes", "Hydrangea", "dahila", "dogwood", "anemone", "carnation", "portrait", "chamomile",
           "Christmas", "banner", "lotus", "apple flower", "lips", "myosotis", "clematis", "skull", "cornus", "lily",
           "Bluebell", "viola", "dahlia", "gift box", "fish", "psychotria", "Fritillaria", "sakura",
           "chrysanthemum", "amarillis", "succulentus", "magnolia", "crocuses", "vector", "camellia",
           "Tropical Hawaii coco", "Tropical Hawaii leaves", "aster",
           "Tropical plants", "iris", "petrikovka", "Wedding", "leaves", "Tropical Hawaii leaves aloe", "peony",
           "cherry", "Abstract", "aquilegia", "lavender", "fruit", "kiwi and avocado", "rose", "poppies", "hyacinth",
           "roses", "sunflower", "lavender", "bow", "decoration", "Mushrooms", "fuchsia", "peonies", "tulip",
           "Valentines Day", "love", "arrow", "kosmeya", "cotton", "poppy", "orchid", "butterfly", "elephant",
           "wild animal", "parrot", "rosa", "ladybug", "beetle", "bronzovka", "Vector", "Cat", "bird", "feather",
           "Orchid", "Abstruct", "Amarillis", "Anemone", "AppleFlower", "Aquilegia", "Bird", "Butterflies", "Camellia",
           "cannabis", "Carnation", "carnegiea", "CherryFlower", "Chrysanthemum", "Chubushnik", "Clematis",
           "Cornus", "Crocuses", "Dahila", "daisy", "dandelion", "Dogwood", "dragonfly", "Eustoma", "ExoticFlower",
           "Feather", "Fish", "Forgetmenot", "fresia", "Fuchsia", "Gaillardia", "hibiscus", "immortelle",
           "Iris", "Kosmeya", "Lavender", "Lily", "London", "Love", "Magnolia", "Malus", "Myosotis", "Narcissus",
           "Olive", "Orchids", "other", "Paintbrush", "Peony", "PhotoPromotion", "Poppy", "Primula",
           "Rose", "Sakura", "Sarracenia", "Succulentus", "cactus", "Tropical Hawaii leaves palm tree", "Tulip",
           "Viola", "Weigela"]


def getSetByTitle():
    dataFrameIN = pd.read_csv("../UploadedImages/DF_TotalUplodedImages.csv")
    listTitle = dataFrameIN.Title
    listID = dataFrameIN.ID
    for id, title in zip(listID, listTitle):
        if type(title) == float:
            print(id, title)
        list = []
        for set in setList:
            if set in title:
                list.append(set)
        if "feather" in str(list):
            print(id, " | ", list, " | ", title)
        if any("feather" in s for s in set):
            print(id, " | ", list, " | ", title)


def main():
    getSetByTitle()


main()
