#!/usr/bin/env python3
import unittest

def multiple_Of_Three(num):
	if num%3==0:
		return "Devhaus "
	else:
		return ""
def multiple_Of_Five(num):
	if num%5==0:
		return "Learning "
	else:
		return ""
def multiple_Of_Seven(num):
	if num%7==0:
		return "Model"
	else:
		return ""
def Devhaus():
	result=[]
	for i in range(1,106):
		p=multiple_Of_Three(i)+multiple_Of_Five(i)+multiple_Of_Seven(i)
		if p!="" and p!="Learning Model":
			print(p)
			result.append(p)
		else:
			print(i)
			result.append(i)
	return result
			
arr=Devhaus()

#test cases
class Testcase(unittest.TestCase):
	def test01(self):
		self.assertEqual(arr[0], 1)
	def test02(self):
		self.assertEqual(arr[1], 2)
	def test03(self):
		self.assertEqual(arr[102], 103)
	def test04(self):
		self.assertEqual(arr[103], 104)
	def test05(self):
		self.assertEqual(arr[104], "Devhaus Learning Model")
		
if __name__ == '__main__':
	unittest.main()
		
		