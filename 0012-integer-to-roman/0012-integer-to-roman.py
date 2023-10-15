class Solution:
    def intToRoman(self, num: int) -> str:

        def get_rules(order, n: int):

            n = int(n)

            tab_1 = ['I', 'V', 'X']
            tab_10 = ['X', 'L', 'C']
            tab_100 = ['C', 'D', 'M']

            if order == 1:
                a = tab_1
            elif order == 2:
                a = tab_10
            elif order == 3:
                a = tab_100
            else:
                return n * 'M'

            rules = {0:'', 1:a[0]*1, 2:a[0]*2, 3:a[0]*3, 4:a[0]+a[1], 5:a[1], 6:a[1] + a[0]*1, 7:a[1] + a[0]*2, 8:a[1] + a[0]*3, 9:a[0]+a[2]}
                
            return rules[n]
        
        answer = ''
        order = len(str(num))
        current_order = order

        while current_order > 0:
            answer += get_rules(current_order, str(num)[order-current_order])
            current_order -= 1

        return answer