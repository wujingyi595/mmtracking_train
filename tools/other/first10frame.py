# 打开文件
with open('/home/wjy/wujingyi/Dataset/MDMTchallenge/train/23-2/gt/gt.txt', 'r') as file:
    lines = file.readlines()

# 创建一个新的列表来存储符合条件的行
filtered_lines = []

# 遍历每一行
for line in lines:
    # 将每一行的内容分割成一个列表
    parts = line.split(',')
    # 获取该行的第一个数字，并将其转换为整数
    first_number = int(parts[0])
    # 如果第一个数字在1到10之间，则将该行添加到新的列表中
    if 1 <= first_number <= 10:
        filtered_lines.append(line)

# 将符合条件的行写入新文件中
with open('/home/wjy/wujingyi/Dataset/MDMTchallenge/train/23-2/gt/gt.txt', 'w') as file:
    file.writelines(filtered_lines)

print("筛选完成！")
