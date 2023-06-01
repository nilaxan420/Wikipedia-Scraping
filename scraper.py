import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_physics",
    )

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find(id="firstHeading")
print(title.contents)

allUnsolvedProblems = soup.find_all('span', {'class': 'mw-headline'})

def returnTitles():
    unsolved_problems_titles = []

    for line in allUnsolvedProblems:
        unsolved_problems_titles.append(line.text)
    
    return unsolved_problems_titles

# for title in unsolved_problems_titles:
#     print(title)

