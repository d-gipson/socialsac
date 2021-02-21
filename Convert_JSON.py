import requests, json

from urllib.request import urlopen

from bs4 import BeautifulSoup

from lxml.html import fromstring, tostring, etree

from io import StringIO


def shelterlist():
   
    ###define site to get HTML data from
    URL = 'https://www.shelterlist.com/city/ca-sacramento'

    ###get HTML data
    GET = urlopen(URL)

    ###store HTML data
    page_html = GET.read()
    
    ###close connection
    GET.close()

    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')
    
    ###finding exact data
    data = page_soup.find("div",{"class":"listings"})
    
    data_dictionary = {}
    
     #stripped_data = []
    #for line in data:
    #    line.strip()
    #    print(type(line))
    #    stripped_data.extend(line)       
    #return stripped_data
    #data = stripped_data.read().decode('utf-8')
    #parser = etree.HTMLParser()
    #data = etree.parse(StringIO(data), parser)

    for i in data:
        street_address = i.find("div",{"class":"street"})
        cityState = i.find("div",{"class":"cityState"})
        phone = i.find("div",{"class":"phone"})
        data_dictionary = {street_address, cityState, phone}
        print(data_dictionary)

    ###define dictionary to convert to json
    #convert_data = []

    ###for loop 
    #for i in data:
     #   entry = {'title': i.find("h3").get_text(), 
      #  'details': i.find("address class"{"class":"listingaddress"})}
       # convert_data.append(entry)

    #jsonD = json.dumps(data.text)
    #return jsonD
    
    #print(json.dumps(conver_data))

    
    #clean_text = tostring(fromstring(data), pretty_print=pretty_print)
    #for line in clean_text
    
    #return clean_text

print(shelterlist())

"""
def sacramentofoodbank():

    ###define site to get HTML data from
    URL = 'https://www.sacramentofoodbank.org/location'

    ###get HTML data
    GET = urlopen(URL)

    ###store HTML data
    page_html = GET.read()

    ###close connection
    GET.close()

    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')
    
    ###finding exact data
    data1 = page_soup.find("div", attrs={"id":"block-fdc6c3e945144062a7ca"})

    jsonD1 = json.dumps(data1.text)
   
    ###finding exact data
    data2 = page_soup.find("div", attrs={"id":"block-85b5e7e83335788fa163"})
   
    jsonD2 = json.dumps(data2.text)

    return jsonD1, jsonD2
    
    

print(sacramentofoodbank())

def homelessshelterdirectory():
    
    ###define site to get HTML data from
    URL = 'https://www.homelessshelterdirectory.org/cgi-bin/id/city.cgi?city=Sacramento&state=CA'

    ###get HTML data
    GET = urlopen(URL)
    
    ###store HTML data
    page_html = GET.read()

    ###close connection
    GET.close()

    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')

    ###variable to help parse data hidden within links
    links = [a['href'] for a in page_soup.find_all('a', href=True, attrs={"class": "btn btn_red"})]

    ###creating a variable to store only links to desired data
    data_details = len(links)

    ###printing only valid links
    for i in range(1, data_details):
        
        print(links[i])
        
        ###passing valid links to urlopen
        more_info = urlopen(links[i])
        
        ###storing html from valid links 
        info_html = more_info.read()
        
        ###closing connection
        more_info.close()
        
        ###parsing the extra HTML info
        more_soup = BeautifulSoup(info_html, 'html.parser')
        
        ###storing desired data in a new variable
        more_data = more_soup.find("div",{"class":"col col_6_of_12"})

        ###convert more_data into json 
        jsonD_more_data = json.dumps(more_data.text)

        ###grabbing names of all organizations offering services
        names_soup = BeautifulSoup(info_html, 'html.parser')
        names = names_soup.find("div",{"class":"col col_9_of_12"})
        
        ###convert names into json
        jsonD_names = json.dumps(names.text)

        return jsonD_more_data, jsonD_names

        print(names.h3.text)
        print(more_data.h4.text)
        print(more_data.p.text)        

homelessshelterdirectory()

def cityofsacramento():
    
    ###define site to get HTML data from
    URL = 'https://www.cityofsacramento.org/City-Manager/Divisions-Programs/Office-of-Community-Response/Homeless-Coordination/Emergency-Services'

    ###get HTML data
    GET = urlopen(URL)

    ###store HTML data
    page_html = GET.read()

    ###close connection
    GET.close()
    
    ###parse HTML data
    page_soup = BeautifulSoup(page_html, 'html.parser')

    ###finding exact data
    data = page_soup.find_all("p", limit=38)

    ###convert data into json 
    jsonD = json.dumps(data.text)
    return jsonD
    ###finding number of useful data tags
    p_tags = len(data)

    ###for loop to iterate desired data only 
    for i in range(1, p_tags):
        print (data[i].text)

cityofsacramento()
"""