# Exercise 1
name = "Amanda Velasquez"
year = 2025
colors = ["white", "black", "blue"]
is_sunny = True

# Exercise 2
first_three = name[:3]
print(first_three)

# Exercise 3
new_year = year+10
print(new_year)

# Exercise 5
last_element = colors[-1:]
print(last_element)

# Exercise 6
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)

# Exercise 7
name = "Amanda Velasquez"
first_word = name.split(" ")[0]
first_word_upper = first_word.upper()
new_name = first_word_upper + name[len(first_word):]
print(new_name)

# Exercise 8
year = 2025
print(f"Estamos en el año {year}.")

# Exercise 9
saludo = "hello world"
print(saludo)

# Exercise 10
cadena = "La palabra hola es grave"
cadena_uno = cadena.find("hola")
print(cadena_uno)
cadena_dos = cadena.replace("hola", "adios")
print(cadena_dos)