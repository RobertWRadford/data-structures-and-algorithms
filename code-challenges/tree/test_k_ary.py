import pytest
from k_ary_tree import Node, KaryTree

def test_tree_structure(default_tree):
	assert [default_tree.head.children[0].children[i].value for i, values in enumerate(default_tree.head.children[0].children)] == [5,6,7]
	assert [default_tree.head.children[0].children[0].children[i].value for i, values in enumerate(default_tree.head.children[0].children)] == [14,15,16]

def test_contains(default_tree):
	assert default_tree.contains(23)
	assert not default_tree.contains(80)

def test_postOrder(default_tree):
	assert default_tree.postOrder() == [14, 15, 16, 5, 17, 18, 19, 6, 20, 21, 22, 7, 2, 23, 24, 25, 8, 26, 27, 28, 9, 29, 30, 31, 10, 3, 32, 33, 34, 11, 35, 36, 37, 12, 38, 39, 40, 13, 4, 1]

def test_preOrder(default_tree):
	assert default_tree.preOrder() == [1, 2, 5, 14, 15, 16, 6, 17, 18, 19, 7, 20, 21, 22, 3, 8, 23, 24, 25, 9, 26, 27, 28, 10, 29, 30, 31, 4, 11, 32, 33, 34, 12, 35, 36, 37, 13, 38, 39, 40]

@pytest.fixture
def default_tree():
	kTree = KaryTree(3, [i for i in range(1, 41)])
	#																			1
	#					2														3														4
	#	5				6				7						8				9				10						11				12				13
	#14	15	16		17	18	19		20	21	22				23	24	25		26	27	28		29	30	31				32	33	34		35	36	37		38	39	40
	return kTree