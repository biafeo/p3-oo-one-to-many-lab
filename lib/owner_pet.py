

class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner= None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise ValueError("Invalid pet type. Allowed types are: {}".format(", ".join(self.PET_TYPES)))
        self.pet_type = pet_type
        self.owner=owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only instances of Pet can be added as pets.")
        pet.owner = self

    @property 
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise TypeError("Owner must be an instance of Owner.")
        self._owner = value