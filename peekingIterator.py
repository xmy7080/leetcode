#lt solution with presaved _next element.
#the reason why we need self._next is that there is a self.next() func
#hence the iterator can be just self.iterator
class PeekingIterator:
    def __init__(self, iterator):
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        return self._next

    def next(self):
        if self._next is None:
            raise StopIteration()
        toReturn = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return toReturn

    def hasNext(self):
        return self._next is not None
