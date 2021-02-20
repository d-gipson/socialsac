import requests
### pip install requests

from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup
### pip install bs4




###homelessshelterdirectory.org
URL1 = 'https://www.homelessshelterdirectory.org/cgi-bin/id/city.cgi?city=Sacramento&state=CA'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page1 = requests.get(URL1, verify=True)

###storing HTML content into another variable
page1_html = page1.read()

###closing previous connection for security
page1.close()

###parse html, then store in new variable
soup1 = BeautifulSoup(page1_html, 'html.parser')

###grab the needed HTML data 
data1 = soup1.find_all("div",{"class":"item_content"})


#python_shelters = results.find_all('h4', string='shelter')



###sacramentofoodbank.org
URL2 = 'https://www.sacramentofoodbank.org/'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page2 = requests.get(URL2, verify=True)

###storing HTML content into another variable
page2_html = page2.read()

###closing previous connection for security
page2.close()

###parse html, then store in new variable
soup2 = BeautifulSoup(page2_html, 'html.parser')



###shra.org
URL3 = 'https://www.shra.org/emergency-housing-and-other-homeless-resources/'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page3 = requests.get(URL3, verify=True)

###storing HTML content into another variable
page3_html = page3.read()

###closing previous connection for security
page3.close()

###parse html, then store in new variable
soup3 = BeautifulSoup(page3_html, 'html.parser')



###211sacramento.org
URL4 = 'https://www.211sacramento.org/211/online-database/categories/homeless/'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page4 = requests.get(URL4, verify=True)

###storing HTML content into another variable
page4_html = page4.read()

###closing previous connection for security
page4.close()

###parse html, then store in new variable
soup4 = BeautifulSoup(page4_html, 'html.parser')



###namisacramento.org
URL5 = 'https://namisacramento.org/resources/homeless-low-income-resources/'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page5 = requests.get(URL5, verify=True)

###storing HTML content into another variable
page5_html = page5.read()

###closing previous connection for security
page5.close()

###parse html, then store in new variable
soup5 = BeautifulSoup(page5_html, 'html.parser')



###cityofsacramento.org
URL6 = 'https://www.cityofsacramento.org/City-Manager/Divisions-Programs/Office-of-Community-Response/Homeless-Coordination/Emergency-Services'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page6 = requests.get(URL6, verify=True)

###storing HTML content into another variable
page6_html = page6.read()

###closing previous connection for security
page6.close()

###parse html, then store in new variable
soup6 = BeautifulSoup(page6_html, 'html.parser')



###shelterlist.com
URL7 = 'https://www.shelterlist.com/city/ca-sacramento'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page7 = requests.get(URL7, verify=True)

###storing HTML content into another variable
page7_html = page7.read()

###closing previous connection for security
page7.close()

###parse html, then store in new variable
soup7 = BeautifulSoup(page7_html, 'html.parser')



###nextmovesacramento.org
URL8 = 'https://www.nextmovesacramento.org/'

###initiating connection, verifying site is SSL/TLS secured, then downloading HTML
page8 = requests.get(URL8, verify=True)

###storing HTML content into another variable
page8_html = page8.read()

###closing previous connection for security
page8.close()

###parse html, then store in new variable
soup8 = BeautifulSoup(page8_html, 'html.parser')