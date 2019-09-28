#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:13:12 2019

this script aims to find FCIs for each mutant
@author: phantom
"""

import linecache


# =============================================================================
# 首先建立universe文件中测试用例的名字与fault-matrix文件中的名字的映射关系
# =============================================================================


# 存放映射关系的字典
universe_matrix_map = {}

constant_str = "unitest"
matrix_file_name = "fault-matrix"


def construct_map():
    #计数器
    counter = 0
    
    for line in open("fault-matrix"):
        line = line.strip().split(":")[0]
        if constant_str in line:
            counter += 1
            universe_matrix_map[line] = linecache.getline(
                    "universe", counter).strip()
        else:
            pass



# =============================================================================
# 识别FCI
# =============================================================================

# 构建7个列表存放揭示对应故障的FCIs
v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
v6 = []
v7 = []

def find_FCIs():
    counter = 0
    
    with open('fault-matrix', 'r') as file:
        for line in file:
            counter += 1
            line = line.strip().split(':')[0]
            if "unitest" in line:
                if "1" in linecache.getline(matrix_file_name, counter + 2).strip():
                    v1.append(line)
                if "1" in linecache.getline(matrix_file_name, counter + 4).strip():
                    v2.append(line)
                if "1" in linecache.getline(matrix_file_name, counter + 6).strip():
                    v3.append(line)
                if "1" in linecache.getline(matrix_file_name, counter + 8).strip():
                    v4.append(line)
                if "1" in linecache.getline(matrix_file_name, counter + 10).strip():
                    v5.append(line)
                if "1" in linecache.getline(matrix_file_name, counter + 12).strip():
                    v6.append(line)
                if "1" in linecache.getline(matrix_file_name, counter + 14).strip():
                    v7.append(line)
            else:
                pass
    file.close

                
# =============================================================================
# 获得FCIs
# =============================================================================

construct_map()
find_FCIs()

FCIs = {}

temp_v1 = []
temp_v2 = []
temp_v3 = []
temp_v4 = []
temp_v5 = []
temp_v6 = []
temp_v7 = []

for ele in v1:
    content = universe_matrix_map.get(ele)
    temp_v1.append(content)
    
for ele in v2:
    temp_v2.append(universe_matrix_map.get(ele))
    
for ele in v3:
    temp_v3.append(universe_matrix_map.get(ele))
for ele in v4:
    temp_v4.append(universe_matrix_map.get(ele))
for ele in v5:
    temp_v5.append(universe_matrix_map.get(ele))
for ele in v6:
    temp_v6.append(universe_matrix_map.get(ele))
for ele in v7:
    temp_v7.append(universe_matrix_map.get(ele))
    
f = open('FCIs', 'w+')

f.write("FCIs for v1: \n")
f.write("; ".join(temp_v1))

f.write("\n FCIs for v2: \n")
f.write("; ".join(ele for ele in temp_v2))

f.write("\n FCIs for v3: \n")
f.write("; ".join(ele for ele in temp_v3))

f.write("\n FCIs for v4: \n")
f.write("; ".join(ele for ele in temp_v4))

f.write("\n FCIs for v5: \n")
f.write("; ".join(ele for ele in temp_v5))

f.write("\n FCIs for v6: \n")
f.write("; ".join(ele for ele in temp_v6))

f.write("\n FCIs for v7: \n")
f.write("; ".join(ele for ele in temp_v7))

f.close()

print('OK')












            
            
    




