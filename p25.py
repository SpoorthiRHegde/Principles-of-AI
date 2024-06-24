import string
t="welcome_to_my_python_world"
print("Original string: "+t)
res=string.capwords(t.replace("_"," "))
print("The string after changing: "+res)
