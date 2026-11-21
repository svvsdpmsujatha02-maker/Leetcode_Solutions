class Solution:
    def numberOfSteps(self, num: int) -> int:
        number_of_steps = 0 
        while num != 0 :
            if num % 2 == 0 :
                num /= 2
                number_of_steps += 1
            else :
                num -= 1
                number_of_steps += 1
        return number_of_steps
        