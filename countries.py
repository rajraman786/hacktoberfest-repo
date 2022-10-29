#London Olympics 2012 - 101computing.net/london-2012/
### Step 1 - open the text file
file=open("countries.txt")

# Prepare the list (empty list to start with)
countryList = []


# Read through the text file line by line
for eachLine in file:
    ### Step 2 - Extract the data from the text file
    totalmedals=0
    splitData=eachLine.split(";")
    nameOfCountry = splitData[0]
    goldMedals = int(splitData[1])
    silverMedals = int(splitData[2])
    bronzeMedals = int(splitData[3])
    totalmedals = goldMedals + silverMedals + bronzeMedals

    
    # Append this data to listOfCountries
    countryList.append([nameOfCountry, goldMedals, silverMedals, bronzeMedals, totalmedals])

#Sort this list in ascending order of gold medals
print("\n######## London 2012 - Top 10 Countries in ascending order of gold medals ##########\n")
countryascendinggold = sorted(countryList,key=lambda sort: sort[1])
for eachCountry in countryascendinggold:
    print(eachCountry[0] + " " + str(eachCountry[1]) + " gold medals")

# Sort this list in alphabetical (ascending) order of name of country
print("\n######## London 2012 - Top 10 Countries in alphabetical (ascending) order of name of country ##########\n")
countryascendingoredr = sorted(countryList,key=lambda sort: sort[0])
for eachCountry in countryascendingoredr:
    print(eachCountry[0])

#Sort this list in descending order of silver medals
print("\n######## London 2012 - Top 10 Countries in descending order of silver medals ##########\n")
countrydscendingsilver = sorted(countryList,key=lambda sort: sort[2], reverse=True)
for eachCountry in countrydscendingsilver:
    print(eachCountry[0] + " " + str(eachCountry[2]) + " silver medals")

#Sort this list in descending order of bronze medals
print("\n######## London 2012 - Top 10 Countries in descending order of bronze medals ##########\n")
countrydscendingbronze = sorted(countryList,key=lambda sort: sort[3], reverse=True)
for eachCountry in countrydscendingbronze:
    print(eachCountry[0] + " " + str(eachCountry[3]) + " broze medals")
    
#Sort this list in descending order of total number of medals (Bronze + Silver + Gold medals)
print("\n######## London 2012 - Top 10 Countries in descending order of total number of medals (Bronze + Silver + Gold medals) ##########\n")
countrydscendingtotal = sorted(countryList,key=lambda sort: sort[4], reverse=True)
for eachCountry in countrydscendingtotal:
    print(eachCountry[0] + " have total " + str(eachCountry[4]) + " medals")  


file.close()