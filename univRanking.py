import csv

# univRanking
WORLD_RANK = 0
INSTITUTION = 1
COUNTRY = 2
NATIONAL_RANK = 3
QUALITY_OF_EDUCATION = 4
ALUMNI_EMPLOYMENT = 5
QUALITY_OF_FACULTY = 6
RESEARCH_PERFORMANCE = 8
SCORE = 8

# capitals
COUNTRY_NAME = 0
CAPITAL = 1
LATITUDE = 2
LONGITUDE = 3
COUNTRY_CODE = 4
CONTINENT = 5

def main():
    capitals = []
    with open('capitals.csv', 'r') as fh:
        headers = fh.readline()

        for line in fh:
            # print(line)
            data = line.strip().split(',')
            # print("here", data)
            # print(data)
            capitals.append(data)

    topUni = []
    with open('TopUni.csv', 'r') as fh:
        headers = fh.readline()

        for line in fh:
            # print(line)
            data = line.strip().split(',')
            # print("here", data)
            # print(data)
            topUni.append(data)

    #print(availableCountries(topUni))
    #print(availableContinents(capitals))
    #teststring = universityInternationalRank(topUni,'USA').replace(' ','').upper()
    #print(teststring)
    #print("ATINTERNATIONALRANK=>1THEUNIVERSITYNAMEIS=>HARVARDUNIVERSITY")
    #print(universityNationalRank(topUni,'Canada'))
    print(universityInternationalRank(topUni,'usa'))
    #print(universityInternationalRank(topUni, 'USA'))
    #print(averageScore(topUni,'Japan'))
    #print(continentRelativeScore(topUni,capitals,'Japan'))
    #print(capitalCity(capitals,'Canada'))
    #print(universityCapitalName(topUni,capitals,'France'))
def universitiesCount(univ):
    return 'Total number of universities => ' + str(len(univ)-1)

def availableCountries(univ):
    countries = []
    for row in univ:
        if row[COUNTRY].upper() not in countries:
            countries.append(row[COUNTRY].upper())

    return 'Available countries => ' + ', '.join(countries)

def availableContinents(capitals):
    continents = []
    for row in capitals:
        if row[CONTINENT].upper() not in continents:
            continents.append(row[CONTINENT].upper())
    return 'Available continents => ' + ', '.join(continents)
def universityInternationalRank1(univ, country):
    #print(country)
    line = 0
    internationalRanking = []
    for row in univ:
        #print('row',row[COUNTRY])
        if row[COUNTRY] == country:
            #print('hereee')
            internationalRanking.append(row[WORLD_RANK])
    print(internationalRanking)
    #print(internationalRanking[0])
    #rank = int(internationalRanking[0])
    #print('rank',rank)
    #print(univ[rank-1])
    returnString = 'At international rank => ' + '10'
    returnString2 =' the university name is => ' + str((univ[10][INSTITUTION]).upper())

    #return 'At international rank => ' + str(internationalRanking[0]) + ' the university name is => ' + str((univ[rank-1][INSTITUTION]).upper())
    #
    #               print(returnString)
    #returnString= returnString.upper()
    return returnString

def universityInternationalRank(univ, country):
    line = 0
    internationalRanking = []
    #print('country',country)
    for row in univ:

        if row[COUNTRY].lower() == country.lower():
            internationalRanking.append(row[WORLD_RANK])
    #print(internationalRanking)
    #print(internationalRanking[0])
    rank = int(internationalRanking[0])
    #print(univ[rank-1])
    returnString = 'At international rank => ' + str(internationalRanking[0]) + ' the university name is => ' + str((univ[rank][INSTITUTION]).upper())
    #print(returnString)
    #return 'At international rank => ' + str(internationalRanking[0]) + ' the university name is => ' + str((univ[rank-1][INSTITUTION]).upper())

    #returnString= returnString.upper()
    return returnString

