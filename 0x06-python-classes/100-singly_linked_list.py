#!/usr/bin/python3
"""task 100"""


class Node:
    """node"""
    def __init__(self, data, next_node=None):
        """def init Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve data"""
        return self.__data

    @data.setter
    def data(self, data):
        """set data value"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """def next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """node setter"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        """init linked list"""
        self.__head = None
