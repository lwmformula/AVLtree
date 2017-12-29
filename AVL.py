
# coding: utf-8

# In[ ]:


import time

####################### Reading data #######################
start = time.time()
import sys
import os

td = 15
dividefac = 20
instmp = []
qrytmp = []
qryval = []
rawlist2 = []
filepath = sys.argv[1]
output = os.getcwd() + '/' + 'output.txt'

f = open(filepath,'r')
raw = f.readlines()
####################### Reading data #######################
######################### AVL Tree #########################
class createNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
class avl(object):
    def createAVL(self,arr,l,r):
        if l == r:
            return None
        m = (l+r) >> 1
        node = createNode(arr[m])
        node.left = self.createAVL(arr,l,m)
        node.right = self.createAVL(arr,m+1,r)
        return node
    
    def avlinit(self, arr):
        return self.createAVL(arr,0,len(arr))
    
#Query function   
def qryinit(init,num):
    tmpqry = []
    if init.val == num:
        return init.val
    else:
        tmpqry.append(init.val)
        return qry(init,num,tmpqry)
    
def qry(nextnode,num,tmpqry):
    if nextnode == None:
        cls = [i for i in tmpqry if i < num]
        if len(cls) == 0: return -999999
        else: return max(cls)
        
    elif nextnode.val == num:
        return nextnode.val
        
    elif nextnode.val < num:
        tmpqry.append(nextnode.val)
        nextnode = nextnode.right
        return qry(nextnode,num,tmpqry)

    elif nextnode.val > num:
        tmpqry.append(nextnode.val)
        nextnode = nextnode.left
        return qry(nextnode,num,tmpqry)
######################### AVL Tree #########################
######################## Quick Sort ########################
def choose(ctmp,begin,end):
    for i in range (begin, end):
        cdex = i
        for j in range (i+1, end+1):
            if ctmp[j] < ctmp[cdex]: cdex = j
        if cdex != i: ctmp[i],ctmp[cdex] = ctmp[cdex], ctmp[i]
            
def divf(rawtmp,smallest,largest):
    ddex = piv(rawtmp,smallest,largest)
    val = rawtmp[ddex]
    rawtmp[ddex], rawtmp[smallest] = rawtmp[smallest], rawtmp[ddex]
    limit = smallest

    for i in range(smallest, largest+1):
        if rawtmp[i] < val:
            limit += 1
            rawtmp[i], rawtmp[limit] = rawtmp[limit], rawtmp[i]
    rawtmp[smallest], rawtmp[limit] = rawtmp[limit],rawtmp[smallest]
    return limit

def piv(rawtmp,smallest,largest):
    m = (largest+smallest) // 2
    ptmp = sorted([rawtmp[smallest],rawtmp[largest],rawtmp[m]])
    if ptmp[1] == rawtmp[smallest]: return smallest
    elif ptmp[1] == rawtmp[m]: return m
    return largest

def qs(rawtmp):
    qstmp(rawtmp,0,len(rawtmp)-1)
    
def qstmp(rawtmp,smallest,largest):
    if largest-smallest < td and smallest < largest: choose(rawtmp, smallest, largest)
    elif smallest < largest:
        div = divf(rawtmp, smallest, largest)
        qstmp(rawtmp, smallest, div - 1)
        qstmp(rawtmp, div + 1, largest)
######################## Quick Sort ########################
##################### Data Preprossing #####################
atree = avl()
def classifyqry(tmp):
    sigh = tmp.split('\n')[0]
    if sigh[0:3] == 'ins': instmp.append(int(sigh.split(' ')[1]))
    elif sigh[0:3] == 'qry':
        qrytmp.append(raw.index(tmp))
        qryval.append(int(sigh.split(' ')[1]))
        instmp.append('qry')
        
def totree(varwhole):
    loopv = len(varwhole) / dividefac
    for j in range(0,len(varwhole),loopv):
        clss = varwhole[j:j+loopv]
        qs(clss)
        pretre = atree.avlinit(clss)
        dnq.append(pretre)

map(classifyqry,raw)
dnq = []
totree(instmp[0:qrytmp[0]])
for i in qrytmp:
    try:
        var = instmp[i+1:qrytmp[(qrytmp.index(i)+1)]]
        totree(var)
    except:
        break
##################### Data Preprossing #####################
for i in qryval:
    qryindex = qryval.index(i)
    tree = dnq[0:(qryindex+1)*dividefac]
    suit = list(map(lambda t: qryinit(t,i),tree))
    with open(output,'a') as final:
        final.write(str(max(suit)) + '\n')
    
end = time.time()
print 'Time used: ', end - start

