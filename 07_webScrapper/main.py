from requests import get
from bs4 import BeautifulSoup

keyword = str(input("Input search Keyword : "))
weworkremotelyURL = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"

response = get(weworkremotelyURL)
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all("li", class_="feature"))
