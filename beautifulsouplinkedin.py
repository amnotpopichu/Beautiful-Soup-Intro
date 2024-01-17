import csv
#python3 -m pip installrequests
#python3 -m pip installhtml5lib
#python3 -m pip install bs4
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
#example with realpythons fake website 
URL = "https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&currentJobId=3807908471&position=2&pageNum=0"
page = requests.get(url=URL, headers=headers) 
data=page.content
soup = BeautifulSoup(page.content, "html.parser")

#print(soup.prettify())
#outputs "prettified data"
prettified = soup.prettify()
#print(prettified)
results = soup.find(id="main-content")


job_elements = results.find_all("li")#, class_="jobs-search__results-list")
#print(job_elements)
def nonecheck(a):
    if a is not None:
        return a.text.strip()

    return "not found"
file = open("test.csv", "w+")
for job_element in job_elements:
    title_element = job_element.find("h3", class_="base-search-card__title")
    company_element = job_element.find("h4", class_="base-search-card__subtitle")
    linkel = company_element.find("a")
    location_element = job_element.find("span", class_="job-search-card__location")
    file.write(str(nonecheck(title_element)))
    file.write(str(nonecheck(linkel)))
    file.write(str(nonecheck(location_element)))
    file.write("\n")
    '''
    print(nonecheck(title_element))
    print(nonecheck(linkel))
    print(nonecheck(location_element))
    print()
    
'''
file.close()