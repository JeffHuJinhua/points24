#coding:utf-8
# 模拟一副牌的连续发牌，并且使用图形的牌代替1-10的数字
# 加入手机摄像头AI识别扑克牌功能，结合AR技术，移动版本会变得更加有趣

from __future__ import print_function
import random
import copy

# 遍历第三个运算
def oper3(res, op3):
    # print(op3)
    if op3 == '+':
        res = res + game[3]
    if op3 == '-':
        res = res - game[3]
    if op3 == '*':
        res = res * game[3]
    if op3 == '/':
        if (res % game[3]) != 0:
            return -100
        res = res / game[3]
    return res


# 遍历第二个运算
def oper2(res, op2):
    if op2 == '+':
        res = res + game[2]
    if op2 == '-':
        res = res - game[2]
    if op2 == '*':
        res = res * game[2]
    if op2 == '/':
        if res % game[2] != 0:
            return -100
        res = res / game[2]
    res = oper3(res, op3)
    return res


# 遍历第一个运算
def oper1(res, op1):
    if op1 == '+':
        res = game[0] + game[1]
    if op1 == '-':
        res = game[0] - game[1]
    if op1 == '*':
        res = game[0] * game[1]
    if op1 == '/':
        if game[0] % game[1] != 0:
            return -100
        res = game[0] / game[1]
    res = oper2(res, op2)
    return res


point = {'♥A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '♠J': 10, '♦Q': 10, '♣K': 10}
puke = ['♥A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '♠J', '♦Q', '♣K']
# for s in puke:
#    print(point[s])
# game.append(random.randint(1,10))
# game.append(random.randint(1,10))
# game.append(random.randint(1,10))
# game.append(random.randint(1,10))
games = []
# puke4 = puke[random.randint(0,13))]
puke4 = [puke[random.randint(0, 12)] for _ in range(4)]
game4 = [point[p] for p in puke4]
# game4 = []
# for i in puke4:
# print(point[i])
# game4.append(point[i])
print('发牌：[', end='')
for i in range(4):
    print('{}'.format(puke4[i]), end='')
    if i < 3:
        print(',', end='')
print(']')
#print('发牌：' + str(puke4))
print('牌点：' + str(game4))
for a in game4:
    # game.append(a)
    # 不适合出现重复牌的情况
    # for b in [x for x in game4 if x != a]:
    # 生成抽取牌的排列
    game3 = copy.deepcopy(game4)
    game3.remove(a)
    for b in game3:
        game2 = copy.deepcopy(game3)
        game2.remove(b)
        # game.append(b)
        # for c in [x for x in game4 if x != a and x != b]:
        for c in game2:
            game1 = copy.deepcopy(game2)
            game1.remove(c)
            # game.append(c)
            # for d in [x for x in game4 if x != a and x != b and x != c]:
            for d in game1:
                games.append([a, b, c, d])
# print(games)
# print(len(games))

ops = ['+', '-', '*', '/']
results = []
answers = []
for game in games:
    # results = []
    res = 0
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                # print(op1 + op2 + op3)
                res = oper1(res, op1)
                if res == 24:
                    answers.append(
                        '((({} {} {}) {} {}) {} {})'.format(game[0], op1, game[1], op2, game[2], op3, game[3]))
                    results.append(res)

inp = raw_input('答案')
print(inp)
# print(results)
# print(len(results))
if len(results) == 0:
    print('There are no answers/没有答案😅')
else:
    print('There are {} answers/有{}个答案😎'.format(len(results), len(results)))

for answer in answers:
    print(answer)