def universityNationalRank(univ, country):
    nationalRanking = []
    for row in univ:
        if row[COUNTRY].lower() == country.lower():
            return 'At national rank => 1 the university name is => ' + str(row[INSTITUTION]).upper()
            #nationalRanking.append(row[NATIONAL_RANK])
    #return nationalRanking

def averageScore(univ, country):
    score = 0
    count = 0

    for row in univ:
        if row[COUNTRY].lower() == country.lower():
            count +=1
            score += float(row[SCORE])
    print()
    return 'The average score => ' + str(round((score/count),2)) + '%'



def continentRelativeScore(univ,capitals, country):
    countriesInContinent = []
    dict = {}
    for row in capitals:
        if row[COUNTRY_NAME] not in dict:
            dict[row[COUNTRY_NAME]] = row[CONTINENT]
            #print(row[COUNTRY_NAME])
    continent = ''
    if country in dict:
        continent = dict[country]

    #print(country)
    #print('conti',continent)

    for x, key in dict.items():
        if key == continent:
            countriesInContinent.append(x.lower())


    # find highest score in continent USA so North America
    highest_score = 0
    score = 0
    counter = 0
    for row in univ:
        if row[COUNTRY].lower() in countriesInContinent:
            counter += 1
            score += float(row[SCORE])
            if float(row[SCORE]) > highest_score:
                highest_score = float(row[SCORE])

    #print("**** ",highest_score,countriesInContinent)

    avg = averageScore(univ,country)
    avg = avg.replace('The average score => ', '')
    avg = avg.replace('%', '')
    avg = float(avg)
    #print('here',avg)
    #print(highest_score)

        #for i in countriesInContinent:
        #    if row[]
    #print(avg)
    #print(highest_score)
    return 'The relative score to the top university in ' + continent.upper() + ' is => ' + f'({avg} / {highest_score}) ' \
           + 'x 100% = ' +str(round(((avg / highest_score ) * 100), 2)) +'%'

def capitalCity(capitals,country):
    #print(country)
    for row in capitals:
        if country in row:
            return 'The capital is => ' + row[CAPITAL].upper()

def universityCapitalName(univ,capitals,country):
    print()
    capital = ''
    for row in capitals:
        if country in row:
            capital = row[CAPITAL]
    institutionList = []
    for row in univ:
        # concatenate or else it would not return true

        if capital in str(row[INSTITUTION]):
            #print(row[INSTITUTION])
            #print('here')
            institutionList.append(row[INSTITUTION])
    #print(capital)
    #print(institutionList)
    returnString = ''
    for i in range(len(institutionList)):
        returnString += f'    #{i+1} ' + institutionList[i].upper() + '\n'
    return 'The universities that contain the capital name =>\n' + returnString

def loadCSVData(filename):
    list=[]
    fileContent = open(filename,"r",encoding='utf8')
    for line in fileContent:
        #next(fileContent)
        line = line.lower()
        data = line.strip().split(',')
        # print("here", data)
        # print(data)
        list.append(data)

    fileContent.close()
    return list

def getInformation(selectedCountry,rankingFileName,capitalsFileName):
    univ = loadCSVData(rankingFileName)
    capitals = loadCSVData(capitalsFileName)
    selectedCountry = selectedCountry.lower()
    with open('output.txt','w') as f:
        f.write(universitiesCount(univ))
        f.write(availableCountries(univ))
        f.write(availableContinents(capitals))
        #print("here", selectedCountry)

        #print('selected',selectedCountry)
        #print(universityInternationalRank(univ,selectedCountry))
        f.write(universityInternationalRank(univ,selectedCountry))
        f.write(universityNationalRank(univ,selectedCountry))
        f.write(averageScore(univ,selectedCountry))
        f.write(continentRelativeScore(univ,capitals,selectedCountry))
        f.write(capitalCity(capitals,selectedCountry))
        f.write(universityCapitalName(univ,capitals,selectedCountry))

#main()