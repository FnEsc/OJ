#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-01-13 13:33:50
# @Author  : Simulink Lin (smlin97@outlook.com)
# @Link    : https://fnesc.github.io
# @Version : $Id$
# 初级算法
# LeetCode 官方推出的经典面试题目清单 —— 「初级算法 - 帮助入门」
# https://leetcode-cn.com/leetbook/detail/top-interview-questions-easy/


#---------- 数组 ----------#

#--->删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

#--->买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # 每一天设立两种状态，dp0为当天无股票的利润，dp1为当前有股票的利润
        # 新得一天只与前一天状态有关
        # dp0, dp1 = 0, -(prices[0])
        # for i in range(1, len(prices)):
        #     dp0 = max(dp0, dp1 + prices[i]) # max(上一天的两种情况到今天卖出)=>当前情况已获利润
        #     dp1 = max(dp0 - prices[i], dp1) # max(上一天的两种情况到今天持有)=>当前情况已获利润
        # return dp0
        
        # 贪心算法
        # 查找有利润的区间求和
        out = []
        for i in range(1, len(prices)):
            out.append(max(0, prices[i]-prices[i-1]))
        return sum(out)

#--->旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())

#--->存在重复元素
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums)==len(set(nums)) else True

#--->只出现一次的数字
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)

#--->两个数组的交集 II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)< len(nums2): nums1, nums2 = nums2, nums1 # nums1为较长数组
        from collections import Counter
        tcounter = Counter(nums1)
        out = []
        for i in nums2:
            if tcounter[i] > 0:
                out.append(i)
                tcounter[i] -= 1
        return out

#--->加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int("".join(map(str, digits)))+1).zfill(len(digits))))

#--->移动零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums)):
            if nums[i-zero_count] == 0:
                nums.pop(i-zero_count)
                nums.append(0)
                zero_count += 1

#--->两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ->常常出现在python函数定义的函数名后面, 为函数添加元数据, 描述函数的返回类型
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [hash_map[target - x], i]
            hash_map[x] = i

#--->有效的数独
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        from collections import Counter
        for rowindex in range(9):
            tcount = Counter(board[rowindex])
            tcount['.'] = 0
            if max(tcount.values()) > 1:
                return False
        # colunm
        for colunmindex in range(9):
            tcount = Counter([board[rowindex][colunmindex] for rowindex in range(9)])
            tcount['.'] = 0
            if max(tcount.values()) > 1:
                return False
        # box
        for boxrowindex in range(3):
            for boxcolumnindex in range(3):
                tmplist = []
                tmplist.append(board[boxrowindex*3+0][boxcolumnindex*3+0])
                tmplist.append(board[boxrowindex*3+0][boxcolumnindex*3+1])
                tmplist.append(board[boxrowindex*3+0][boxcolumnindex*3+2])
                tmplist.append(board[boxrowindex*3+1][boxcolumnindex*3+0])
                tmplist.append(board[boxrowindex*3+1][boxcolumnindex*3+1])
                tmplist.append(board[boxrowindex*3+1][boxcolumnindex*3+2])
                tmplist.append(board[boxrowindex*3+2][boxcolumnindex*3+0])
                tmplist.append(board[boxrowindex*3+2][boxcolumnindex*3+1])
                tmplist.append(board[boxrowindex*3+2][boxcolumnindex*3+2])
                tcount = Counter(tmplist)
                tcount['.'] = 0
                if max(tcount.values()) > 1:
                    return False
        return True

#--->旋转图像
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先从水平中间作为翻转
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        # 再从主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


#---------- 字符串 ----------#

#--->反转字符串
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

#--->整数反转
class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(x)[::-1]) if x >= 0 else int(str(x)[:0:-1])*-1
        return res if res in range(-2**31, 2**31) else 0

#--->字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        for item in Counter(s).items():
            if item[1] == 1:
                return s.index(item[0])
        return -1

#--->有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        ts = Counter(s)
        tt = Counter(t)
        return (ts-tt)==(tt-ts)

#--->验证回文串
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s if (i.isalpha() or i.isdigit())]).lower()
        return s == s[::-1]

#--->字符串转换整数 (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        return min(max(int(*re.findall('^[\-\+]?\d+', s.lstrip())), -2**31), 2**31-1)

#--->实现 strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if l == 0: return 0
        for i in range(len(haystack)-len(needle)+1):
            # 逐个字母判断
            # for j in range(len(needle)):
            #     if haystack[i+j] != needle[j]: break
            #     if (j == (len(needle)-1)) & (haystack[i+j] == needle[j]): return i
            # 其实更好应该使用切片判断，虽然都很低效率
            if haystack[i: i + l] == needle: return i
        return -1

