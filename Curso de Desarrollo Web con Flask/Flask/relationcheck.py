from example8 import dataBase, Pet, Owner, Toy


pet1 = Pet('7asán')
pet2 = Pet('Malak')
pet3 = Pet('Fiera')

dataBase.session.add_all([pet1, pet2, pet3])
dataBase.session.commit()

pets= Pet.query.all()
print('Show all pets')
print(pets)

pet1 = Pet.query.filter_by(name='7asán').first()
pet2 = Pet.query.filter_by(name='Malak').first()
pet3 = Pet.query.filter_by(name='Fiera').first()

owner1 = Owner('Mónica', pet1.id)
owner2 = Owner('Naim', pet2.id)
owner3 = Owner('Emir', pet3.id)
dataBase.session.add_all([owner1, owner2, owner3])
dataBase.session.commit()

owners = Owner.query.all()
print('Show all owners')
print(owners)

toy1 = Toy('Ball', pet1.id)
toy2 = Toy('Little stick', pet1.id)
toy3 = Toy('Ball', pet2.id)
toy4 = Toy('Little stick', pet2.id)
toy5 = Toy('Ball', pet3.id)
toy6 = Toy('Little stick', pet3.id)

dataBase.session.add_all([toy1, toy2, toy3, toy4, toy5, toy6])
dataBase.session.commit()

toys = Toy.query.all()
print('Show all Toys')
print(toys)

Pet.show_toy()
