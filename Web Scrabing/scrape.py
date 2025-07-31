import requests
from bs4 import BeautifulSoup

url = "https://wuzzuf.net/search/jobs/?q=machine%20learning"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')
jobs = soup.find_all('div', class_='css-1gatmva')

for job in jobs[:5]:
    title = job.find('h2', class_='css-m604qf').text.strip()
    company = job.find('a', class_='css-17s97q8').text.strip()
    location = job.find('span', class_='css-5wys0k').text.strip()
    details = job.find('div', class_='css-y4udm8').text.strip()

    print(f"""
Job Title       : {title}
Company Name    : {company}
Location        : {location}
Details         : {details}
    """)
    print("=" * 60)