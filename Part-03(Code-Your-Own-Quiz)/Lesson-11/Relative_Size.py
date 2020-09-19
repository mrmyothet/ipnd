#IN text
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21.],
             ['United States','Washington',307]]
print (countries[0][2] / countries[2][2])

#my own
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21.],
             ['United States','Washington',307]]
china = countries[0][2]
romania = countries[2][2]
division_result = china / romania
multiple_result = china * romania
plus_result = china + romania
subtraction_result = china - romania
print (china)
print (romania)
print ("division_result--" + str(division_result))
print ("multiple_result--" + str(multiple_result))
print ("plus_result--" + str(plus_result))
print ("subtraction_result--" + str(subtraction_result))
