import random

countries = {'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome'}
print(countries)
countries_population = {country: random.randint(1, 100) for country in countries}
print(countries_population)
print(countries_population.items())
countries_population_condition = {country: population for country, population in countries_population.items() if
                                  population > 50}
print(countries_population_condition)
