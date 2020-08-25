from pyqueue import Queue
def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
        while simqueue.size() > 1:
            for i in range(num):
                simqueue.enqueue(simqueue.dequeue())
                simqueue.dequeue()
        return simqueue.dequeue()
print(hotPotato(["Aung Aung","Mg Mg","Thida","Thin Thin","Ko Ko","Hla Hla"],8))
