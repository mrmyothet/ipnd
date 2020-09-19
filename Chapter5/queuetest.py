from pyqueue import Queue
q=Queue()
q.enqueue(6)
q.enqueue('cat')
q.enqueue(True)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.size())
