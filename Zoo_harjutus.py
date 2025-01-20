class Animal:
    """Animal class."""

    def __init__(self, name: str, specie: str, age: int):
        """
        Class constructor.

        Each animal has a name, species, and age.

        :param name: animal's name
        :param species: animal's species
        :param age: animal's age
        """
        self.name = name
        self.specie = specie
        self.age = age

    def __repr__(self):
        """
        String representation of the animal with its name, species, and age.
        
        :return: string representation of the animal
        """
        return f"{self.name} ({self.specie}, {self.age} years old),"


class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and a max number of animals the zoo can have.
        There is also an overview of all animals present in the zoo.

        :param name: zoo's name
        :param max_number_of_animals: max number of animals the zoo can have
        """
        self.name = name
        self.max_number_of_animals = max_number_of_animals
        self.animals = []

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and species is not yet present in the zoo.

        :param animal: animal to check
        :return: bool indicating if the animal can be added
        """
        if len(self.animals) >= self.max_number_of_animals:
            return False
        for existing_animal in self.animals:
            if existing_animal == animal or (existing_animal.name == animal.name and existing_animal.specie == animal.specie):
                return False
        return True

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal to add to the zoo
        """
        if self.can_add_animal(animal):
            self.animals.append(animal)

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed if it is present in the zoo.

        :param animal: animal to check
        :return: bool indicating if the animal can be removed
        """
        return animal in self.animals

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal to remove from the zoo
        """
        if self.can_remove_animal(animal):
            self.animals.remove(animal)

    def get_all_animals(self):
        """
        Return a list of all animals in the zoo.

        :return: list of Animal objects
        """
        return self.animals

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        return sorted(self.animals, key=lambda animal: animal.age)

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted alphabetically by name.

        :return: list of Animal objects sorted by name
        """
        return sorted(self.animals, key=lambda animal: animal.name)

