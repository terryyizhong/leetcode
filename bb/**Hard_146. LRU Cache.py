'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
# classic solution using dict and double-linkedlist
    
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        new = Node(key, value)
        if key in self.dic:
            self._remove(self.dic[key])
        elif len(self.dic) == self.cap:
            self.dic.pop(self.head.next.key)
            self._remove(self.head.next)
        self._add(new)
        self.dic[key] = new
        
    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def _add(self, node):
    #        self.tail.prev.next, self.tail.prev, node.next, node.prev = node, node, self.tail, self.tail.prev

        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
# short solution use OrderedDict,
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.cap = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        val = self.dic[key]
        self.dic.pop(key)
        self.dic[key] = val
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.dic.pop(key)
        elif len(self.dic) == self.cap:
                self.dic.popitem(last=False)
        self.dic[key] = value
