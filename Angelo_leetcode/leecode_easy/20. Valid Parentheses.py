# class Solution:
#     def isValid(self, s: str) -> bool:

input_ = "()"
pairs = {")": "(", "]": "[", "}": "{"}  
null_list = []


class Solution:
    def is_valid(self, s:str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"} 

        for i in input_:
            if i in pairs.values:
                stack.append(i)
            return False        
            
            
    