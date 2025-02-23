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

def rearrange_array(arr):
    if len(arr) < 2:
        # 如果数组长度小于 2，直接返回原数组，因为无法进行移动操作
        return arr
    # 提取数组的第一个元素
    first = arr[0]
    # 提取数组的最后一个元素
    last = arr[-1]
    # 提取除第一个和最后一个元素之外的中间部分元素
    middle = arr[1:-1]
    # 重新组合数组，第一个元素不变，最后一个元素放到第二个位置，中间元素依次后移
    new_arr = [first, last] + middle
    return new_arr

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

def Gm(path):
    testcasepath = os.path.join(path, 'testcase_our.txt')
    testcaseList = read_file_by_line_simple(testcasepath)
    testcaseSetPath = os.path.join(path, 'GmSet')
    if not os.path.exists(testcaseSetPath):
        os.makedirs(testcaseSetPath)
    for i in range(len(testcaseList)-1):
        print(testcaseList)
        testcaseList = rearrange_array(testcaseList)
        print(testcaseList)
        gmtestcasepath = os.path.join(testcaseSetPath, 'Gm'+str(i)+'.txt')
        write_string_to_file(gmtestcasepath, testcaseList)
        

path = '/data/muxy/reduceDataset/dataset'
for folder in os.listdir(path):
    Gm(os.path.join(path, folder))
    
