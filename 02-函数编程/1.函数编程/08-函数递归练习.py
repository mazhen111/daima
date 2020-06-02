#递归二分查找
a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107]
def  binary_search(start,end,n,d_list):
	"""
	递归二分查找
	:param start: 
	:param end: 
	:param n: 
	:param list: 
	:return: 
	"""
	if start < end :
		mid = (start + end) //  2
		#print ("mid",mid)
		if d_list[mid] >  n :
			print ("go left",start,mid,end,"--",d_list[start],d_list[mid],d_list[end -1])
			binary_search(start,mid,n,d_list)
		elif d_list[mid] <  n :
			print ("2",d_list[mid])
			print("go left", start, mid, end, "--", d_list[start], d_list[mid], d_list[end -1])
			binary_search(mid+1,end,n,d_list)
		else:
			print ("找到了",d_list[mid])


	else:
		print ("cannot find %s in this data list" % n)

binary_search(0, len(a), 11, a)
