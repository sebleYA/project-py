
def get_total(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

def get_highest_population(pop_list, name):
    highest = pop_list[0]
    i = 0
    for idx in range(1, len(pop_list)-1):
        if pop_list[idx] > highest:
            highest = pop_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ' ' + str(highest)


def get_lowest_population(pop_list, name):
    lowest = pop_list[0]
    i = 0
    for idx in range(1, len(pop_list)-1):
        if pop_list[idx] < lowest:
            lowest = pop_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ' ' + str(lowest)


def get_highest_GDP(GDP_list, name):
    highest = GDP_list[0]
    i = 0
    for idx in range(1, len(GDP_list)-1):
        if GDP_list[idx] > highest:
            highest = GDP_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ' ' + str(highest)


def get_lowest_GDP(GDP_list, name):
    lowest = GDP_list[0]
    i = 0
    for idx in range(1, len(GDP_list)-1):
        if GDP_list[idx] < lowest:
            lowest = GDP_list[idx]
            i = idx
    for y in range(len(name)):
        if(i == y):
            return name[y] + ' ' + str(lowest)

def get_highest_GDP_per_capital(population_list, GDP_list, name):
    highest = GDP_list[0]/population_list[0]
    print(highest)
    i = 0
    for idx in range(1, len(GDP_list)-1):
        if GDP_list[idx]/population_list[idx] > highest:
            highest = GDP_list[idx]/population_list[idx]
            i = idx
    for y in range(len(name)):
        if i == y:
            return name[y] + ' ' + str(highest)


def get_lowest_GDP_per_capital(population_list, GDP_list, name):
    lowest = GDP_list[0]/population_list[0]
    i = 0
    for idx in range(0, len(GDP_list)):
        if (GDP_list[idx])/(population_list[idx]) < lowest:
            lowest = GDP_list[idx]/GDP_list[idx]
            i = idx
    for y in range(len(name)):
        if i == y:
            return name[y] + ' ' + str(lowest)

# create new function to calculate GDP


def GDP_per_capital(population_list, GDP_list):
    GDP_per_capital = []
    for idx in range(len(GDP_list)):
        GDP_per_capital.append(GDP_list[idx] / population_list[idx])
        print(GDP_per_capital)
    return GDP_per_capital

## avarage
def get_average_GDP_per_captial(population_list,GDP_list):
    total_GDP_per_capital = 0
    count = 0
    x = []
    for idx in range(len(GDP_list)):
        x.append(GDP_per_capital(population_list, GDP_list))
        total_GDP_per_capital += x
        count += 1
    return total_GDP_per_capital/count


def main():
    DataFile = open('testingFile.txt', 'r')
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
    # print(get_total(population_list))
    # # print(v)
    # print(get_highest_population(population_list, name))
    # print(get_lowest_population(population_list, name))
    # print(get_highest_GDP(GDP_list, name))
    # print(get_lowest_GDP(GDP_list, name))
    # print(get_highest_GDP_per_captia(population_list,GDP_list,name))
    # print(get_lowest_GDP_per_captia(population_list,GDP_list,name))
    # print(get_average_GDP_per_captia(population_list,GDP_list))
    print(GDP_per_capital(population_list, GDP_list))
    print(get_average_GDP_per_captial(population_list,GDP_list))

    # # print(y)
    # # print('The total numbera of countries are ' + str(country_count))
    # # print('The total numbera of world popultation are ' +
    #       str(format(v, ',.0f')))


main()
