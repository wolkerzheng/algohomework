#encoding=utf8
import random as rd
import time
import math
import copy
import matplotlib.pyplot  as plt


class Graph(object):

    def __init__(self, nodenum, weight=False,weightNum=100):

        self.__nodenum = nodenum
        self.__weight = weight
        self.__weightNum = weightNum
        print '图中节点数：', self.__nodenum
        self.__adjmat = self.__rdCreateGraph()


    def __rdCreateGraph(self):
        adjMat = [[0 for _ in xrange(self.__nodenum)] for _ in xrange(self.__nodenum)]
        if not self.__weight:

            # print '随机无向图的邻接矩阵表示'
            N = self.__nodenum *(self.__nodenum-1) / 2
            # 无向连通图至少需要n-1条边
            Linksnum = rd.randint(self.__nodenum, N)
            print '图中边数：', Linksnum
            n = 0
            while n < Linksnum:
                x = rd.randint(0,self.__nodenum-1)
                y = rd.randint(0,self.__nodenum-1)
                if x == y:
                    continue
                if adjMat[x][y] == 0:
                    adjMat[x][y],adjMat[y][x] = 1,1
                    n += 1
            print '随机生成无权无向图：'
            for i in xrange(self.__nodenum):
                for j in xrange(self.__nodenum):
                    print adjMat[i][j],
                print
        else:
            adjMat = [[ float('inf') for _ in range(self.__nodenum)] for _ in range(self.__nodenum)]
            for i in range(self.__nodenum):
                for j in range(i+1,self.__nodenum):
                    adjMat[i][j] = rd.randint(1,self.__weightNum )
                    adjMat[j][i] = adjMat[i][j]
            for j in range(self.__nodenum):
                adjMat[j][j] = float('inf')
            print '随机生成加权完全无向图：'
            for i in xrange(self.__nodenum):
                for j in xrange(self.__nodenum):
                    print adjMat[i][j],
                print
        return adjMat

    def getAdjMat(self):

        return self.__adjmat


class pathNode:
    """
    搜索队列存储的节点信息
    """
    #记录节点路径

    def __init__(self,idx=-1,pathway=None,v = 0):
        self.idx = idx
        self.pathway = pathway
        self.v = v
class TreeNode:

    def __init__(self,depth,idx,p):
        self.depth = depth
        self.idx = idx
        self.path = p
        pass


def isPath(n, pathway):
    """
    是否为一条路径
    :param n:
    :param pathway:
    :return:
    """
    # print 'pathway:',pathway
    if len(pathway) == n:
            return True
    return False

def isNotVisit(cur,j):
    """
    判断是否访问过该节点j
    :param adjMat: 邻接矩阵
    :param cur:
    :param j:
    :return:
    """
    if cur.idx not in cur.pathway:
        # print '....'
        return True
    return False

def BFS(root,adjMat,n):
    """
    广度优先遍历
    :param root:
    :param adjMat:
    :param n:
    :return:
    """
    queue = []
    #根节点入队
    queue.append(root)
    while queue:
        cur = queue.pop(0)      #出队列
        # print cur.pathway
        way = copy.deepcopy(cur.pathway)
        way.append(cur.idx)
        for j in xrange(n):
            if adjMat[cur.idx][j] == 1:
                if root.idx == j and isPath(n, way):
                    print '广度优先搜索生成路径：',way
                    return True
                if j not in way:
                    t = pathNode(j,way)
                    queue.append(t)
                # print way
    print 'BFS否'
    return False

def DFS(root,adjMat,n):
    """
    :param root:
    :param adjMat:
    :param n:
    :return:
    """
    stack = []
    stack.append(root)
    while stack!=[]:
        cur = stack.pop(-1)
        if cur.idx == root.idx and isPath(n,cur.pathway):
            print '深度优先搜索生成路径：',cur.pathway
            return True
        for i in xrange(n-1,-1,-1):
            if adjMat[cur.idx][i] == 1 and isNotVisit( cur, i) == True:
                way = copy.deepcopy(cur.pathway)
                way.append(cur.idx)
                tmpNode = pathNode(i, way)
                stack.append(tmpNode)
    print 'DFS否'
    return False

def clibm(start,adjMat,n,weigh=False):

    stack = []
    stack.append(start)

    while stack:
        cur = stack.pop(-1)
        if cur.idx == start.idx and isPath(n,cur.pathway):
            print '爬山法生成路径：',cur.pathway
            if weigh:
                W = getWeight(start,adjMat,cur.pathway)
                print '爬山法生成权重：',W
                return W
            return True
        curChild = heuristic(cur,adjMat,n,weigh)
        #启发度从大到小入栈
        for c in curChild:
            if c:
                stack.append(c)
    print '爬山法：否'
    return False
    pass
