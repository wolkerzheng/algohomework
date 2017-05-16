# algrohomework
算法实验课作业
## 搜索策略
（1）求解哈密顿环问题：输入是一个无向连通图G=(V,E)；如果G中存在哈密顿环则输出该环，否则输出“否”。
（2）求解最小哈密顿环问题：输入是一个无向连通图G=(V,E)，每个节点都没有到自身的边，每对节点间都有一条非负加权边；输出一个权值代价和最小的哈密顿环。注意：事实上输入图是一个完全图，因此哈密顿环是一定存在的。
DFS算法描述：
1. 构造一个由根构成的单元素栈S;
2. If Top(S)是目标节点
3. Then 输出解，停止 ;
4. ELSE T＝ Top(S), Pop(S);
5. 把T的所有子节点压入栈顶 ;
6. If S空 Then 无解;
7. Else goto 2.

BFS算法描述：
1. 构造仅由根组成的队列 Q;
2. IF Q的第一个元素x是目标节点
3. Then 输出解,停止 ;
4. ELSE 从Q中删除x， 把x的所有
子节点加入Q的末尾;
5. IF Q空 Then 无解
6. Else goto 2.

爬山法描述：
爬山策略使用贪心方法确定搜索的方向,是优化的深度优先搜索策略
伪代码：
1. 构造由根组成的单元素栈S;
2. If Top(S)是目标节点 Then 停止 ;
3. Pop(S);
4. S的子节点按照其启发测度由大到
小的顺序压入S;
5. If S空 Then 失败 Else goto 2.

分支界限法描述：
– 产生分支的机制 (使用了爬山法，爬山策略为按下个节点可以扩展的权重从大到小入栈)
– 产生一个界限(用爬山法产生的界限)
– 进行分支界限搜索, 即剪除不可能产生优化解的分支.

## 近似算法
集合覆盖问题：
输入：有限集X，X的子集合族F,X =∪s∈F S
输出：CF,满足
	（1）X =∪s∈F S
	（2）C是满足条件（1）的最小集族，即|C|最小

生成数据集，运用以下两种方法
1.实现基于贪心策略的近似算法
2.实现一个基于线性规划的近似算法
测试在|X|=|F|=100、 1000、 5000 情况，可行解方案

基于贪心策略的近似算法
  思想：每次选择能覆盖最多未被覆盖元素的子集。近似比为ln|X|+1。
伪代码：
Greedy-Set-Cover(X, F)
1. UX; /* U是X中尚未被覆盖的元素集 */
2. C;
3. While U Do
4. Select SF 使得S∩U最大;
/* Greedy选择—选择能覆盖最多 U元素的子集S */
5. UU-S;
6. CC∪ S; /* 构造X的覆盖 */
7. Return C.

基于线性规划的近似算法
Primal-dual Schema思想：
对F中的每个集合S，引入一个变量 xS
xS=0 表示SC ， xS=1 表示SC
集合覆盖问题表示为整数规划
