#coding:utf-8
#将game4的4个元素的列表生成全部24种排列组合的games[列表]

import copy

def split_combination(game4):
    games = []
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
    return games


# 遍历第三个运算
def oper3(res, game, op3):
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
def oper2(res, game, op2, op3):
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
    res = oper3(res, game, op3)
    return res


# 遍历第一个运算
def oper1(res, game, op1, op2, op3):
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
    res = oper2(res, game, op2, op3)
    return res

#对games的全部运算组合，将符合结果=24的运算表达式存入answers[]返回
def comput24(games):
    ops = ['+', '-', '*', '/']
    answers = []
    for game in games:
        res = 0
        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    res = oper1(res, game, op1, op2, op3)
                    if res == 24:
                        answers.append(
                            '((({} {} {}) {} {}) {} {})'.format(game[0], op1, game[1], op2, game[2], op3, game[3]))
    return answers
