#python3 -m pip installrequests
#python3 -m pip installhtml5lib
#python3 -m pip install bs4
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
#example with realpythons fake website 
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(url=URL, headers=headers) 
data=page.content
soup = BeautifulSoup(page.content, "html.parser")

#print(soup.prettify())
#outputs "prettified data"
prettified = soup.prettify()
#print(prettified)
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
