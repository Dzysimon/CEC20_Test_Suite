# CEC20 Test Function Suite for Single Objective Bound Constrained Numerical Optimization(Python Version)

## User Instructions
1. The DLL file is generated from the cpp file.
2. How to use this tool is shown in example.py.
3. REMEMBER to copy input_data/, cec20_test_func.dll and CEC20_Test_Suite.py together to your new python working directory.

## Requirements
1. python >= 3.7.0
2. numpy >= 1.18.0
3. Windows 10

## Parameters

void cec20_test_func(double *x, double *f, int nx, int mx,int func_num0)

1. double *x: 输入数组 Input array.
2. double *f: 计算结果 Result of test function.
3. int nx: 单个数组的维度 Dimension of single array.
4. int mx: 输入数组的个数 Number of input arrays.
5. int func_num0: 函数索引值（1~10）The index of ten cec20 test functions, from 1 to 10.

## Usage


```shell
python example.py
```



