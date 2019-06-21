from bs4 import BeautifulSoup
from time import sleep
import requests, os


"""
This script Pulls country location for any given Ip Address

Just run the script, enter your desired ip address then see the result.

Test Ips:
    - 84.186.46.192 (Germany)
    - 14.1.32.0 (New Zealand)
    - 14.200.0.0 (Australia)
    - 121.157.50.191 (South Korea)
    - 161.185.160.93 (United States)
"""

#Cleans the console
def cleanConsole():
    os.system('cls')

#list for Countries
countryList = []

#Infor for user
cleanConsole()
initialInfo = "\nEnter IpAddress below or type 'exit' to stop script"
textDivider = '\n===================================================='


while True:

    #Prints info at top of Screan  
    print(initialInfo + textDivider)

    #Prints ALL countries searched
    if countryList != []:
        print('\nCountries Found:')
        #Removes any dupe countries from the list
        noDupes = list(dict.fromkeys(countryList))
        for country in noDupes:
            print(country)
    else:
        pass


    #Method that gives user choice to find more countries for exit script
    def exitLoop():
        exitChoice = input("\n\nWould you like to exit?\n\n   (Yes / No): ")
        if exitChoice.lower() == "yes":
            exit()
        elif exitChoice.lower() == "no":            
            sleep(1)
            cleanConsole()
        else:
            print('Invalid entry - Try again.')
            sleep(2)
            cleanConsole()
            exitLoop()


    def allCountries():
        countryList.append(getCountry)


    #Finds Country, prints it to screen and add's all countries searched to a list or exits script 
    try:
        ipAddress = input('\nIp Address: ')
        if ipAddress.lower() != 'exit':
            webpage_response = requests.get('https://whatismyipaddress.com/ip/{}'.format(ipAddress))
            webpage = webpage_response.content

            soup = BeautifulSoup(webpage, 'html.parser')
            getCountry = soup.select('td')[11].get_text()
            print("\nCountry Found!" + "\n\n   Result ~ " +getCountry)
            allCountries()
            exitLoop()
        else:
            break
    except IndexError:
        print("\nInvalid Ip Address Format. Try again")
        sleep(2)
        cleanConsole()
        