#--->外观数列
class Solution:
    def countAndSay(self, n: int) -> str:
        # 迭代，前一个推出后一个
        # res = "1"
        # for _ in range(n-1):
        #     i, tmp = 0, '' # i表示每轮中对str的index
        #     for j, c in enumerate(nowstr):
        #         if c != res[i]:
        #             tmp += str(j-i) + res[i]
        #             i = j
        #     res = tmp + str(len(res) - i) + res[-1] # 子循环最后一个在这里加上
        # return res
        # 递归，向前一项索取结果后计算当次
        if n==1: return "1"
        s = self.countAndSay(n-1) # 第n次的结果由n-1次的结果进行以下计算返回
        i, res = 0, ''
        for j, c in enumerate(s):
            if c != s[i]:
                res += str(j-i) + s[i]
                i = j
        res += str(len(s) - i) + s[-1] # 子循环最后一个在这里加上
        return res

#--->最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        con = ""
        i = 0
        while 1:
            tmp_set = set([tmp_str[i:i+1] for tmp_str in strs])
            if (len(tmp_set) != 1) or (tmp_set == {''}):
                break
            con += tmp_set.pop()
            i += 1
        return con

#---------- 链表 ----------#

#--->删除链表中的节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next

#--->删除链表的倒数第N个节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针
        # 创建一个预头节点，指向链表的头
        dummy = ListNode(0, head)
        slowp = fastp = dummy
        for _ in range(n):
            fastp = fastp.next
        while fastp.next:
            slowp, fastp = slowp.next, fastp.next
        slowp.next = slowp.next.next
        return dummy.next

#--->反转链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

#--->合并两个有序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0, l1)
        p = dummy
        p1 = l1
        p2 = l2
        while 1:
            if p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p = p2
                    p2 = p2.next
            elif p1 and (p2==None):
                p.next = p1
                break
            else:
                p.next = p2
                break
        return dummy.next

#--->回文链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals, p = [], head
        while p:
            vals.append(p.val)
            p = p.next
        return vals == vals[::-1]

#--->环形链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 方法一，哈希表
        # p, hashset = head, set()
        # while p:
        #     if p in hashset:
        #         return True
        #     else:
        #         hashset.add(p)
        #         p = p.next
        # return False
        # 方法二，龟兔赛跑圈
        if not head or not head.next:
            return False
        slowp, fastp = head, head.next
        while slowp != fastp:
            # 判断空链/单字点，返回False
            # fast指向最后一个node或者倒数第二个node的next.next的None
            # 注意 if True or not define 不会报错
            if not fastp or not fastp.next: 
                return False
            slowp = slowp.next
            fastp = fastp.next.next
        return True


#---------- 树 ----------#

#--->二叉树的最大深度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归
        if root == None: return 0
        if root.left == root.right ==  None:
            return 1
        elif root.left == None:
            return self.maxDepth(root.right) + 1
        elif root.right == None:
            return self.maxDepth(root.left) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#--->验证二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 二叉搜索树是包括子节点的对比的
        # 中序遍历二叉树，或者自定递归
        # 注意Python中可以用如下方式表示正负无穷 float("inf"), float("-inf")
        # 下面使用递归遍历中序二叉树
        def recur(root):
            return recur(root.left) + [root.val] + recur(root.right) if root else []
        res = recur(root)
        return all([res[i]<res[i+1] for i in range(len(res)-1) ])

#--->对称二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        fls = [[root]]
        while any(fls[-1]):
            tmp = []
            for node in fls[-1]:
                if node == None:
                    tmp += [None, None]
                else:
                    tmp += [node.left, node.right]
            if [i.val if i else i for i in tmp] != [i.val if i else i for i in tmp][::-1]: 
                return False
            fls.append(tmp)
        return True

#--->二叉树的层序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        out = []
        cur_fls = [root]
        while cur_fls:
            cur_vals = []
            next_fls = []
            for node in cur_fls:
                if node:
                    cur_vals.append(node.val)
                    next_fls.append(node.left)
                    next_fls.append(node.right)
            if cur_vals:
                out.append(cur_vals)
            cur_fls = next_fls
        return out

#--->将有序数组转换为二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置右边的数字作为根节点
            mid = (left + right + 1) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1) # 从根节点直接开始


#---------- 排序和搜索 ----------#

#--->合并两个有序数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

#--->第一个错误的版本
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


#---------- 动态规划 ----------#

