# -*- coding: utf-8 -*-
import random,sys
def gen_ans():
    ans = []
    while len(ans) != 4:
        n = random.randrange(0, 10)
        if not n in ans:
            ans.append(n)
    print(ans)
    return ans
def check_input(user_input):
    try: int(user_input)
    except: return False
    for x in user_input:
        if user_input.count(x)>1:
            return False
    if len(user_input) != 4: return False
    else: return True
def check_answer(ans, nums):
    a, b = 0, 0
    for n in nums:
        if n in ans:
            if nums.index(n) == ans.index(n):
                a += 1
            else:
                b += 1
    return a, b
def game1(answer,user_input):
    if check_input(user_input):
        num = []
        for x in user_input:
            num.append(int(x))
        a, b = check_answer(answer, num)
        if a == 4:
            return "4A0B,Good job"
        else:
            return "%dA%dB,Keep trying!" % (a, b)
    else:
        return "You need to guess 4 numbers between 0 ~ 9.\nFor example: ! 1234\nPlease try again."
def ooxx(bool):
    if bool == True:
        return "⭕"
    elif bool == False:
        return "❌"
    elif bool == None:
        return "☐"
def board():
    board = {'1':None,'2':None,'3':None,'4':None,'5':None,'6':None,'7':None,'8':None,'9':None}
    return board
def check_ans(board):
    for x in board:
        if board[x] == None:
            break
    else:
        return 'no one win'
    if board['1'] == board['2'] == board['3'] !=None or board['4'] == board['5'] == board['6'] !=None or board['7'] == board['8'] == board['9'] !=None or board['1'] == board['4'] == board['7'] !=None or board['2'] == board['5'] == board['8'] !=None or board['3'] == board['6'] == board['9'] !=None or board['1'] == board['5'] == board['9'] !=None or board['3'] == board['5'] == board['7'] !=None:
        return 'win'
    else:
        return False
def print_board(board):
    return ooxx(board['1'])+ooxx(board['2'])+ooxx(board['3'])+"\n"+ooxx(board['4'])+ooxx(board['5'])+ooxx(board['6'])+"\n"+ooxx(board['7'])+ooxx(board['8'])+ooxx(board['9'])
def input_ans(board,num,bool):
    try:
        k = int(num)
        if k <=9 and k>=1 and board[str(k)] == None:
            board[str(k)] = bool
            return board
        else:
            return "not in range"
    except:
        return "not a num"