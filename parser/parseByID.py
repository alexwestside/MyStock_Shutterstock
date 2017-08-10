



setList = []




# https://submit.shutterstock.com/edit_media.mhtml?type=photos&approved=1&id=508655170

# from BeautifulSoup import BeautifulSoup
# from lxml.html import parse
#
link = '../html_txt/parseByID.txt'
#
# soup = BeautifulSoup(link)
# line = soup.


with open(link, mode='r') as file:
    lines = file.readlines()
    for line in lines:
        if line.find('textarea name=\"description\"') > 0:
            totalInfo = line.split('>')[1].split('<')[0]
            print('Ok')

