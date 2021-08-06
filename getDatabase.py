import json

def readDataGlobal():
    with open("dataGlobal.json") as f_global:
        global_data = json.load(f_global)
    global_info = "Cases: " + str(global_data['cases']) + "\n" + "Deaths: " + str(global_data['deaths']) + "\n" + "Recovered: " + str(global_data['recovered'])
    return global_info

def readDataByCountry(country_name):
    with open("dataAllCountry.json") as f_country:
        all_country_data = json.load(f_country)
    j = 0
    for i in all_country_data:
        if(country_name == all_country_data[j]['country']):
            country_info = "Country: "
            country_info += str(all_country_data[j]['country']) + "\n"
            country_info += "Cases: "
            country_info += str(all_country_data[j]['cases']) + "\n"
            country_info += "Cases today: "
            country_info += str(all_country_data[j]['todayCases']) + "\n"
            country_info += "Deaths: "
            country_info += str(all_country_data[j]['deaths']) + "\n"
            country_info += "Today deaths: "
            country_info += str(all_country_data[j]['todayDeaths']) + "\n"
            country_info += "Recovered: "
            country_info += str(all_country_data[j]['recovered']) + "\n"
            country_info += "Active: "
            country_info += str(all_country_data[j]['active']) + "\n"
            country_info += "Critical: "
            country_info += str(all_country_data[j]['critical']) + "\n"
            country_info += "Cases per one million: "
            country_info += str(all_country_data[j]['casesPerOneMillion']) + "\n"
            country_info += "Deaths per one million: "
            country_info += str(all_country_data[j]['deathsPerOneMillion']) + "\n"
            country_info += "Total test: "
            country_info += str(all_country_data[j]['totalTests']) + "\n"
            country_info += "Test per one million: "
            country_info += str(all_country_data[j]['testsPerOneMillion'])
        j+=1
    return country_info

def readDataInVN(province):
    pass


if __name__ == '__main__':
    # readDataGlobal()
    readDataByCountry("Vietnam")
        