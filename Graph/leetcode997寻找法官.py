"""
997. 找到小镇的法官
在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。
如果小镇的法官真的存在，那么：
小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。
示例 1：
输入：N = 2, trust = [[1,2]]
输出：2
示例 2：
输入：N = 3, trust = [[1,3],[2,3]]
输出：3
示例 3：
输入：N = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1
示例 4：
输入：N = 3, trust = [[1,2],[2,3]]
输出：-1
示例 5：
输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3
提示：
1 <= N <= 1000
trust.length <= 10000
trust[i] 是完全不同的
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""

"""
思路：
1、统计每个节点的入度
    如果满足只有一个节点的入度 = N-1
    则可以判断出法官
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        if len(trust) < n-1 or not trust:
            return -1
        inEdgeDict = {key:0 for key in range(1,n+1)}
        # judgeNum = 0
        judge = None
        candidates = [i for i in range(1,n+1)]
        for edge in trust:
            outNode,inNode = edge
            # if outNode in candidates:
            #     candidates.remove(outNode)
            inEdgeDict[inNode]  += 1
            if inEdgeDict[inNode] == n - 1:
                # judgeNum += 1
                judge = inNode
        if judge:
            if inEdgeDict[judge] == 0:
                return judge
        # if judgeNum == 1 and judge in candidates:
        #     return judge
        return -1