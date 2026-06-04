# Input: geeksforgeeks_is_best  
# Output: GeeksforgeeksIsBest

str="geeksforgeeks_is_best"
print( ''.join(word.capitalize() for word in str.split('_')) )