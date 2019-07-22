# -*- coding: utf-8 -*-
"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""
# type your code for "String Concatenation" below this comment and above the one below it.------------------------------

var = "Hello" + " world"
print(var)

a = 11
b = 38
c = str(a) + str(b)
print(c)


# ----------------------------------------------------------------------------------------------------------------------
"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit
[name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""
# type your code for "%s and input()" below this comment and above the one below it.------------------------------------

# Feito usando a versão 2.x do python. Nessa versão o input aprendido na aula é o raw_input

rest = raw_input("What is your favorite restaurant?")
place = raw_input("What place you want to visit?")
nick = raw_input("First name or Nickname")

print("Seu restaurante favorito é %s, você gostaria de visitar %s e seu nick é %s" % (rest, place, nick))
# ----------------------------------------------------------------------------------------------------------------------