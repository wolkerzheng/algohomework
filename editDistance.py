#encoding=utf8

"""
if i == 0 且 j == 0，edit(i, j) = 0
if i == 0 且 j > 0，edit(i, j) = j
if i > 0 且j == 0，edit(i, j) = i
if i ≥ 1  且 j ≥ 1 ，
edit(i, j) == min{ edit(i-1, j) + 1, edit(i, j-1) + 1, edit(i-1, j-1) + f(i, j) }，
当第一个字符串的第i个字符不等于第二个字符串的第j个字符时，
f(i, j) = 1；否则，f(i, j) = 0。
"""
def main(strA,strB):


	lenA,lenB = len(strA),len(strB)
	#存储最大编辑距离
	dpMat = [[0 for _ in xrange(lenB+1)] for _ in xrange(lenA+1)]
	#初始化
	for i in xrange(lenA+1):
		dpMat[i][0] = i
	for j in xrange(lenB+1):
		dpMat[0][j] = j

	for i in xrange(1,lenA+1):

		for j in xrange(1,lenB+1):

			if strA[i-1] == strB[j-1]:
				f = 0
			else:
				f = 1
			dpMat[i][j] = min(dpMat[i-1][j]+1,dpMat[i][j-1]+1,dpMat[i-1][j-1]+f)
	print dpMat[i][j]
	return dpMat
			


if __name__ == '__main__':
	
	strA = 'wok'
	strB = 'wak'
	main(strA,strB)
	a = ['a','ab','zheng','',' ','b','kitten','']
	b = ['a','cd','dong','','a','ab','sitting']
	for strA,strB in zip(a,b):
		print strA,strB
		main(strA,strB)