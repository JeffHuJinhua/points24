#coding:utf-8
# 模拟一副牌的连续发牌，并且使用图形的牌代替1-10的数字
# 加入手机摄像头AI识别扑克牌功能，结合AR技术，移动版本会变得更加有趣

import random
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

games = []
puke4 = []
puke_img4 = []
game4 = []

root = Tk()
root.title('算24/Points24（©H20180529）')
image_label = Label(root)

def bu1Button():
    global puke4
    global puke_img4
    global game4

    puke_ind = [random.randint(0, 51) for _ in range(4)]
    puke4 = [puke[i] for i in puke_ind]
    puke_img4 = [puke_img[i] for i in puke_ind]
    game4 = [point[p] for p in puke4]

    text1.set(puke4[0] + '  ' + puke4[1] + '  ' + puke4[2] + '  ' + puke4[3])
    te1.delete(0.0, END)

    image_file4 = []
    for img in puke_img4:
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
    image_label.image = im

def bu2Button():
    te1.delete(0.0, END)
    games = split_combination(game4)
    answers = comput24(games)
    if len(answers):
        te1.insert(END, 'There are {} answers/有{}个答案\n'.format(len(answers), len(answers)))
        for answer in answers:
            te1.insert(END, answer + '\n')
    else:
        te1.insert(END, 'There are no answers/没有答案\n')

    te1.pack()

games = split_combination(game4)
answers = comput24(games)

text1 = StringVar()
text1.set('等待发牌/Waiting for deal...')
text2 = '等待答案/Waiting for answers...'

bu1 = Button(root, text='发牌/Deal', command=bu1Button).pack()
la1 = Label(root, textvariable=text1).pack()
te1 = Text(root)
te1.insert(END, text2)
te1.pack()
bu2 = Button(root, text='答案/Answers', command=bu2Button).pack()

image_file4 = []
image_file4.append(Image.open(r'images/54.jpg'))
image_file4.append(Image.open(r'images/54.jpg'))
image_file4.append(Image.open(r'images/53.jpg'))
image_file4.append(Image.open(r'images/53.jpg'))
target = Image.new('RGB', (420, 150))
left = 0
right = 105
for image in image_file4:
    target.paste(image, (left, 0, right, 150))
    left += 105
    right += 105
im = ImageTk.PhotoImage(target)
image_label.config(image=im)
image_label.pack()

root.mainloop()

games = split_combination(game4)
answers = comput24(games)
