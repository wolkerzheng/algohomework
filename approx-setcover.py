#encoding=utf8

import random as rd
import copy
import time
import matplotlib.pyplot  as plt
def createSet(x):
    """
    生成数据集
    :param x:
    :return:
    """
    F = [set([]) for _ in range(x)]
    Cover = set([])
    Total = set([i+1 for i in range(x)])
    F[0] = F[i]|set(rd.sample(Total,20))
    Cover = Cover|F[0]
    Uncover = Total - Cover
    i = 1
    while len(Uncover)>20:
        n = rd.randint(1,20)
        m = rd.randint(1,n)
        # print n,m
        F[i] = F[i]|set(rd.sample(Uncover,m))
        F[i] = F[i]|set(rd.sample(Cover,n-m))
        Cover = Cover |F[i]
        Uncover = Uncover-F[i]
        i += 1
    F[i] = F[i]|Uncover
    i+=1
    while i<x:
        F[i] = F[i]|set(rd.sample(Total,rd.randint(1,20)))
        i+=1
    # print len(F)
    return F
def selectLargeInter(F,U):
    maxNum = 0
    idx = 0
    for i in xrange(len(F)):
        if maxNum<len(F[i]&U):
                maxNum = len(F[i]&U)
                idx = i
    return F[idx]
def greedySetCover(x,F):
    U = set([i+1 for i in range(x)])
    copyF = copy.deepcopy(F)
    C = []
    C_idx = []
    while U:
        s = selectLargeInter(F,U)
        C.append(s)
        copyF.remove(s)
        U = U - s
        C_idx.append(F.index(s))
    return C

def approxGreedyCoverSet(x,F):
    """
    对偶拟合
    :param x:
    :param F:
    :return:
    """
    U = set([i+1 for i in range(x)])
    F_1 = set([])
    S = copy.deepcopy(F)
    C = []
    while len(F_1)!=len(U):
        s = selectS(S,F_1)
        C.append(s)
        F_1 = F_1 | s
        S.remove(s)
        # print S
    # print len(C),C
    return C

def selectS(S,F):
    """
    每次选覆盖最大的
    :param S:
    :param F:
    :return:
    """
    maxNum = 0
    resS = set()
    for s in S:
        if maxNum<len(s-F):
            resS = s
            max = len(s-F)
    return resS
def Primal_dual_Schema(U,S):
    """
    原偶
    :param U: 有限集
    :param S: 集族
    :return:
    """
    # print('基于 Primal-dual Schema的集合覆盖近似算法')
    #向量，S中的每个集合S对应一个分量 xs
    X = [0 for _ in range(len(S))]
    #向量， U中的每个元素 e对应一个分量 ye
    Y = [0 for _ in range(U)]
    Cost = [1 for _ in  range(len(S))]
    #/*记录被覆盖的子集*/
    F = set([])
    Uncover = set([i+1 for i in range(x)])
    while len(F) != U:
        unCoverNum = Uncover-F
        e0 = list(unCoverNum)[rd.randint(0,len(unCoverNum)-1)]
        Y[e0-1] = 1
        res = []
        # while len(res)==0:
        for s in xrange(len(S)):
            sumNum = 0
            for e in S[s]:
                sumNum += Y[e-1]
            if sumNum == Cost[s-1] and X[s]!=1:
                res.append(s)
        # print res
        for s in res:
            X[s] = 1
            F = F|S[s]
    C = [S[i] for i in range(len(X)) if X[i] == 1]
    # print len(C),C
    return C

if __name__ == '__main__':

    X = [100,1000,5000]
    # X = [100]
    y1 = []
    y2 = []
    y3 = []
    x1 = [i for i in range(len(X))]
    y4 = []
    y5 = []
    y6 = []
    for x in X:
        print ' 有限集 X :',x
        F =  createSet(x)
        # print len(F)
        # print '基于贪心策略的近似算法'
        s1 = time.clock()
        C1 = greedySetCover(x,F)

        s2 = time.clock()
        # print '基于线性规划的近似算法'
        s3 = time.clock()
        C2 = approxGreedyCoverSet(x,F)
        s4 = time.clock()
        C3 = Primal_dual_Schema(x,F)
        s5 = time.clock()
        y1.append(s2-s1)
        y2.append(s4-s3)
        y3.append(s5-s4)
        y4.append(len(C1))
        y5.append(len(C2))
        y6.append(len(C3))
        # break
    plt.figure('Runing Time')
    plt.plot(x1, y4, 'r',label='Greedy')
    plt.plot(x1, y5, 'g',label='DONH')
    plt.plot(x1, y6, 'y',label='Dual')
    print y1,y2,y3
    print y4,y5,y6
    plt.xlabel('Sizes')
    plt.ylabel('time')
    # plt.xlim(0.0,7.0)
    plt.legend(loc='upper left')
    plt.show()