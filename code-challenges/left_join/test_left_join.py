from left_join import HashTable, left_join
import pytest

def test_left_join_happy(default_tables):
	result = left_join(default_tables[0], default_tables[1])
	assert ['dirty', 'filthy', 'clean'] in result
	assert ['wall', 'barricade', 'opening'] in result
	assert ['double', 'copy', None] in result
	assert ['comfortable', 'pleasant', 'disagreeable'] in result

def test_left_join_larger_second_table(default_tables):
	T1 = default_tables[0]
	T2 = default_tables[1]
	T2.set('hostile', 'friendly')
	T2.set('addicted', 'indifferent')
	T2.set('hypnotize', 'disenchant')
	result = left_join(T1, T2)
	assert ['dirty', 'filthy', 'clean'] in result
	assert ['wall', 'barricade', 'opening'] in result
	assert ['double', 'copy', None] in result
	assert ['comfortable', 'pleasant', 'disagreeable'] in result

def test_left_join_empty_first_table(default_tables):
	T1 = HashTable(4)
	T2 = default_tables[1]
	assert left_join(T1, T2) == []

@pytest.fixture
def default_tables():
	T1 = HashTable(4)
	T2 = HashTable(3)
	T1.set('wall', 'barricade')
	T2.set('wall', 'opening')
	T1.set('dirty', 'filthy')
	T2.set('dirty', 'clean')
	T1.set('double', 'copy')
	T1.set('comfortable', 'pleasant')
	T2.set('comfortable', 'disagreeable')
	return (T1, T2)