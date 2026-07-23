groups = [['student1', 'student2', 'student3'],
 
    ['student4', 'student5', 'student6'],
 
    ['student7', 'student8', 'student9'],
 
    ['student10', 'student11', 'student12']]
 
for group in groups:
    print('Nested list: {}, group {}'.format(groups.index(group), group))



set_a = set(['a', 'b', 5, 2])
print("Set_a: {}".format(set_a))
  
set_b = {'a', 'c', 5, 4, None}
print("Set_b: {}".format(set_b))
  
  
print("Intersection: {}".format(set_a & set_b)) 
  
print("Union: {}".format(set_a | set_b)) 
  
print("Difference: {}".format(set_a - set_b))


set_a = set(['a', 'b', 5, 2])
 
print("Starting set: {}".format(set_a))
 
 
set_a.add(None) # Dodavanje elementa None
 
print("After usage of .add() method: {}".format(set_a))
 
set_a.remove(5) # Brisanje elementa koji ima vrednost 5
 
print("After usage of .remove() method: {}".format(set_a))
 
 
set_a.clear() # Uklanjanje svih elemenata iz seta
 
print(set_a) # Dobijamo prazan set


lst=[1993, 1994, 1995, 1994, 1993, 1996] 
set_lst = set(lst) 
print(set_lst)
  
lst = list(set_lst) 
print(lst)
  
lst.sort() 
print(lst)

packets = {"Total 1", "Total 4", "Total 8"}
for package in packets: 
    print(package)


student_dict = {'Name':'Marco', 'Field':'Electrical engineering', 'Age':'20'}
 
values_dict = dict(first=1, second = 2)
 
cities_dict = {}
cities_dict['city1'] = 'New York'
cities_dict['city2'] = 'London'
cities_dict['city3'] = 'Moscow'
 
print(student_dict)
print(values_dict)
print(cities_dict)


# print(student_dict['Gender'] ) # key Error
print(student_dict.get('Gender', 'Field does not exist') ) # OK

recnik = {}.fromkeys(['name', 'last name', 'address', 'city'], None)
print(recnik)

for i in student_dict:
    print(i, end= ', ')
for i in student_dict.values():
    print(i, end= ', ')
for key, value in student_dict.items():
    print('{}:{}'.format(key, value), end = ', ')

student_dict = {'Name':'Marco', 'Field':'Electrical engineering', 'Age':'20'}
 
student_dict_keys = list(student_dict.keys())
 
student_dict_keys.sort()
 
print("Order of dict keys: {}".format(student_dict.keys()))
 
print("Order of dict keys in a sorted list: {}".format(student_dict_keys))
 
 
for i in student_dict_keys:
    print("Dict element: {}, on a key: {}".format(student_dict[i], i))


# Program sadrži jedan rečnik sa pozdravnim porukama, ključ je oznaka jezika, a vrednost je prevod poruke.

# Potrebno je napisati program koji će prilikom startovanja tražiti od korisnika da unese oznaku jezika. Nakon odabira jezika, program prikazuje pozdravnu poruku iz rečnika na jeziku koji je korisnik odabrao.

messages = {"en":"Hello", "de": "Hallo", "it": "Ciao"}
language = input("Choose language (en, de or it):Serbian ")
print(messages[language]) 
