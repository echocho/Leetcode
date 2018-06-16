import copy
import numpy

import datetime

def unix_time_millis():
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (datetime.datetime.now() - epoch).total_seconds() * 1000.0

def findRelativeRanks(nums):
    """
    # saw online, a linear-time-growth algorithm
    sort = sorted(nums)[::-1]
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
    return map(dict(zip(sort, rank)).get, nums)
    """
    compare_lst = copy.deepcopy(nums)
    compare_lst.sort(reverse=True)
    for i in nums:
        compare_index = compare_lst.index(i)
        nums_index = nums.index(i)
        if compare_index > 2:
            nums[nums_index] = str(compare_index + 1)
        elif compare_index == 0:
            nums[nums_index] = 'Gold Medal'
        elif compare_index == 1:
            nums[nums_index] = 'Silver Medal'
        else:
            nums[nums_index] = 'Bronze Medal'
    return nums

# print(findRelativeRanks([57,36,97,4,17,98,2]))

def evaluate_function_time(func_name, func_args):
    t1 = unix_time_millis()
    func_name(func_args)
    t2 = unix_time_millis()
    return t2 - t1

def generate_random_array_by_size(n):
    return numpy.random.choice(n,n).tolist()

g_10000_size_array = generate_random_array_by_size(10000)
g_20000_size_array = generate_random_array_by_size(20000)
g_40000_size_array = generate_random_array_by_size(40000)
g_80000_size_array = generate_random_array_by_size(80000)
#
k1 = 5268.31616211
k2 = 18279.5979004
k3 = 77423.3532715
k4 = 350680.125
print(k1 - evaluate_function_time(findRelativeRanks, g_10000_size_array))
print(k2 - evaluate_function_time(findRelativeRanks, g_20000_size_array))
print(k3 - evaluate_function_time(findRelativeRanks, g_40000_size_array))
print(k4 - evaluate_function_time(findRelativeRanks, g_80000_size_array))



