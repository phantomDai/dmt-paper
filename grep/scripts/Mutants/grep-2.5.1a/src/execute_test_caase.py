#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/14
# @Anthor   : phantomDai
"""
execute each test case
"""
import os

def execute_test_case():
    results = []
    with open('partition_scheme_testcases_1.2', 'r') as file:
        counter = 1
        for aline in file:
            aline = aline.strip()
            shell_command = r'./grep -E ' + "\"" + aline + "\" ./file.test > ./result/" + str(counter) + " 2>&1"
            shell_command_1 = r'./grep -E ' + "\"" + aline + "\" ./file.test"
            os.system(shell_command)
            counter += 1
    file.close()

all_results = []


def get_all_results():
    parent_path = os.path.join(os.getcwd(), 'result')
    for i in range(1, 101194):
        with open(os.path.join(parent_path, str(i)), 'r') as file:
            if file.readlines() not in all_results:
                all_results.append(file.readlines())
            else:
                pass
        file.close()


get_all_results()






