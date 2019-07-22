# -*- coding: utf-8 -*-
"""
string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it
"""
# type your code for "string and escape sequences" in between this single line comment and the one below it-------------

#1-
str1 = "teste"
print(str1)

#2-
str2 = 'teste'
print(str2)

#3-
str3 = "O livro \"Gerra dos tronos\" é bom"
print(str3)

#4-
str4 = 'O livro \'Guerra dos tronos\' é bom'
print(str4)

# ----------------------------------------------------------------------------------------------------------------------
"""
accessing values by index and string slicing:
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
2.create a variable and assign it the "a" from the string assigned to the variable lannisters.
3.create a variable and assign it the "J" from the string assigned to the variable lannisters.
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters.
5.create a variable and assign it "Cersei" from the string assigned to the variable lannisters.
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.
"""
# type your code for "accessing values by index and string slicing" in between this comment and the one below it--------

#1-
lannisters = "JaimeCerseiTyrion"
print(lannisters)

#2-
str5 = lannisters[1]
print(str5)

#3-
str6 = lannisters[0]
print(str6)

#4-
str7 = lannisters[:5]
print(str7)

#5-
str8 = lannisters[5:11]
print(str8)

#6-
str9 = lannisters[11:]
print(str9)

# ----------------------------------------------------------------------------------------------------------------------