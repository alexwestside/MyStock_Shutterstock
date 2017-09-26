

setList = ['Abstruct', 'Amarillis', 'Anemone', 'AppleFlower', 'Aquilegia', 'Bird', 'Butterflies', 'Camellia',
           'cannabis', 'Carnation', 'carnegiea', 'CherryFlower', 'Chrysanthemum', 'Chubushnik', 'Clematis',
           'Cornus', 'Crocuses', 'Dahila', 'daisy', 'dandelion', 'Dogwood', 'dragonfly', 'Eustoma', 'ExoticFlower',
           'Feather', 'Fish', 'Forgetmenot', 'frame', 'fresia', 'Fuchsia', 'Gaillardia', 'hibiscus', 'immortelle',
           'Iris', 'Kosmeya', 'Lavender', 'Lily', 'London', 'Love', 'Magnolia', 'Malus', 'Myosotis', 'Narcissus',
           'Olive', 'Orchids', 'other', 'Paintbrush', 'pattern', 'Peony', 'PhotoPromotion', 'Poppy', 'Primula',
           'Rose', 'Sakura', 'Sarracenia', 'Succulentus', 'cactus', 'Tropical Hawaii leaves palm tree', 'Tulip',
           'Viola', 'Weigela']

# https://submit.shutterstock.com/edit_media.mhtml?type=photos&approved=1&id=508655170

# from BeautifulSoup import BeautifulSoup
# from lxml.html import parse
#
link = '../html_txt/parseByID.txt'
#
# soup = BeautifulSoup(link)
# line = soup.

set = None

with open(link, mode='r') as file:
    lines = file.readlines()
    for line in lines:
        if line.find('textarea name=\"description\"') > 0:
            totalInfo = line.split('>')[1].split('<')[0]
            for _set in setList:
                if _set in totalInfo:
                    set = _set
                elif _set == 'pattern' and _set == 'frame':
                    pass
            print(set)
