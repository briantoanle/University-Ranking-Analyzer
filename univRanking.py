
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
    #print(universityInternationalRank(topUni,'South Korea'))
    #print(universityNationalRank(topUni,'Canada'))
    #print(averageScore(topUni,'Japan'))
    #print(continentRelativeScore(topUni,capitals,'Japan'))
    #print(capitalCity(capitals,'Canada'))
def universitiesCount(univ):
    return 'Total number of universities => ' + str(len(univ))

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

def universityInternationalRank(univ, country):
    line = 0
    internationalRanking = []
    for row in univ:
        if row[COUNTRY] == country:
            internationalRanking.append(row[WORLD_RANK])

    rank = int(internationalRanking[0])
    #print(univ[rank-1])
    return 'At international rank => ' + str(internationalRanking[0]) + ' the university name is => ' + str((univ[rank-1][INSTITUTION]).upper())

def universityNationalRank(univ, country):
    nationalRanking = []
    for row in univ:
        if row[COUNTRY] == country:
            return 'At national rank => 1 the university name is => ' + str(row[INSTITUTION]).upper()
            #nationalRanking.append(row[NATIONAL_RANK])
    #return nationalRanking

def averageScore(univ, country):
    score = 0
    count = 0

    for row in univ:
        if row[COUNTRY] == country:
            count +=1
            score += float(row[SCORE])

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
    #print('conti',continent)

    for x, key in dict.items():
        if key == continent:
            countriesInContinent.append(x)

    # find highest score in continent USA so North America
    highest_score = 0
    score = 0
    counter = 0
    for row in univ:
        if row[COUNTRY] in countriesInContinent:
            counter += 1
            score += float(row[SCORE])
            if float(row[SCORE]) > highest_score:
                highest_score = float(row[SCORE])


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

def universityCapitalName(capitals,country):
    print()
main()