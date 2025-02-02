import student
def main():

    state = True
    while(state):
        print("1.添加学生信息\t2.查询学生信息")
        print("3.修改学生信息\t4.删除学生信息")
        print("5.显示所有学生信息\t6.统计功能")
        print("7.文件操作\t0.退出系统")
        option = input("请选择：")
        if option in ['0','1','2','3','4','5','6','7']:
            option = int(option)
            if option == 0:
                print("您已成功退出系统")
                state = False
            elif option == 1:
                inf = student.StudentList.insert()
            elif option == 2:
                student.StudentList.find()
            elif option == 3:
                student.StudentList.update()
            elif option == 4:
                student.StudentList.delete()
            elif option == 5:
                student.StudentList.show()
            elif option == 6:
                student.StudentList.scoreprocess()
            elif option == 7:
                student.StudentList.filesop()