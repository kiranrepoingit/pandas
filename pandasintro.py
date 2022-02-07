import pandas as pd
## sarvan35
def pd_series():
    data = pd.Series(['Ram','Rakesh','Rakesh'], index=['8273','17238','1239'])
    print(data)
    print("Get a particular data >> ",data['17238'])
    print(data.values)
    print(data.index)

def pd_series_Dict_1():
    population_dict = {'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860,'Illinois': 12882135}
    population = pd.Series(population_dict)
    population = population.sort_index()
    print(population)
    print(population['California'])


def pd_series_Dict_2():
    area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995}
    area = pd.Series(area_dict)
    print(area)


def pd_dframe():
    population_dict = {'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860,
                       'Illinois': 12882135}
    population = pd.Series(population_dict)

    ############################

    area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995}
    area = pd.Series(area_dict)

    ############################

    states = pd.DataFrame({'population_col1': population, 'area_col2': area})
    print(states)


pd_dframe()