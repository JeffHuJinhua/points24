#coding:utf-8
# 模拟一副牌的连续发牌，并且使用图形的牌代替1-10的数字
# 加入手机摄像头AI识别扑克牌功能，结合AR技术，移动版本会变得更加有趣

from __future__ import print_function
import random
import copy
from Tkinter import *
from PIL import Image, ImageTk
from comput24 import *


point = {'♠A': 1, '♠2': 2, '♠3': 3, '♠4': 4, '♠5': 5, '♠6': 6, '♠7': 7, '♠8': 8, '♠9': 9, '♠10': 10, '♠J': 10, '♠Q': 10, '♠K': 10,
        '♥A': 1, '♥2': 2, '♥3': 3, '♥4': 4, '♥5': 5, '♥6': 6, '♥7': 7, '♥8': 8, '♥9': 9, '♥10': 10, '♥J': 10, '♥Q': 10, '♥K': 10,
        '♣A': 1, '♣2': 2, '♣3': 3, '♣4': 4, '♣5': 5, '♣6': 6, '♣7': 7, '♣8': 8, '♣9': 9, '♣10': 10, '♣J': 10, '♣Q': 10, '♣K': 10,
        '♦A': 1, '♦2': 2, '♦3': 3, '♦4': 4, '♦5': 5, '♦6': 6, '♦7': 7, '♦8': 8, '♦9': 9, '♦10': 10, '♦J': 10, '♦Q': 10, '♦K': 10}
puke = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
        '♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
        '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
        '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K']
puke_img = []
for i in range(1, 53):
    puke_img.append(str(i)+'.jpg')
print(puke_img)
# for s in puke:
#    print(point[s])
# game.append(random.randint(1,10))
# game.append(random.randint(1,10))
# game.append(random.randint(1,10))
# game.append(random.randint(1,10))
games = []
# puke4 = puke[random.randint(0,13))]
puke_ind = [random.randint(0,51) for _ in range(4)]
print(puke_ind)
#puke4 = [puke[random.randint(0, 12)] for _ in range(4)]
puke4 = [puke[i] for i in puke_ind]
print(puke4)
puke_img4 = [puke_img[i] for i in puke_ind]
print(puke_img4)
game4 = [point[p] for p in puke4]
print(game4)
#puke_img4 =
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

root = Tk()
root.title('Points24/算24')
image_label = Label(root)

def bu1Button():
    #root = Tk()
    #print('bu1Button')
    #print(puke4[0] + '  ' + puke4[1] + '  ' + puke4[2] + '  ' + puke4[3])
    global puke4
    global puke_img4
    global game4
    #global image_label
    puke_ind = [random.randint(0, 51) for _ in range(4)]
    print(puke_ind)
    # puke4 = [puke[random.randint(0, 12)] for _ in range(4)]
    puke4 = [puke[i] for i in puke_ind]
    print(puke4)
    puke_img4 = [puke_img[i] for i in puke_ind]
    print(puke_img4)
    game4 = [point[p] for p in puke4]
    print(game4)
    #puke4 = [puke[random.randint(0, 12)] for _ in range(4)]
    #game4 = [point[p] for p in puke4]
    #print(puke4)
    #print(id(puke4))
    #print(game4)
    print(id(game4))
    print(image_label)

    text1.set(puke4[0] + '  ' + puke4[1] + '  ' + puke4[2] + '  ' + puke4[3])
    te1.delete(0.0, END)

    image_file4 = []
    for img in puke_img4:
        print(r'images/' + img)
        image_file4.append(Image.open(r'images/' + img))
    print(image_file4)
    target = Image.new('RGB', (420, 150))
    left = 0
    right = 105

    for image in image_file4:
        target.paste(image, (left, 0, right, 150))
        left += 105
        right += 105
    #target.show()
    im = ImageTk.PhotoImage(target)
    image_label.config(image=im)
    image_label.image = im
    #image_label.pack()
    #image_label.config(image=im1)

    #la2 = Label(root, text=comput24(games)).pack()
    #image_frame = Frame(root)
    #image_file = Image.open(r'images/1.jpg')
    #im = ImageTk.PhotoImage(image_file)
    #image_label = Label(image_frame, image=im).pack(side=LEFT, padx=5)
    #image_frame.pack()

def bu2Button():
    print('bu2Button')
    print(puke4)
    print(id(puke4))
    print(game4)
    print(id(game4))

    #te1 = Text(root)
    te1.delete(0.0, END)
    games = split_combination(game4)
    answers = comput24(games)
    if len(answers):
        te1.insert(END, 'There are {} answers/有{}个答案\n'.format(len(answers), len(answers)))
        for answer in answers:
            te1.insert(END, answer + '\n')
    else:
        te1.insert(END, 'There are no answers/没有答案\n')

 #   ans = 'There are {} answers/有{}个答案\n'.format(len(answers), len(answers))

#    for answer in answers:
#        ans += answer + '😎😅\n'
#        #te1.insert(END, answer + '\n')
#    print(ans)

#    te1.insert(END, ans)
    te1.pack()

games = split_combination(game4)
answers = comput24(games)

text1 = StringVar()
text1.set('等待发牌')
text2 = 'Waiting answers...'

bu1 = Button(root, text='发牌', command=bu1Button).pack()
la1 = Label(root, textvariable=text1).pack()
te1 = Text(root)
te1.insert(END, text2)
te1.pack()
bu2 = Button(root, text='答案', command=bu2Button).pack()
#la2 = Label(root, textvariable=text2).pack()

#la1 = Label(root, text=puke4[0]+'  '+puke4[1]+'  '+puke4[2]+'  '+puke4[3]).pack()

#image_file = Image.new()
image_file = Image.open(r'images/1.jpg')
image_file2 = Image.open(r'images/2.jpg')
im = ImageTk.PhotoImage(image_file)
im2 = ImageTk.PhotoImage(image_file2)
image_label = Label(root, image = im)
image_label.pack()
image_label.config(image=im2)

image_file4 = []
for img in puke_img4:
    print(r'images/' + img)
    image_file4.append(Image.open(r'images/' + img))
target = Image.new('RGB', (420, 150))
left = 0
right = 105
for image in image_file4:
    target.paste(image, (left, 0, right, 150))
    left += 105
    right += 105
im = ImageTk.PhotoImage(target)
image_label.config(image=im)

root.mainloop()

games = split_combination(game4)

'''
#将game4的4个元素的列表生成全部24种排列组合的games[列表]
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
'''

'''
#对games的全部运算组合，将符合结果=24的运算表达式存入answers[]返回
ops = ['+', '-', '*', '/']
#results = []
#results_count = 0
answers = []
for game in games:
    # results = []
    res = 0
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                # print(op1 + op2 + op3)
                res = oper1(res, game, op1, op2, op3)
                if res == 24:
                    answers.append(
                        '((({} {} {}) {} {}) {} {})'.format(game[0], op1, game[1], op2, game[2], op3, game[3]))
                    #results.append(res)
                    #results_count += 1
'''

answers = comput24(games)

#inp = raw_input('答案')
#print(inp)
#多余了^_^
# print(results)
# print(len(results))
#if len(results) == 0:
#    print('There are no answers/没有答案😅')
#else:
#    print('There are {} answers/有{}个答案😎'.format(len(results), len(results)))
if len(answers):
    print('There are {} answers/有{}个答案😎'.format(len(answers), len(answers)))
else:
    print('There are no answers/没有答案😅')

for answer in answers:
    print(answer)

