"""
Given an array of integers nums and an integer target, 
return indices of two numbers such that they add up to target.

"""



class two_sum():
    def sum_two(self,num,target):
        for i in range(len(num)):
            for j in range(i +1, len(num)):
                if num[i] + num[j] == target:
                    return [i,j]
        return []
