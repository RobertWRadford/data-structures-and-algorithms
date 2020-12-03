import pytest
from tree_non_search import Node, BinaryTree, Queue, Stack

def test_can_form_tree(default_tree):
	assert default_tree.head.right.left.value == 17
	assert default_tree.head.left.left.right.value == 3

def test_can_find_max(default_tree):
	assert default_tree.find_max() == 19

def test_max_of_empty(default_tree):
	xmas = BinaryTree()
	assert xmas.find_max() is None

def test_return_all_nodes(default_tree):
	assert default_tree.traverse_tree() == [5,3,6,8,10,17,19,1,3]

@pytest.fixture
def default_tree():
	xmas = BinaryTree()
	xmas.add(5)
	xmas.add(3)
	xmas.add(6)
	xmas.add(8)
	xmas.add(10)
	xmas.add(17)
	xmas.add(19)
	xmas.add(1)
	xmas.add(3)
	#            5
	#      3           6
	#   8     10    17     19
	# 1   3
	return xmas