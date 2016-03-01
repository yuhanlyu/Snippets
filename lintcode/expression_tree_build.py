"""
Definition of ExpressionTreeNode:
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None
"""


class Solution:
    # @param expression: A string list
    # @return: The root of expression tree
    def build(self, expression):
        def append():
            node, right, left = op.pop(), stack.pop(), stack.pop()
            node.left, node.right = left, right
            stack.append(node)
        stack, op = [], []
        for token in expression:
            if token == "(":
                op.append(ExpressionTreeNode(token))
            elif token in "+-":
                while op and op[-1].symbol != "(":
                    append()
                op.append(ExpressionTreeNode(token))
            elif token in "*/":
                while op and op[-1].symbol in "*/":
                    append()
                op.append(ExpressionTreeNode(token))
            elif token == ")":
                while op and op[-1].symbol != "(":
                    append()
                op.pop()
            else:
                stack.append(ExpressionTreeNode(token))
        while op:
            append()
        return stack[-1] if stack else None
