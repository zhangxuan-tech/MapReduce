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

import random

def random_swap_except_first(arr):
    if len(arr) <= 1:
        return [arr]
    first = arr[0]
    remaining = arr[1:]
    result = []
    for _ in range(len(arr) - 1):
        # 复制 remaining 列表，避免修改原始列表
        temp = remaining.copy()
        # 随机交换 temp 列表中的元素
        random.shuffle(temp)
        # 将第一个元素添加到交换后的列表开头
        new_arr = [first] + temp
        result.append(new_arr)
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

def RandomTest(path):
    testcasepath = os.path.join(path, 'testcase_our.txt')
    testcaseList = read_file_by_line_simple(testcasepath)
    testcaseSetPath = os.path.join(path, 'RandomSet')
    if not os.path.exists(testcaseSetPath):
        os.makedirs(testcaseSetPath)
    testcaseLists = random_swap_except_first(testcaseList)
    for i in range(len(testcaseLists)):
        randomtestcasepath = os.path.join(testcaseSetPath, 'Random'+str(i)+'.txt')
        write_string_to_file(randomtestcasepath, testcaseLists[i])
        
# RandomTest('/data/muxy/reduceDataset/dataset/r1')
path = '/data/muxy/reduceDataset/dataset'
for folder in os.listdir(path):
    print(folder)
    RandomTest(os.path.join(path, folder))

    