def heuristic(cur,adjMat,n,weigh=False):
    childNode = []
    #选择可以走通的下一个点的集合
    for i in xrange(n):
        if not weigh:
            if adjMat[cur.idx][i] == 1 and cur.idx not in cur.pathway:
                way = copy.deepcopy(cur.pathway)
                way.append(cur.idx)
                count = 0
                #无权图时，启发度按其下一个节点可扩展的数
                for j in xrange(n):
                    if adjMat[j][i] == 1  and i not in way:
                        count += 1
                tmpNode = pathNode(i, way,count)
                childNode.append(tmpNode)
        else:
            if adjMat[cur.idx][i]!= float('inf') and cur.idx not in cur.pathway:
                way = copy.deepcopy(cur.pathway)
                way.append(cur.idx)
                tmpNode = pathNode(i, way,adjMat[cur.idx][i])
                childNode.append(tmpNode)
    # 排序返回
    i = 1
    while i < len(childNode):
        j = i
        while j > 0 and childNode[j].v > childNode[j-1].v:
            childNode[j],childNode[j-1] = childNode[j-1],childNode[j]
            j = j - 1
        i += 1
    return childNode

def getWeight(root,adjmat,way):
    res = 0
    for i in range(1,len(way)):
         res += adjmat[way[i]][way[i-1]]
    res += adjmat[way[i]][root.idx]
    return res

def testH1(n):
    y1 = []
    y2 = []
    y3 = []
    x = []
    for i in xrange(len(n)):
        g = Graph(n[i])
        adjMat = g.getAdjMat()
        root = pathNode(0,[])
        # print root.idx,root.pathway
        # print '深度优先搜索'
        s1 = time.clock()
        DFS(root,adjMat,n[i])
        s2 = time.clock()
        # print '广度优先搜索：'
        BFS(root,adjMat,n[i])

        clibm(root,adjMat,n[i],weigh=False)
        s3 = time.clock()
        y1.append(s2-s1)
        y2.append(s3-s2)
        x.append(i)
    drawPicture(x,y1,y2,'Hamiltonian')

def drawPicture(x1, y1, y2,titlet):
    print y1
    print y2
    plt.figure('Hamilton')
    plt.plot(x1, y1, 'r',label='DFS')
    plt.plot(x1, y2, 'g',label='BFS')
    plt.title(titlet)
    plt.xlabel('times')
    plt.ylabel('time')
    plt.xlim(0.0,7.0)
    plt.legend()
    plt.show()

def branchBound(root,adjMat,n,boundVal):
    stack = []
    stack.append(root)
    minVal = boundVal
    minPath = []
    while stack!=[]:
        cur = stack.pop(-1)
        if cur.idx == root.idx and isPath(n,cur.pathway):
            if cur.v < minVal:
                minVal = cur.v
                minPath = cur.pathway
        for i in xrange(n-1,-1,-1):
            if cur.idx != i and isNotVisit( cur,i) == True:
                val = cur.v + adjMat[cur.idx][i]
                if val > minVal:
                    continue            #剪枝
                else:
                    way = copy.deepcopy(cur.pathway)
                    way.append(cur.idx)
                    tmpNode = pathNode(i, way,val)
                    stack.append(tmpNode)
    print '分支界限搜索生成路径：',minPath
    print '分支界限搜索最小哈密顿环：', minVal
    return minVal

def teshH2(n):
    y1 = []
    y2 = []
    y3 = []
    x = []
    for i in xrange(len(n)):
        g = Graph(n[i],weight=True)
        adjMat = g.getAdjMat()
        print '爬山法：'
        root = pathNode(0,[])
        s1 = time.clock()
        boundVal = clibm(root,adjMat,n[i],weigh=True)
        s2 = time.clock()
        branchBound(root,adjMat,n[i],boundVal)
        e1 = time.clock()
        y1.append(s2-s1)
        y2.append(e1-s2)
        x.append(i)

    plt.figure('minHamitonRunningTime')
    plt.plot(x, y1, 'r',label='ClimbHill')
    plt.plot(x, y2, 'g',label='BranchBound')
    # plt.title(titlet)
    plt.xlabel('times')
    plt.ylabel('time')
    # plt.xlim(0.0,7.0)
    plt.legend(loc='upper left')
    plt.show()
        # t = Tree(g)

if __name__ == '__main__':
    n = [8, 9,10,11,12,13]
    # n = [8,8,8,10]
    # n = [8,9,10,11,12]
    # testH1(n)
    teshH2(n)