# -*- coding:utf-8 -*-
import re
def getstr():
	fr=open("test.txt","r")
	fr.close
	strlist=[]
	for a in fr.readlines():
		a=a.replace('\n','')
		a=a.replace('\t',' ')
		strlist.append(a)
#	print(strlist)
	return strlist


if __name__ == '__main__':
	strlist=getstr()
	fr=open("product.txt")
	namelist=[]
	result=[]
	dellist=[]
	a=0
	start=0
	for product in fr.readlines():
		namelist.append(product[:-1])
#	從將整個產品名稱加入改成將產品名稱分隔開來後再以LIST的形式加入整個list裡
#	又或者先將每個產品的單詞分開來後 統一加入list裡 然後先一個個找 有的並且在前後沒有東西的情況下就加入list裡
#		全部找完之後再回來看有沒有，這樣子就可以處理關於詞分開的問題
#	那麼 關於詞中間被特殊符號插入的問題
#	for product in fr.readlines():
#		namelist.append(product[:-1].split()
		
	for product in namelist:
		"""
		
		
		split=product.split()
		index=0
		if string.find(split[0])>-1:
			for index in range(1,len(split)):
			tag=tag[1]
			tag=tag.lower()
			for string in strlist:
				string=string.lower()
				if string.find(tag)>-1:
					if index==0:
						start=string.find(tag)
						tag=tag[index]
					elif tag==product[len(product)-1]:
						result.append([])
						result[a].append(product)
						result[a].append(start)
						result[a].append(len(tag)+string.find(tag))
						a+=1
						print(result,product)
					else
						tag+=1
				else:
					index=0
"""
		
		product=product.lower()
		for string in strlist:
			#由於大家有很多product 的名字共用一塊部分，所以我想在find的時候，如果將起始跟結束記錄下來，再將有被其他列入包圍的給去除掉
			#我現在想把產品名稱用空白分開來，然後一個一個找，那如果一個一個找，關於演算法要怎麼寫
			
			'''
			現在能處理的部分，只有直接找，然後能避免產品使用重複的區塊
			現在遇到沒辦法處理的部分，有產品名字分隔開來表示，產品中間夾雜著特殊符號
			'''
			
			
			string=string.lower()
			if string.find(product)>-1:
				print(product+"\t"+str(string.find(product)))
				result.append([])
				result[a].append(product)
				result[a].append(string.find(product))
				result[a].append(len(product)+string.find(product))
				a+=1
				

#	print(result)
	for i in result:
		for j in result:
			if(i != j):
				print(i[1],i[2],j[1],j[2])
				if((j[1]>=i[1]) and (j[2]<=i[2])):
					print(j)
					result.remove(j)
				print(result)
	
	if(len(dellist)>0):
		for i in range(0,len(dellist)):
			result.remove(dellist[i])
			
	fr.close()
