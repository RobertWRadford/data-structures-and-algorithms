#Node class
class Animal:

    def __init__(self, animal = None, next_ = None):
        self.animal = animal
        self.next = next_

class InvalidOperationError(Exception):
    pass

#Stack class
class Waiting_list:

    def __init__(self):
        self.first_up = None

    def none_available(self):
        return True if self.first_up else False

    def whos_next(self):
        if not self.first_up:
            raise InvalidOperationError("All animals have been adopted!")
        return self.first_up.animal

    def intake (self, animal):
        new_animal = Animal(animal, self.first_up)
        self.first_up = new_animal
        return self.first_up

    def discharge(self):
        if not self.first_up:
            raise InvalidOperationError("All animals have been adopted!")
        bye_bye = self.first_up
        self.first_up = self.first_up.next
        return bye_bye.animal

#Queue class
class Animal_Shelter():

    def __init__(self, waiting_list=Waiting_list(), temp_cage=Waiting_list()):
        self.shelter = waiting_list
        self.temp_cage = temp_cage

    def __str__(self):
        if not self.shelter.first_up:
            return None
        ret_string = f'{self.shelter.first_up.animal}'
        current = self.shelter.first_up
        while current.next_:
            current = current.next_
            ret_string += f' ->{current.animal}'
        return ret_string

    def welcome_in(self, animal):
        if animal in ['cat','dog']:
            if not self.shelter.first_up:
                self.shelter.intake(animal)
            else:
                while self.shelter.first_up:
                    self.temp_cage.intake(self.shelter.discharge())
                self.temp_cage.intake(animal)
                while self.temp_cage.first_up:
                    self.shelter.intake(self.temp_cage.discharge())
        else:
            raise InvalidOperationError("Sorry we only take dogs & cats here.")

    def adoption_out(self, animal_type=None):
        if not self.shelter.first_up:
            raise InvalidOperationError("All animals have been adopted!")
        if animal_type in ['cat', 'dog']:
            while self.shelter.whos_next() != animal_type:
              self.temp_cage.intake(self.shelter.discharge())
            if self.shelter.first_up != animal_type:
                adopted = f'There are no {animal_type}s left.'
            else:
                adopted = self.shelter.discharge()
            while self.temp_cage.first_up:
                self.shelter.intake(self.temp_cage.discharge())
        elif animal_type is None:
            adopted = self.shelter.discharge()
        else:
            raise InvalidOperationError("Sorry we only keep dogs & cats here.")
        return adopted.animal


if __name__ == "__main__":
    testrun = Animal_Shelter()
    testrun.welcome_in("dog")
    testrun.welcome_in("cat")
    print(testrun.shelter.first_up.animal)