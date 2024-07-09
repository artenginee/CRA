class OddEven:
    def get_result(self, nums):
        result = []
        for data in nums:
            even_cnt = 0
            odd_cnt = 0
            if data % 2 == 0:
                even_cnt += 1


        for data in nums:
            if data % 2 == 0:
                result.append('O')
            else:
                result.append('X')
        return result