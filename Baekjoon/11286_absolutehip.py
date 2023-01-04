import sys
input = sys.stdin.readline

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Nodemanagement():
	def __init__(self, head):
		self.head = head

	def insert(self, value):
		self.current_node = self.head
		while True: # 각 노드를 순회
			if value < self.current_node.data:
				if self.current_node.left != None:
					self.current_node = self.current_node.left
				else:
					self.current_node.left = Node(value)
					break
			else:
				if self.current_node.right != None:
					self.current_node = self.current_node.right
				else:
					self.current_node.right = Node(value)
					break

n = int(input())

for _ in range(n):
	x = int(input())
