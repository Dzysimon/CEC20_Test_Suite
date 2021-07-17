#!/bin/python
#  _*_encoding = utf-8_*_
#  CEC20 Test Function Suite for Single Objective Bound Constrained Numerical Optimization 
#  Z.Duan, Beihang University, Beijing.
#  E-mail: duanzhiyu@buaa.edu.cn
#  2021.07.17


import ctypes
import numpy as np

class CEC20_Test_Suite:

    def __init__(self, func_num):
        """
        Load the cpp dynamic library, and set parameters for python interface.
        :param func_num: index of the chosen test function, from 1 to 10.
        """
        dll = ctypes.WinDLL("./cec20_test_func.dll")
        self.func_num = func_num
        self.cec_func = dll.cec20_test_func
        self.cec_func.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"), np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"), ctypes.c_int, ctypes.c_int, ctypes.c_int]

    def func(self, x: np.array):
        """
        Test function.
        :param x: np.array([[], [], ..., []], dtype=np.float64) Input matrix.
        """
        m = len(x)
        dim = len(x[0])
        r = np.array([0.0] * m, dtype=np.float64)
        x = x.ravel()
        self.cec_func(x, r, dim, m, self.func_num)
        return r

