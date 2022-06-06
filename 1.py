from sql import database

print('方式二-数据库大作业-吴旦:')

while True:
    print('''


--------------------------------
       1 注册用户（默认为学生）  |
       2 登录系统               |
       3 退出系统               |
--------------------------------

''')
    a=int(input())
    if a==1:
        print("输入："'用户名', '英文名', '密码', '专业', '电话')
        a1=str(input())
        a2=str(input())
        a3=str(input())
        a4=str(input())
        a5=str(input())
        database.insertUserInfo(a1,a2,a3,a4,a5)
    elif a==2:
        print('账号：')
        b=str(input())
        print('密码:')
        b1=str(input())
        if (database.logincheck(b,b1)):
            umod,uid=database.checkRole(b)
            if umod==0:
                print('\n您是：管理员')
                while True:
                    print('''
              -----管理员界面:---
                1、账户管理
                2、题目管理       
                3、作答记录管理  
                4、退出登录      
                ''')

                    c = int(input())
                    if c==1:
                        while True:
                            print(''''
                         ---账户管理----
                           1、添加账户
                           2、删除账户
                           3、修改账户
                           4、查看所有账户
                           5、返回上一级
                        ''')
                            d = int(input())
                            if d==1:
                                print("输入："'用户名', '英文名', '用户类型', '密码（不超过六位）', '专业', '电话')
                                i1 = str(input())
                                i2 = str(input())
                                i3 = str(input())
                                i4 = str(input())
                                i5 = str(input())
                                i6 = str(input())
                                database.adduser(i1, i2, i3, i4, i5,i6)
                            elif d==2:
                                print('请输入要删除的用户的ID号')
                                j=int(input())
                                database.deleteuser(j)
                            elif d==3:
                                print("输入："'用户ID号','更改后用户名', '更改后英文名', '用户类型','密码（不超过六位）', '电话','专业')
                                k1 = str(input())
                                k2 = str(input())
                                k3 = str(input())
                                k4 = str(input())
                                k5 = str(input())
                                k6 = str(input())
                                k7 = str(input())
                                database.upgradeuser(k1,k2,k3,k4,k5,k6,k7)
                            elif d==4:
                                database.inputitem()
                            elif d==5:
                                break
                    elif c==2:
                        while True:
                            print('''
                               -----题目管理------
                                 1、添加题目
                                 2、删除题目
                                 3、修改题目
                                 4、查看所有题目
                                 5、返回上一级
                                         ''')
                            e = int(input())
                            if e==1:
                                print("请输入：题目编号,题目内容, 题目类型, 专业号,知识点, 答案,详细答案,分值,难度系数,A选项,B选项,C选项,D选项,E选项,F选项")
                                m1 = str(input())
                                m2 = str(input())
                                m3 = str(input())
                                m4 = str(input())
                                m5 = str(input())
                                m6 = str(input())
                                m7 = str(input())
                                m8 = str(input())
                                m9 = str(input())
                                m10 = str(input())
                                m11 = str(input())
                                m12 = str(input())
                                m13 = str(input())
                                m14 = str(input())
                                m15 = str(input())

                                database.addtitle(m1,m2,m3,m4,m5 ,m6 ,m7 ,m8 ,m9 ,m10 ,m11 ,m12 ,m13 ,m14 ,m15 )
                            elif e==2:
                                print('请输入要删除的题目的ID号')
                                l = int(input())
                                database.deletetitle(l)
                            elif e==3:
                                print("请输入：题目编号,题目内容, 题目类型, 专业号,知识点, 答案,详细答案,分值,难度系数,A选项,B选项,C选项,D选项,E选项,F选项")
                                m1 = str(input())
                                m2 = str(input())
                                m3 = str(input())
                                m4 = str(input())
                                m5 = str(input())
                                m6 = str(input())
                                m7 = str(input())
                                m8 = str(input())
                                m9 = str(input())
                                m10 = str(input())
                                m11 = str(input())
                                m12 = str(input())
                                m13 = str(input())
                                m14 = str(input())
                                m15 = str(input())

                                database.upgradetitle(m1,m2,m3, m4,m5 ,m6 ,m7 ,m8 ,m9 ,m10 ,m11 ,m12 ,m13 ,m14 ,m15 )
                            elif e==4:
                                database.inputitemtitle()
                            elif e == 5:
                                break
                    elif c==3:
                        while True:
                            print('''
                         ------作答记录管理----
                           1 添加作答记录
                           2 删除作答记录
                           3 修改作答记录
                           4 查看所有作答记录
                           5 返回上一级
                        ''')
                            f = int(input())
                            if f==1:
                                print("请输入测试ID,用户ID, 卷子ID, 分数,答案1,答案2,答案3,答案4,答案5,答案6,答案7,答案8,答案9,答案10")
                                q1 = str(input())
                                q2 = str(input())
                                q3 = str(input())
                                q4 = str(input())
                                q5 = str(input())
                                q6 = str(input())
                                q7 = str(input())
                                q8 = str(input())
                                q9 = str(input())
                                q10 = str(input())
                                q11 = str(input())
                                q12 = str(input())
                                q13 = str(input())
                                q14 = str(input())
                                database.addanswer(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14)
                            elif f==2:
                                print("请输入删除的测试号")
                                r = str(input())
                                database.deleteanswer(r)
                            elif f==3:
                                print("请输入测试ID,用户ID, 卷子ID(只有1), 分数,答案1,答案2,答案3,答案4,答案5,答案6,答案7,答案8,答案9,答案10")
                                q1 = str(input())
                                q2 = str(input())
                                q3 = str(input())
                                q4 = str(input())
                                q5 = str(input())
                                q6 = str(input())
                                q7 = str(input())
                                q8 = str(input())
                                q9 = str(input())
                                q10 = str(input())
                                q11 = str(input())
                                q12 = str(input())
                                q13 = str(input())
                                q14 = str(input())
                                database.upgradeanswer(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14)
                            elif f==4:
                                database.inputitemanswer()
                            elif f == 5:
                                break
                    elif c==4:
                        break
            elif umod==1:
                print('您是：教师')
                while True:
                    print('''
                                -----教师界面:----
                                    1、录入题目
                                    2、退出登录
                                    ''')
                    a=int(input())
                    if a==1:
                        
                        print('''
                           -----教室界面------
                             1、添加题目
                             2、删除题目
                             3、修改题目
                             4、查看所有题目
                             5、返回上一级
                                     ''')
                        e = int(input())
                        if e==1:
                            print("请输入：题目编号,题目内容, 题目类型, 专业号,知识点, 答案,详细答案,分值,难度系数,A选项,B选项,C选项,D选项,E选项,F选项")
                            m1 = str(input())
                            m2 = str(input())
                            m3 = str(input())
                            m4 = str(input())
                            m5 = str(input())
                            m6 = str(input())
                            m7 = str(input())
                            m8 = str(input())
                            m9 = str(input())
                            m10 = str(input())
                            m11 = str(input())
                            m12 = str(input())
                            m13 = str(input())
                            m14 = str(input())
                            m15 = str(input())

                            database.addtitle(m1,m2,m3,m4,m5 ,m6 ,m7 ,m8 ,m9 ,m10 ,m11 ,m12 ,m13 ,m14 ,m15 )
                        elif e==2:
                            print('请输入要删除的题目的ID号')
                            l = int(input())
                            database.deletetitle(l)
                        elif e==3:
                            print("请输入：题目编号,题目内容, 题目类型, 专业号,知识点, 答案,详细答案,分值,难度系数,A选项,B选项,C选项,D选项,E选项,F选项")
                            m1 = str(input())
                            m2 = str(input())
                            m3 = str(input())
                            m4 = str(input())
                            m5 = str(input())
                            m6 = str(input())
                            m7 = str(input())
                            m8 = str(input())
                            m9 = str(input())
                            m10 = str(input())
                            m11 = str(input())
                            m12 = str(input())
                            m13 = str(input())
                            m14 = str(input())
                            m15 = str(input())

                            database.upgradetitle(m1,m2,m3, m4,m5 ,m6 ,m7 ,m8 ,m9 ,m10 ,m11 ,m12 ,m13 ,m14 ,m15 )
                        elif e==4:
                            database.inputitemtitle()
                        elif e == 5:
                            break
                    elif a==2:
                        break
            elif umod==2:
                print('您是：学生')
                while True:
                    print('''
            -----------学生界面:------------
                1、选择专业并进行答题 
                2、查看答案
                3、退出登录
                ''')
                    h = int(input())
                    if h==1:
                        print("输入专业号")
                        o1 = str(input())
                        database.Answercheck(o1)
                        print("开始作答")
                        print("请输入：题号,作答结果(0-9数字)")
                        p1 = str(input())
                        p2 = str(input())
                        database.upanswer(p2,p1)
                    elif h==2:
                        print("请输入你的专业号,查看题目解析")
                        sd=str(input())
                        database.Answersee(sd)
                    elif h==3:
                        break
        else:
            print('没有此用户或者密码错误')
    elif a==3:
        break


