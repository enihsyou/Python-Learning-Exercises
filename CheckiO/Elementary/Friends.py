"""
File name: Friends
Reference: https://checkio.org/mission/friends/
Time: 2016-05-07
By: enihsyou
"""
from functools import reduce


class Friends:
    def __init__(self, connections):
        self.connections = list(connections)  # ({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
        self.node = {a: '' for i, a in  # id: root  {'a': '', 'b': 'a'}
                     enumerate(reduce(lambda a, b: a.union(b), self.connections))}
        # print(self.node)
        # for item in self.connections:

    def _search_root(self, dit, root):
        # if dit[id] != '':
        #     root = dit[id]
        #     self._search_root(dit, root)
        while dit[root] != '': root = dit[root]
        return root

    def _unite(self, a, b):
        root_a = self.search_root(a)
        # root_b = self.search_root(b)
        self.node[b] = root_a

    def _find(self, a, b):
        return self.search_root(a) == self.search_root(b)

    def add(self, connection):
        if connection not in self.connections:
            self.connections = self.connections + [connection]
            return True
        return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        return reduce(lambda a, b: a.union(b), self.connections)

    def connected(self, name):
        result = set()
        for item in self.connections:
            if name in item:
                result.update(item - {name})
        return result


if __name__ == '__main__':
    f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
    f.connected("nikola")
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
