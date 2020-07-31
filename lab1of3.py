#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.


reservoir_volume = 4.445e8

rainfall = 5e6






# add the rainfall variable to the reservoir_volume variable




# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm




# decrease reservoir_volume by 5% to account for evaporation




# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.





# print the new value of the reservoir_volume variable
# to decrease the rainfall volume by 10%, that means what is left is (100-10)% which is 90%.let this be denoted by runoff. This accounts for runoff
rainfall *= (90/100)

#add the rain_fall variable to the reservoir_variable
reservoir_volume += rainfall


#to increase the reservoir_volume by 5%, this implies that we have (100+5)% =105%. Thisaccountsfor stormwater that flows intothe reservoir
reservoir_volume*= (105/100)

#to decreasethereservoir volume by 5%,we have 95%. This accounts for evaporation 
reservoir_volume*= (95/100)

#to account for water that's piped to arid regions
reservoir_volume -=2.5e5
print(reservoir_volume)