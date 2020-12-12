## The program reads data from a file and shows a report to the user.
## Seblewonge Abera
## CSC 110
## Section D3
## 12/11/2020

# The function calculated the total by taking the list as an argument
def get_total(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

# The function takes two arguments and return the highest population and name of the country
def get_highest_population(pop_list, name):
    highest = pop_list[0]
    i = 0
    for idx in range(1, len(pop_list)-1):
        if pop_list[idx] > highest:
            highest = pop_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ', ' + format(highest,',.0f')

# The function takes two arguments and return the lowest population and the name of the country
def get_lowest_population(pop_list, name):
    lowest = pop_list[0]
    i = 0
    for idx in range(1, len(pop_list)-1):
        if pop_list[idx] < lowest:
            lowest = pop_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ', ' + format(lowest,',.0f')

# The function takes two arguments and return the highest GDP and the name of the country
def get_highest_GDP(GDP_list, name):
    highest = GDP_list[0]
    i = 0
    for idx in range(1, len(GDP_list)-1):
        if GDP_list[idx] > highest:
            highest = GDP_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ', ' + format(highest,',.0f')

# The function takes two arguments and return the lowest GDP and the name of the country
def get_lowest_GDP(GDP_list, name):
    lowest = GDP_list[0]
    i = 0
    for idx in range(1, len(GDP_list)-1):
        if GDP_list[idx] < lowest:
            lowest = GDP_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ', ' + format(lowest,',.0f')

# The function takes three arguments and return the highest GDP per capital and the name of the country
def get_highest_GDP_per_capital(population_list, GDP_list, name):
    highest = GDP_list[0]/population_list[0]
    i = 0
    for idx in range(1, len(GDP_list)-1):
        if GDP_list[idx]/population_list[idx] > highest:
            highest = GDP_list[idx]/population_list[idx]
            i = idx
    for y in range(len(name)):
        if i == y:
            return name[y] + ', ' + format(highest,',.2f')

# The function takes three arguments and return the lowest GDP and the name of the country
def get_lowest_GDP_per_capital(population_list, GDP_list, name):
    lowest = GDP_list[0]/population_list[0]
    i = 0
    for idx in range(1, len(GDP_list)-1):
        if (GDP_list[idx]/population_list[idx]) < lowest:
            lowest = (GDP_list[idx]) / (population_list[idx])
            i = idx
    for y in range(len(name)):
        if i == y:
            return name[y] + ', ' + format(lowest,'.2f')


# The funtion take two arguments and retunrs a list containing the GDP of all the countries
def GDP_per_capital(population_list, GDP_list):
    GDP_per_capital = []
    for idx in range(len(GDP_list)):
        GDP_per_capital.append(GDP_list[idx] / population_list[idx])
    return GDP_per_capital

# The function takes two arguments and retruns the average of GDp per capital
def get_average_GDP_per_captial(population_list, GDP_list):
    count = 0
    avg = 0
    x = GDP_per_capital(population_list, GDP_list)
    for idx in range(len(x)):
        count += x[idx]
        avg = count/len(x)
    return avg
# The function takes three arguments and returns a list of rich countries
def get_rich_countries(population_list, GDP_list, name):
    avg = get_average_GDP_per_captial(population_list,GDP_list)
    gdp = GDP_per_capital(population_list, GDP_list)
    to_compare = avg * 3
    rich_country = []

    for i in range(len(gdp)):
        if(gdp[i] > to_compare):
            rich_country.append(name[i])
    return rich_country

# The function takes three arguments and returns a list of poor countries
def get_poor_countries(population_list, GDP_list, name):
    avg = get_average_GDP_per_captial(population_list,GDP_list)
    gdp = GDP_per_capital(population_list, GDP_list)
    to_compare = 0.025 * avg  
    poor_country = []
    for i in range(len(gdp)):
        if gdp[i] < to_compare:
            poor_country.append(name[i])
    return poor_country


def main():
    DataFile = open('world_gdp_data_2012.txt', 'r')
    country_count = 0
    population_list = []
    GDP_list = []
    name = []
    data = DataFile.readline()

    while data != '':
        data = data.rstrip('\n')
        data = data.split(',')
        country_count += 1
        for i in range(1, len(data)-1):
            name.append(data[0])
            population = int(data[i])
            population_list.append(population)
            GDP_list.append(int(data[i+1]))

        data = DataFile.readline()

    DataFile.close()
    # # print(GDP_list)
    # # print(population_list)
    # # print(name)
    print('\nThe total numbera of countries are ' + str(country_count))

    print('\nThe total world population: ' + str(format(get_total(population_list),',.0f')))
    # # print(v)
    print('\nThe name and population of the country that has the highest population: ' +
          str(get_highest_population(population_list, name)))
    print('\nThe name and population of the country that has the lowest population: ' +
          str(get_lowest_population(population_list, name)))
    print('\nThe name and GDP of the country that has the greatest GDP: ' +
          str(get_highest_GDP(GDP_list, name)))
    print('\nThe name and GDP of the country that has the lowest GDP: ' +
          str(get_lowest_GDP(GDP_list, name)))
    print('\nThe name and \"GDP per capita"\ of the country that has the highest \"GDP per capita"\: ' + '\n' +
          str(get_highest_GDP_per_capital(population_list, GDP_list, name)))
    print('\nThe name and \"GDP per capita"\ of the country that has the lowesr \"GDP per capita"\: ' + '\n' +
          str(get_lowest_GDP_per_capital(population_list, GDP_list, name)))
    # print(get_average_GDP_per_captia(population_list,GDP_list))
    # print(GDP_per_capital(population_list, GDP_list))
    print('\nAverage "GDP per capita": ' +
          str(get_average_GDP_per_captial(population_list, GDP_list)))
    print('\nA list of "rich countries": ' +
          str(get_rich_countries(population_list, GDP_list, name)))
    print('\nA list of "poor countries": ' +
          str(get_poor_countries(population_list, GDP_list, name)))



main()
