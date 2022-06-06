import pymssql
import random

def connect():
    conn = pymssql.connect(server='localhost', database='wd')
    return conn

class database(object):
    def __init__(self):
        pass

#登录相关功能
    @staticmethod
    def logincheck(username, password):

        sql = "SELECT * FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        flag = 0
        for row in rows:

            if username == row[1] and password == row[4]:
                flag = 1
                break

        return flag
        conn.close()

    @staticmethod
    def checkRole(username):
        sql = "SELECT userName,userRole,userId FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            if username == row[0]:
                flag = int(row[1])
                role =  row[2]
                break
        return flag,role
        conn.close()

#管理员相关功能
#用户管理

    @staticmethod
    def insertUserInfo(username, username_English, password, major, phone):

        length = str(int(random.randint(100,10000)))
        userRole='2'
        sql = "INSERT INTO [User] VALUES(%s, %s, %s, %s, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(length, username, username_English, userRole, password, phone, major))
        print('注册成功')
        conn.commit()
        conn.close()

    @staticmethod
    def inputitem():
        sql = "SELECT * FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print('用户ID,用户名,用户英文名，用户角色(0为超级管理员，1为老师，2为学生),密码,联系方式,专业')
        for i in rows:
            print(i)

        conn.close()

    @staticmethod
    def adduser(username, username_English, userRole, password, major, phone):

        length = str(int(random.randint(100,10000)))
        sql = "INSERT INTO [User] VALUES(%s, %s, %s, %s, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(length, username, username_English, userRole, password, phone, major))
        print('添加成功')
        conn.commit()
        conn.close()

    @staticmethod

    def upgradeuser(userId,username, username_English, userRole,password, phone, major):

        sql = "UPDATE [User] set userName=%s, userEnglishName=%s, userRole=%s,passWord=%s, telephoneNumber=%s, majorId=%s where userId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(username, username_English, userRole,password, phone, major,userId))
        print('更改成功')
        conn.commit()
        conn.close()

    @staticmethod
    def deleteuser(userId):

        sql = "DELETE from [User] where userId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(userId))
        print('删除成功')
        conn.commit()
        conn.close()


#题目管理


    @staticmethod
    def inputitemtitle():
        sql = "SELECT * FROM Title"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print('题目编号,题目内容, 题目类型, 专业号,知识点, 答案,详细答案,分值,难度系数,图像,A选项,B选项,C选项,D选项,E选项,F选项')
        for i in rows:
            print(i)
        conn.close()

    @staticmethod
    def addtitle(titleId,titleContent, titleType, majorId,knowledgeId, answer, answerDetails,points,difficultyLevel,selectFlagA,selectFlagB,selectFlagC,selectFlagD,selectFlagE,selectFlagF):

        length = str(int(random.randint(100,10000)))
        sql = "INSERT INTO Title(titleId,titleContent, titleType, majorId,knowledgeId, answer, answerDetails,points,difficultyLevel,selectFlagA,selectFlagB,selectFlagC,selectFlagD,selectFlagE,selectFlagF) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(titleId,titleContent, titleType, majorId,knowledgeId, answer, answerDetails,points,difficultyLevel,selectFlagA,selectFlagB,selectFlagC,selectFlagD,selectFlagE,selectFlagF))
        print('添加成功')
        conn.commit()
        conn.close()
        return length

    @staticmethod

    def upgradetitle(titleId,titleContent, titleType, majorId,knowledgeId, answer, answerDetails,points,difficultyLevel,selectFlagA,selectFlagB,selectFlagC,selectFlagD,selectFlagE,selectFlagF):#title更新

        sql = "UPDATE Title set titleContent=%s, titleType=%s, majorId=%s,knowledgeId=%s, answer=%s, answerDetails=%s, points=%s, difficultyLevel=%s, selectFlagA=%s, selectFlagB=%s, selectFlagC=%s, selectFlagD=%s, selectFlagE=%s, selectFlagF=%s where titleId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(titleContent, titleType, majorId,knowledgeId, answer, answerDetails,points,difficultyLevel,selectFlagA,selectFlagB,selectFlagC,selectFlagD,selectFlagE,selectFlagF,titleId))
        print('更改成功')
        conn.commit()
        conn.close()

    @staticmethod
    def deletetitle(titleId):

        sql = "DELETE from Title where titleId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(titleId))
        print('删除成功')
        conn.commit()
        conn.close()


#作答记录管理
    @staticmethod
    def inputitemanswer():
        sql = "SELECT * FROM Answer"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print('测试ID,用户ID, 卷子ID, 分数,答案1,答案2,答案3,答案4,答案5,答案6,答案7,答案8,答案9,答案10')
        for i in rows:
            print(i)
        conn.close()

    @staticmethod
    def addanswer(testId,userId, paperId, score,result1, result2, result3,result4,result5,result6,result7,result8,result9,result10):

        length = str(int(random.randint(100,10000)))
        sql = "INSERT INTO Answer(testId,userId, paperId, score,result1, result2, result3,result4,result5,result6,result7,result8,result9,result10) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(testId,userId, paperId, score,result1, result2, result3,result4,result5,result6,result7,result8,result9,result10))
        print('添加成功')
        conn.commit()
        conn.close()
        return length

    @staticmethod

    def upgradeanswer(testId,userId, paperId, score,result1, result2, result3,result4,result5,result6,result7,result8,result9,result10):#title更新

        sql = "UPDATE Answer set userId=%s,paperId=%s, score=%s,result1=%s, result2=%s, result3=%s, result4=%s, result5=%s, result6=%s, result7=%s, result8=%s, result9=%s, result10=%s where testId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(userId,paperId, score,result1, result2, result3,result4,result5,result6,result7,result8,result9,result10,testId))
        print('更改成功')
        conn.commit()
        conn.close()

    @staticmethod
    def deleteanswer(testId):

        sql = "DELETE from Answer where testId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(testId))
        print('删除成功')
        conn.commit()
        conn.close()

#教师的一部分功能是管理员的一部分功能

#学生功能

    @staticmethod
    def Answercheck(majorId):
        sql = "SELECT titleId,titleContent FROM Title where majorId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(majorId))
        rows1 = cur.fetchall()
        print('题号：,题目')
        for i in rows1:
            print(i)
        conn.close()

    @staticmethod
    def upanswer(selectFlagF,titleId):
        sql = "UPDATE Title set selectFlagF=%s where titleId=%s"

        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(selectFlagF,titleId))
        print('答题完毕')

        conn.close()

    def Answersee(majorId):
        sql = "SELECT titleId,answerDetails FROM Title where majorId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(majorId))
        rows = cur.fetchall()
        print('题目，解析')
        for i in rows:
            print(i)
        conn.close()

