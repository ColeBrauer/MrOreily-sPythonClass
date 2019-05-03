# Broken Boolean; toggle each one of these EXPRESSION on by removing
# the hash tag and then press F5. Go through the list and see if this is
# broken.

print('a' == ('a' or 'b')) 
print('b' == ('a' or 'b')) 

print('a' == ('a' and 'b'))
print('b' == ('a' and 'b'))


# Add print to detemine if these statements are True or False.
# explain why this happened. How can you rewrite correct way to get
# the results intuitively needed?

# If the statement is or, it reads the first variable
# if the statement is and, it reads the last variable


print('a' == ('a' or 'b')) 
print('b' == ('b' or 'a')) 

print('a' == ('a' and 'b'))
print('b' == ('b' and 'a'))
