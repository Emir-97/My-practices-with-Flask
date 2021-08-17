from example7 import dataBase, Person

#Se agrega la información de la nueva columna country creada en example7.py y luego agregada a la tabla
person = Person.query.get(1)
person.country = 'Argentina'
person4 = Person.query.get(2)
person4.country = 'China'
dataBase.session.add_all([person, person4])
dataBase.session.commit()

persons = Person.query.all()
print(persons)
