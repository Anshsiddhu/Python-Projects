from bs4 import BeautifulSoup
import requests
url"http://oceanofgames.com/?s=cyber"
response = requests.get(url)
<Response [200]>
data = response.text
soup = BeautifulSoup(data, 'html.parser')
titles = soup.find_all("a", {"class":"result-tittle"})
for title in titles
    print(title.text)

