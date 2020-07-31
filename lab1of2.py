#Quiz: 

#Let the number of tiles needed for the entire floor be denoted by entire_floor. entire_floor is given by the number needed for the first part +the number needed for the second part.
first_part = 9*7
second_part = 5*7
entire_floor = first_part + second_part
print(entire_floor)

# The number of tiles that will be left over is given by the number of given packages - the number of tilesneeded for the entire floor  
seventeen_packages = 17*6
left_over = seventeen_packages - entire_floor

print(left_over)