#--->爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归，超时
        # if n < 2 :
        #     return 1
        # else: # 最后走两步/走一步
        #     return self.climbStairs(n-2) + self.climbStairs(n-1)
        # 迭代
        p, q, r = 0, 0, 1
        for i in range(n):
            p, q = q, r
            r = p + q
        return r

#--->买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 暴力超时
        # l = len(prices)
        # salary_area = [prices[i] - prices[i - 1] for i in range(1, l)]
        # glo = [0]
        # for i in range(l-1):
        #     glo.append(max([sum(salary_area[i:j]) for j in range(l)]))
        # return max(glo)
        # 动态规划，从1起，计算可获取的最大和，注意此处num[i]的赋值
        # 等价于最大子序和
        salary_area = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        for i in range(1, len(salary_area)):
            salary_area[i] = max(salary_area[i-1]+salary_area[i], salary_area[i])
        salary_area.append(0)
        return max(salary_area)

#--->最大子序和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划，从1起，计算可获取的最大和，注意此处num[i]的赋值
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)

#--->打家劫舍
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        else:
            # v1
            # out = []  # dp0表示不偷后利润，dp1表示偷后利润
            # dp0 = dp1 = 0
            # for i in range(l):
            #     dp0, dp1 = max(dp0, dp1)+0, dp0+nums[i]
            #     out.append([dp0, dp1])
            # return max(out[-1])
            # v2
            dp0 = dp1 = 0
            for i in range(l):
                dp0, dp1 = max(dp0, dp1) + 0, dp0 + nums[i]
            return max(dp0, dp1)


#---------- 设计问题 ----------#

#--->打乱数组
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.l = len(self.nums)
        self.orgnums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orgnums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        for i in range(self.l):
            randindex = random.randrange(i, self.l)
            self.nums[i], self.nums[randindex] = self.nums[randindex], self.nums[i]
        return self.nums

#--->最小栈
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.olist = []
        self.omin = float('inf')

    def push(self, x: int) -> None:
        self.olist.append(x)
        if x < self.omin:
            self.omin = x

    def pop(self) -> None:
        opop = self.olist.pop()
        if opop == self.omin:
            self.omin = min(self.olist) if self.olist else float('inf')

    def top(self) -> int:
        return self.olist[-1]

    def getMin(self) -> int:
        return min(self.olist)


#---------- 数学 ----------#

#--->Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        outlist = [str(i) for i in range(n+1)]
        oFizz = 3
        while oFizz <= n:
            outlist[oFizz] = "Fizz"
            oFizz += 3
        oBuzz = 5
        while oBuzz <= n:
            outlist[oBuzz] = "FizzBuzz" if outlist[oBuzz] == "Fizz" else "Buzz"
            oBuzz += 5
        return outlist[1:]

#--->计数质数
class Solution:
    def countPrimes(self, n: int) -> int:
        # 判断枚举质数的方法
        if n < 2: return 0
        import math
        is_Prime = [1] * n
        is_Prime[0] = is_Prime[1] = 0
        for i in range(2, math.ceil(n ** 0.5)):  # 判断次数少于
            if is_Prime[i]:
                cur_num, step = i*2, i
                while cur_num < n:
                    is_Prime[cur_num] = 0
                    cur_num += step
        last_t = math.ceil(n ** 0.5)  # 追加最后一次的判断次数
        if last_t < n and is_Prime[last_t]:
            cur_num, step = last_t*2, last_t
            while cur_num < n:
                is_Prime[cur_num] = 0
                cur_num += step
        return sum(is_Prime)

#--->3的幂
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n = n//3
        return n == 1

#--->罗马数字转整数
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        d = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
            'M': 1000
        }
        i = 0
        while i < len(s):
            if s[i:i + 2] in d:
                res += d[s[i:i + 2]]
                i += 2
            else:
                res += d[s[i]]
                i += 1
        return res


#---------- 其他 ----------#

#--->位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

#--->汉明距离
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b = bin(x)[2:], bin(y)[2:]
        maxl = max(len(a), len(b))
        a, b = a.zfill(maxl), b.zfill(maxl)
        return sum([a[i] != b[i] for i in range(maxl)])

#--->颠倒二进制位
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)

#--->杨辉三角
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        else:
            out = [[1]]
        for i in range(numRows-1):
            cur_fls = out[-1]
            next_fls = [1] + [sum([cur_fls[j], cur_fls[j+1]]) for j in range(len(cur_fls)-1)] + [1]
            out.append(next_fls)
        return out

#--->有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        s, stack = list(s), []
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        while s:
            c = s.pop(0)
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if stack and d[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if stack else True

#--->缺失数字
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        misslen = len(nums)
        for i,num in enumerate(nums):
            misslen ^= (i^num)
        return misslen



