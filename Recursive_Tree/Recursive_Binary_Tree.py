class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None

	def __r_insert(self, current_node, value):
		if current_node == None:
			return Node(value)
		if value < current_node.value:
			current_node.left = self.__r_insert(current_node.left, value)
		if value > current_node.value:
			current_node.right = self.__r_insert(current_node.right, value)
		return current_node

	def r_insert(self, value):
		if self.root == None:
			self.root = Node(value)
		self.__r_insert(self.root, value)

	def min_value(self, current_node):
		while (current_node.left is not None):
			current_node = current_node.left
		return current_node.value

	def __delete_node(self, current_node, value):
		if current_node is None:
			return None
		if value < current_node.value:
			current_node.left = self.__delete_node(current_node.left, value)
		elif value > current_node.value:
			current_node.right  = self.__delete_node(current_node.left, value)
		else:
			if current_node.left is None and current_node.right is None:
				return None
			elif current_node.left is None:
				current_node = current_node.right
			elif current_node.right is None:
				current_node = current_node.left
			else:
				min_value = self.min_value(current_node.right)
				current_node.value = min_value
				current_node.right = self.__delete_node(current_node.right, min_value)
		return current_node

	def delete_node(self, value):
		self.__delete_node(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)

my_tree.delete_node(2)

print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)
