# Linked Lists

## Challenge
Create a node class and a linked list class that keeps track of sequential order for objects of the class

## Approach & Efficiency
I set up the initial Node class to take in the value and a next property that are defaulted as None, and also gave it a str method to return its value in a string format. Next I created the LinkedList class with a value of head that is initiated as None and then a str method, insert, and includes method. The insert method creates a variable of a Node instance with the current head value as its next value, and then assigns the new value to the head. The includes method checks for a mtaching value starting from the head and then to each next value until it encounters a None and then returns False. Lastly the str method creates a variable with initial value of the heads value in string format and then adds each next value in string format with a -> attached beforehand.