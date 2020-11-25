import pytest
from fifo_animal_shelter import Animal, Waiting_List, Animal_Shelter

def test_Animal_Shelter_sequence(default_shelter):
	assert str(default_shelter) == 'dog ->cat ->cat ->cat ->dog ->dog ->cat'

def test_Animal_Shelter_no_dogs():
	animal_shelter = Animal_Shelter()
	animal_shelter.welcome_in('cat')
	animal_shelter.welcome_in('cat')
	animal_shelter.welcome_in('cat')
	animal_shelter.welcome_in('cat')
	assert animal_shelter.adoption_out('dog') == 'There are no dogs left.'

def test_Animal_Shelter_adopt_first(default_shelter):
	default_shelter.adoption_out('dog')
	assert str(default_shelter) == 'cat ->cat ->cat ->dog ->dog ->cat'

def test_Animal_Shelter_adopt_not_first(default_shelter):
	default_shelter.adoption_out('cat')
	assert str(default_shelter) == 'dog ->cat ->cat ->dog ->dog ->cat'

def test_Animal_Shelter_adopt_no_preference(default_shelter):
	default_shelter.adoption_out()
	assert str(default_shelter) == 'cat ->cat ->dog ->dog ->cat'

def test_Animal_Shelter_wrong_animal_given():
	animal_shelter = Animal_Shelter()
	with pytest.raises(InvalidOperationError):
		animal_shelter.welcome_in('penguin')

def test_Animal_Shelter_wrong_animal_requested():
	animal_shelter = Animal_Shelter()
	with pytest.raises(InvalidOperationError):
		animal_shelter.adoption_out('penguin')

def test_Animal_Shelter_nothing_to_adopt():
	animal_shelter = Animal_Shelter()
	with pytest.raises(InvalidOperationError):
		animal_shelter.adoption_out('dog')

@pytest.fixture
def default_shelter():
	animal_shelter = Animal_Shelter()
	animal_shelter.welcome_in('dog')
	animal_shelter.welcome_in('cat')
	animal_shelter.welcome_in('cat')
	animal_shelter.welcome_in('cat')
	animal_shelter.welcome_in('dog')
	animal_shelter.welcome_in('dog')
	animal_shelter.welcome_in('cat')
	return animal_shelter