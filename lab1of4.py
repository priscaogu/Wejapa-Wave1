sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# using the boolean operator,

population_density = san_francisco_pop_density > rio_de_janeiro_pop_density

print(population_density)