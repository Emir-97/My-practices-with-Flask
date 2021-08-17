from example7 import dataBase, Person

#Este método se utiliza para crear la tabla de nuestra base de datos realizada en example7.py
dataBase.create_all()

#Este método se utiliza para crear los datos para nuestra tabla
person1 = Person('Emir', 24)
person2 = Person('Naim', 17)
person3 = Person('Monica', 50)

#Este método se utiliza para agregar los datos creados recientementes a nuestra tabla.
dataBase.session.add_all([person1, person2, person3])
dataBase.session.commit()

#SE UTILIZA EL MÉTODO PARA MOSTRAR TODOS LOS DATOS DE LA TABLA
persons = Person.query.all()
print('Show all data')
print(persons)

#Este método se utiliza para buscar todos los datos que se especifiquen y por columna
#Es cómo un filtro para mostrar datos por columna
filter1 = Person.query.filter_by(name='Emir')
print('The requested information is displayed')
print(filter1.all())

#Este método se utiliza para búsquedas por elementos o id
select1 = Person.query.get(2)
print('Search for id')
print(select1)

#Este método se utiliza para la actualización de los datos de nuestra tabla
person = Person.query.get(3)
person.age = 51
dataBase.session.add(person)
dataBase.session.commit()

#Método para borrar datos de la tabla
deletePerson = Person.query.get(3)
dataBase.session.delete(deletePerson)
dataBase.session.commit()
print("The data {} was deleted from the table".format(deletePerson))

persons = Person.query.all()
print('Show all data')
print(persons)
