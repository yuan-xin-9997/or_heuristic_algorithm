# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: PSO_example.py
@time: 2021/5/13 9:24
@description:粒子群算法一个小的example，参考 https://mp.weixin.qq.com/s/aXzxXOBSqljpSjmJMqtU5g
"""
import random


class AlgorithmPSO:

    def __init__(self, n, c1, c2, v_max, w):
        self.particle_nums = n  # 种群规模（例子个数）
        self.x = []             # 粒子当前位置（函数中自变量x的值）
        self.y = [-9999, -9999]             # 粒子当前适应度（函数中因变量y的值）
        self.v = []             # 例子的方向和速度
        self.c1 = c1            # 学习因子c1
        self.c2 = c2            # 学习因子c2
        self.w = w              # 惯性因子
        self.p_best = [-9999, -9999]        # 表示粒子的历史最优位置
        self.g_best = -9999    # 所有粒子历史最优位置，（最大化问题对应）
        self.v_max = v_max        # 速度最大值

    def fitness_evaluation(self):
        """适应度评估函数"""
        for i in range(self.particle_nums):
            self.y[i] = -1 * self.x[i] * (self.x[i] - 2)

    def initial_function(self):
        """初始化函数"""
        # 初始化粒子（固定生成，假设只有两个粒子）
        self.x = [0.0, 2.0]
        self.v = [0.01, 0.02]
        # 评价每个粒子的适应度
        self.fitness_evaluation()
        # 初始化当前个体最优位置，并找到群体最优位置（更新pbest和gbest）
        for i in range(self.particle_nums):
            self.p_best[i] = self.y[i]  # 由于是初始化，粒子的初始适应度就是p_best
            if self.g_best < self.y[i]:
                self.g_best = self.y[i]
        # 输出算法迭代信息到控制台
        print("算法开始，初始最优解：%s" % self.g_best)
        print("")

    def get_max(self, a, b):
        """获取a和b中的最大值"""
        if a > b:
            return a
        else:
            return b

    def pso_main(self, max_iteration):
        """粒子群算法主函数"""
        for i in range(max_iteration):  # 迭代次数
            for j in range(self.particle_nums):     # 更新粒子速度和位置
                # 更新粒子速度
                self.v[j] = self.w * self.v[j] + self.c1 * random.random() * (self.p_best[j] - self.x[j]) + self.c2 * \
                            random.random() * (self.g_best - self.x[j])
                if self.v[j] > self.v_max:  # 控制速度不超过最大值
                    self.v[j] = self.v_max
                # 更新粒子位置
                self.x[j] += self.v[j]
                if self.x[j] > 2:   # 越界判断，只针对固定生成粒子的情况
                    self.x[j] = 2
                if self.x[j] < 0:
                    self.x[j] = 0
                # 将粒子位置和速度输出到控制台
                print("粒子n%s：位置x=%s 速度v=%s" % (j, self.x[j], self.v[j]))
            # 评价每个粒子的适应度
            self.fitness_evaluation()
            # 更新个体极值和群体极值（更新pbest和gbest）
            for j in range(self.particle_nums):
                self.p_best[j] = self.get_max(self.y[j], self.p_best[j])
                if self.g_best < self.y[j]:
                    self.g_best = self.y[j]
            # 输出算法迭代信息到控制台
            print("第%s次迭代，全局最优解%s" % (i+1, self.g_best))
            print("")


if __name__ == '__main__':
    print("a PSO example")
    pso = AlgorithmPSO(2, 2, 2, 0.1, 0.4)
    pso.initial_function()
    pso.pso_main(100)
