# # Calculate the average of my utility bills for the past three months.
# avg = (23 + 32 + 64)/3
# print(avg)

# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

# How many tiles are needed?
# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

# tiles = 17 * 6
# print(tiles)

# part_one = 9 * 7
# print(part_one)

# part_two = 5 * 7
# print(part_two)

# leftover_tiles = tiles/(part_one + part_two)
# print(leftover_tiles)

# carrot = 24
# rabbits = 8

# crs_per_rab = carrot/rabbits
# print(crs_per_rab)

# rabbits = 12

# crs_per_rab = carrot/rabbits

# ## The current volume of a water reservoir (in cubic metres)
# reservoir_volume = 4.445e8
# ## The amount of rainfall from a storm (in cubic metres)
# rainfall = 5e6

# ## decrease the rainfall variable by 10% to account for runoff
# rainfall *= .9
# print(f"This is the rainfall variable decreased by 10% {rainfall}")

# ## add the rainfall variable to the reservoir_volume variable
# reservoir_volume += rainfall
# print(f"This the reservior volume {reservoir_volume}")
# ## increase reservoir_volume by 5% to account for stormwater that flows
# ## into the reservoir in the days following the storm
# reservoir_volume *= 1.05
# print(f"This is if the reservior volume increased by 5% {reservoir_volume}")
# ## decrease reservoir_volume by 5% to account for evaporation
# reservoir_volume *= 0.95
# print(f"This is if the reservior volume decreased by 5% {reservoir_volume}")
# ## subtract 2.5e5 cubic metres from reservoir_volume to account for water
# ## that's piped to arid regions.
# reservoir_volume -= 2.5e5
# print(f"This is if we subtract 2.5e5 cubic metres from rv to account for water that is piped to arid regions {reservoir_volume}")

# sf_population, sf_area = 864816, 231.89
# rio_population, rio_area = 6453682, 486.5

# san_francisco_pop_density = sf_population/sf_area
# rio_de_janeiro_pop_density = rio_population/rio_area

# # Write code that gives a boolean value True if San Francisco is denser than Rio, and False otherwise
# comparision_result = san_francisco_pop_density > rio_de_janeiro_pop_density
# print(comparision_result)

# my_string = "this is a string"
# my_string2 = 'this is also a string'

# this_string = 'Simon\'s skateboard is in the garage'
# print(this_string)

# single_quote_string = '"This is a quote itself"'

# double_quote_string = "Simon's skateboard is in the garage"

# print(single_quote_string * 5)
# print(len(double_quote_string))
# print(double_quote_string[6])
# print(double_quote_string[5])

# print(len("ababa")/len("ab"))

# Quiz: Fix the Quote
# The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. First run it with Test Run to view the error message. Then resolve the problem so that the quote (from Henry Ford is correctly assigned to the variable ford_quote.

# # TODO: Fix this string!
# ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
# print(ford_quote)

# username = "Kinari"
# timestamp = "04:50"
# url = "http://petshop.com/pets/mammals/cats"

# TODO: write a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

# message = f"{username} accessed the site {url} at {timestamp}."
# print(message) #replace "" with your code

# # Quiz: len()
# # Use string concatenation and the len() function to find the length of a certain movie star's actual full name. Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name!

# given_name = "William"
# middle_names = "Bradley"
# family_name = "Pitt"
# # Todo: calculate how long this name is
# name_length = len(given_name) + len(" ") + len(middle_names) + len(" ") + len(family_name)
# print(name_length) #replace `None` with your code

# # Now we check to make sure that the name fits within the driving license character limit
# # Uncomment the code below. You don't need to make changes to the code.

# driving_license_character_limit = 28
# print(name_length <= driving_license_character_limit)

# print(type(4))
# print(type(3.7))
# print(type('this'))
# print(type(True))

# print("0" + 5)
# print("5" + 0)

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: assign the total sales to a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the assigning statement.

result_string = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print(f"This week's total sales: {result_string}")
