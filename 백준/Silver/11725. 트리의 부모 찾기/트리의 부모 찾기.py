import sys
sys.setrecursionlimit(10**6)  
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # 연결된 노드 번호들

class Tree:
    def __init__(self, n):
        self.nodes = [None] + [Node(i) for i in range(1, n+1)]  # index 1부터 시작
        self.parent = [0] * (n + 1)  # 각 노드의 부모 저장

    def add_edge(self, a, b):
        self.nodes[a].neighbors.append(b)
        self.nodes[b].neighbors.append(a)

    def dfs(self, current, parent):
        self.parent[current] = parent
        for neighbor in self.nodes[current].neighbors:
            if neighbor != parent:  # 방문하지 않은 노드라면
                self.dfs(neighbor, current)

    def print_parents(self):
        self.dfs(1, 0)  # 루트는 1번 노드, 부모는 0
        for i in range(2, len(self.parent)):
            print(self.parent[i])

# 입력 받기
n = int(input())
tree = Tree(n)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree.add_edge(a, b)

tree.print_parents()
