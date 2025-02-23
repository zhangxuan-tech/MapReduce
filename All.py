import os
def read_file_by_line_simple(file_path):
    fileList = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.rstrip('\n')
                linelist =line.split('#')
                fileList.append(linelist[:-1])
            return fileList
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

import itertools


def next_permutation(nums):
    # 从右向左找到第一个满足 nums[i] < nums[i + 1] 的位置 i
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        # 从右向左找到第一个满足 nums[j] > nums[i] 的位置 j
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        # 交换 nums[i] 和 nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    # 反转 nums[i + 1:]
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

def generate_permutations(nums):
    # 先对数组进行排序，确保从最小的排列开始
    nums.sort()
    original = nums[:]
    count = 0
    while True:
        yield nums[:]
        count += 1
        new_nums = next_permutation(nums)
        if count == 500:
            break
        if new_nums == original:
            break
        nums = new_nums

def permute_except_first(arr):
    if len(arr) <= 1:
        return [arr]
    first = arr[0]
    remaining = arr[1:]
    # 生成剩余元素的全排列


    # permutations = list(itertools.permutations(remaining))
    result = []
    counter = 0
    for perm in generate_permutations(remaining):
        # 将第一个元素添加到每个排列的开头
        new_perm = [first] + list(perm)
        result.append(new_perm)
        counter += 1
    return result

def write_string_to_file(file_path, arr):
    content = ''
    for ar in arr:
        for i in range(len(ar)):
            if i != len(ar) - 1:
                content += str(ar[i]) + '#'
            else:
                content += str(ar[i])+ '#' + '\n'


    try:
        # 使用 'w' 模式打开文件，该模式会覆盖文件原有内容
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"成功将内容写入文件：{file_path}")
    except Exception as e:
        print(f"写入文件时出错：{e}")

def All(path):
    testcasepath = os.path.join(path, 'testcase_our.txt')
    testcaseList = read_file_by_line_simple(testcasepath)
    testcaseSetPath = os.path.join(path, 'AllSet')
    if not os.path.exists(testcaseSetPath):
        os.makedirs(testcaseSetPath)
    
    testcaseLists = permute_except_first(testcaseList)
    for i in range(len(testcaseLists)):
        alltestcasepath = os.path.join(testcaseSetPath, 'All'+str(i)+'.txt')
        write_string_to_file(alltestcasepath, testcaseLists[i])
        
path = '/data/muxy/reduceDataset/dataset'
for folder in os.listdir(path):
    print(folder)
    All(os.path.join(path, folder))

    
