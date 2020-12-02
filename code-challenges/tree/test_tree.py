import pytest
from tree import Node, BinaryTree

def test_empty_tree():
	xmas = BinaryTree()
	assert xmas.head is None

def test_single_root():
	xmas = BinaryTree(Node(35))
	assert xmas.head.value == 35

def test_contains(default_tree):
	assert default_tree.contains(60)
	assert not default_tree.contains(100)

def test_root_children():
	xmas = BinaryTree(Node(35))
	xmas.add(20)
	xmas.add(60)
	assert xmas.head.left and xmas.head.right

def test_preOrder_return(default_tree):
	assert default_tree.preOrder() == [35, 20, 10, 2, 18, 24, 22, 28, 60, 45, 43, 55, 90, 77, 99]

def test_inOrder(default_tree):
	assert default_tree.inOrder() == [2, 10, 18, 20, 22, 24, 28, 35, 43, 45, 55, 60, 77, 90, 99]

def test_postOrder(default_tree):
	assert default_tree.postOrder() == [2, 18, 10, 22, 28, 24, 20, 43, 55, 45, 77, 99, 90, 60, 35]

@pytest.fixture
def default_tree():
	xmas = BinaryTree(Node(35))
	xmas.add(20)
	xmas.add(60)
	xmas.add(10)
	xmas.add(24)
	xmas.add(2)
	xmas.add(18)
	xmas.add(22)
	xmas.add(28)
	xmas.add(45)
	xmas.add(90)
	xmas.add(43)
	xmas.add(55)
	xmas.add(77)
	xmas.add(99)
	#           35
	#     20          60
	#  10    24    45    90
	# 2 18  22 28 43 55 77 99
	return xmas