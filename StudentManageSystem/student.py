import os
class Student:
    def __init__(self,no,name,chinese,math,english):
        self.no = no
        self.name = name
        self.chinese = int(chinese)
        self.math = int(math)
        self.english = int(english)

class StudentList:
    def __init__(self):
        self.stulist = []

    def show(self):
        #显示学生信息
        print('{:8}\t{:8}\t{:8}\t{:8}\t{:8}'
              .format('学号','姓名','语文','数学','英语'))
        for stu in self.stulist:            
            print('{:8}\t{:8}\t{:<8}\t{:<8}\t{:<8}'
              .format(stu.no,stu.name,stu.chinese,stu.math,stu.english))
            
    def __enterScore(self,message):
        #成绩输入
        while True:
            try:
                score = input(message)
                if 0 <= int(score) <= 100:
                    break
                else:
                    print("输入错误，成绩应在0到100之间")
            except:
                print("输入错误，成绩应在0到100之间")
        return score  

    def __exists(self,no):
        #判断学号是否存在
        for stu in self.stulist:
            if stu.no == no:
                return True
        else:
            return False
        
    def insert(self):
        #添加学生信息
        while True:
            no = input('学号:')
            if self.__exists(no):
                print('该学号已存在')
            else:
                name = input('姓名:')
                chinese = self.__enterScore('语文成绩:')
                math = self.__enterScore('数学成绩:')
                english = self.__enterScore('英语成绩:')
                stu = Student(no,name,chinese,math,english)
                self.stulist.append(stu)
            choice = input('继续添加(y/n)?').lower()
            if choice == 'n':
                break

    def find(self):
        #查询学生信息
        while True:
            no = input('请输入要查询的学生学号:')                
            for stu in self.stulist[::]:
                if stu.no == no:
                    print('查询成功')
                    print('{:8}\t{:8}\t{:8}\t{:8}\t{:8}'
                        .format('学号','姓名','语文','数学','英语'))
                    print('{:8}\t{:8}\t{:<8}\t{:<8}\t{:<8}'
                        .format(stu.no,stu.name,stu.chinese,stu.math,stu.english))
                    break
            else:
                print('该学号不存在')
                break
            choice = input('继续查询(y/n)?').lower()
            if choice == 'n':
                break

    def delete(self):
        #删除学生信息
        while True:
            no = input('请输入要删除的学生学号:')                
            for stu in self.stulist[::]:
                if stu.no == no:
                    self.stulist.remove(stu)
                    print('删除成功')
                    break
            else:
                print('该学号不存在')
                break
            choice = input('继续删除(y/n)?').lower()
            if choice == 'n':
                break


    def update(self):
        #修改学生信息
        while True:
            no = input('请输入要修改的学生学号:')
            if self.__exists(no):
                for stu in self.stulist:
                    if stu.no == no:
                        stu.name = input('姓名:')
                        stu.chinese = int(self.__enterScore('语文成绩:'))
                        stu.math = int(self.__enterScore('数学成绩:'))
                        stu.english = int(self.__enterScore('英语成绩:'))
                        print('修改成功')
                        break
            else:
                print('该学号不存在')
                break
            choice = input('继续修改(y/n)?').lower()
            if choice == 'n':
                break

    def load(self,fn):
        #导入学生信息
        if os.path.exists(fn):
            try:
                with open(fn,'r',encoding = 'utf-8') as fp:
                    while True:
                        fs = fp.readline().strip('\n')
                        if not fs:
                            break
                        else:
                            stu = Student(*fs.split(','))
                            if self.__exists(stu.no):
                                print('该学号已存在')
                            else:
                                self.stulist.append(stu)
                print('导入完毕')
            except:
                print('发生错误')
        else:
            print('要导入的文件不存在')
        

    def save(self,fn):
        #导出学生信息
        with open(fn,'w',encoding = 'utf-8') as fp:
            for stu in self.stulist:
                fp.write(stu.no + ',')
                fp.write(stu.name + ',')
                fp.write(str(stu.chinese) + ',')
                fp.write(str(stu.math) + ',')                    
                fp.write(str(stu.english) + '\n')                    
            print("导出完毕")

    def scoreavg(self):
        #求课程平均分
        length = len(self.stulist)
        if length > 0:
            chinese_avg = sum([stu.chinese for stu in self.stulist])/length
            math_avg = sum([stu.math for stu in self.stulist])/length
            english_avg = sum([stu.english for stu in self.stulist])/length
            print('语文成绩平均分是:%.2f'%chinese_avg)
            print('数学成绩平均分是:%.2f'%math_avg)
            print('英语成绩平均分是:%.2f'%english_avg)
        else:
            print('暂无学生成绩')

    def scoremax(self):
        #求课程最高分
        if len(self.stulist) > 0:
            chinese_max = max([stu.chinese for stu in self.stulist])
            math_max = max([stu.math for stu in self.stulist])
            english_max = max([stu.english for stu in self.stulist])
            print('语文成绩最高分是:%d'%chinese_max)
            print('数学成绩最高分是:%d'%math_max)
            print('英语成绩最高分是:%d'%english_max)
        else:
            print('暂无学生成绩')

    def scoremin(self):
        #求课程最低分
        if len(self.stulist) > 0:
            chinese_min = min([stu.chinese for stu in self.stulist])
            math_min = min([stu.math for stu in self.stulist])
            english_min = min([stu.english for stu in self.stulist])
            print('语文成绩最低分是:%d'%chinese_min)
            print('数学成绩最低分是:%d'%math_min)
            print('英语成绩最低分是:%d'%english_min)
        else:
            print('暂无学生成绩')

    def filesop(self):
        #文件操作
        print('文件操作')
        print('1.导入学生信息')
        print('2.导出学生信息')
        while True:
            s = input('请选择：')
            s = int(s)
            if s == 1:
                fn = input('请输入要导入的文件名:')
                self.load(fn)
            elif s == 2:
                fn = input('请输入要导出的文件名:')
                self.save(fn)
            else:
                print('输入错误')
    
    def scoreprocess(self):
        #学生成绩统计
        print('学生成绩统计')
        print('1.课程平均分')
        print('2.课程最高分')
        print('3.课程最低分')        
        while True:
            s = input('请选择：')
            s = int(s)
            if s == 1:                
                self.scoreavg()
            elif s == 2:                
                self.scoremax()
            elif s == 3:                
                self.scoremin()
            else:
                print('输入错误')