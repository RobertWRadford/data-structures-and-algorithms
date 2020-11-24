import pytest
from queue_with_stacks import Node, Stack, PseudoQueue

def test_PseudoQueue_init_stack():
	stack_one = Stack()
	stack_one.push(15)
	stack_one.push(10)
	stack_one.push(5)
	stack_one.push(0)
	queue = PseudoQueue(stack_one, Stack())
	actual = str(queue)
	expected = '0 ->5 ->10 ->15'
	assert actual == expected

def test_PseudoQueue_enqueue():
	stack_one = Stack()
	stack_one.push(10)
	stack_one.push(5)
	stack_one.push(0)
	queue = PseudoQueue(stack_one, Stack())
	queue.enqueue(15)
	actual = str(queue)
	expected = '0 ->5 ->10 ->15'
	assert actual == expected

def test_PseudoQueue_dequeue():
	stack_one = Stack()
	stack_one.push(15)
	stack_one.push(10)
	stack_one.push(5)
	stack_one.push(0)
	queue = PseudoQueue(stack_one, Stack())
	queue.dequeue()
	actual = str(queue)
	expected = '5 ->10 ->15'
	assert actual == expected

