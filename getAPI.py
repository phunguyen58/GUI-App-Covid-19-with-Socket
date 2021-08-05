import requests, json # can tai 
import schedule
import pandas as pd #can tai
from bs4 import BeautifulSoup #can tai
from unidecode import unidecode #can tai pip install unicode
import schedule
import time

global_url = "https://coronavirus-19-api.herokuapp.com/all"
all_country_url = "https://coronavirus-19-api.herokuapp.com/countries"
wiki_url = "https://vi.wikipedia.org/wiki/B%E1%BA%A3n_m%E1%BA%ABu:D%E1%BB%AF_li%E1%BB%87u_%C4%91%E1%BA%A1i_d%E1%BB%8Bch_COVID-19/S%E1%BB%91_ca_nhi%E1%BB%85m_theo_t%E1%BB%89nh_th%C3%A0nh_t%E1%BA%A1i_Vi%E1%BB%87t_Nam#cite_note-1"

def getDataFromGlobalURL():
    global_info = json.loads(requests.get(global_url).text)
    global_info_string = json.dumps(global_info, sort_keys=True)
    global_info_file = open('dataGlobal.json', 'w', encoding="utf-8")
    global_info_file.write(global_info_string)
    global_info_file.close()

def getDataFromAllCountryURL():
    all_country_info = json.loads(requests.get(all_country_url).text)
    all_country_info_string = json.dumps(all_country_info, sort_keys=True)
    all_country_info_file = open('dataAllCountry.json', 'w', encoding="utf-8")
    all_country_info_file.write(all_country_info_string)
    all_country_info_file.close()

def getDataFromWikiURL():
    response = requests.get(wiki_url)
    wiki_text = response.text
    soup = BeautifulSoup(wiki_text, 'html.parser')
    required_table = soup.find('table', attrs={'class':"wikitable"})
    header_tags = required_table.find_all('th')
    filtered_header_tags = [header_tag for header_tag in header_tags]
    headers = [header.text.strip() for header in header_tags]
    rows = {}
    rows['province'] = []
    data_rows = required_table.find_all('tr')

    for row in data_rows:
        value = row.find_all('td')
        beautified_value = [dp.text.strip() for dp in value]
        if len(beautified_value) < 6:
            continue
        rows['province'].append({
            'nameProvince': unidecode(beautified_value[0]), # chuyen tu tieng viet co dau thanh ko dau
            'cases': beautified_value[1],
            'inProgress': beautified_value[2],
            'another': beautified_value[3],
            'recovered': beautified_value[4],
            'deaths': beautified_value[5]
        })

    vietnam_info_string = json.dumps(rows)
    vietnam_info_file = open("dataVN.json", "w", encoding="utf-8")
    vietnam_info_file.write(vietnam_info_string)
    vietnam_info_file.close()

def getData():
    # t = time()
    # now_time = ctime(t)
    # print("Database updated at: ", now_time)
    print("Updated database!")
    getDataFromGlobalURL()
    getDataFromAllCountryURL()
    getDataFromWikiURL()
    

# schedule.every().hour.at(":00").do(geeks)
schedule.every().minute.at(":00").do(getData)

while True:
    schedule.run_pending()
    time.sleep(1)

#global information

# print(type(str(global_info)))
# print("Cases: " + str(global_info['cases']))
# print("Deaths: " + str(global_info['deaths']))
# print("Recovered: " + str(global_info['recovered']))


#country information

# country_name = input("Enter country name\n")
# print("Here is your info")
# j = 0
# for i in country_info:
#     if(country_name == country_info[j]['country']):
#         print("Country: ", country_info[j]['country'])
#         print("Cases: ", str(country_info[j]['cases']))
#         print("Cases today: ", country_info[j]['todayCases'])
#         print("Deaths: ", country_info[j]['deaths'])
#         print("Today deaths: ", country_info[j]['todayDeaths'])
#         print("Recovered: ", country_info[j]['recovered'])
#         print("Active: ",country_info[j]['active'])
#         print("Critical: ",country_info[j]['critical'])
#         print("Cases per one million: ", country_info[j]['casesPerOneMillion'])
#         print("Deaths per one million: ",country_info[j]['deathsPerOneMillion'])
#         print("Total test: ", country_info[j]['totalTests'])
#         print("Test per one million: ", country_info[j]['testsPerOneMillion'])
#     j+=1
#provinced in VN information





