def input_student():
    l = []
    while True:
        try:
            n = input('请输入姓名： ')
            if not n:
                break
            a = int(input('请输入年龄： '))
            s = int(input('请输入成绩： '))
        except:
            print('输入有误，请重新输入')
            continue
        d = {}
        d['name'] = n
        d['age'] = a
        d['score'] = s
        l.append(d)
    return l

def output_student(l):
    print('+---------------+----------+----------+')
    print('|     name      |    age   |  score   |')
    print('+---------------+----------+----------+')
    for d in l:
        n = d['name']
        a = d['age']
        s = d['score']
        print('|%s|%s|%s|' % (n.center(15),str(a).center(10),str(s).center(10)))
    print('+---------------+----------+----------+')

def del_student(L):
    n = input('请输入删除学生的姓名:')
    for i in range(len(L)):
        if L[i]['name'] == n:
            del L[i]
            break

def modify_student_xinxi(L):
    n = input('请输入修改学生的姓名:')
    a = input('请输入修改学生的年龄:')
    s = input('请输入修改学生的成绩:')
    for i in range(len(L)):
        if L[i]['name'] == n:
            L[i]['age'] = a
            L[i]['score'] = s
            break

def score_gd_print(L):
    
    l2 = sorted(L,key = lambda d : d['score'] ,reverse = True)
    output_student(l2)

def score_dg_print(L):
    l2 = sorted(L,key = lambda d : d['score'] )
    output_student(l2)

def age_gd_print(L):
    l2 = sorted(L,key = lambda d : d['age'] ,reverse = True)
    output_student(l2)

def age_dg_print(L):
    l2 = sorted(L,key = lambda d : d['age'] )
    output_student(l2)
    
    

def shoumenu():
    print('+---------------+----------+----------+')
    print('| 1)添加信息                          |')
    print('| 2)显示信息                          |')
    print('| 3)删除信息                          |')
    print('| 4)修改信息                          |')
    print('| 5)成绩高低显示                      |')
    print('| 6)成绩低高显示                      |')
    print('| 7)年龄高低显示                      |')
    print('| 8)年龄低高显示                      |')
    print('| q)退出                              |')
    print('+---------------+----------+----------+')
def main():
    L=[]
    while True:
        shoumenu()
        s = input('请选择：')
        if s == 'q':
            break
        elif s == '1':
            L += input_student()
        elif s == '2':
            output_student(L)
        elif s == '3':
            del_student(L)
        elif s == '4':
            modify_student_xinxi(L)
        elif s == '5':
            score_gd_print(L)
        elif s == '6':
            score_dg_print(L)
        elif s == '7':
            age_gd_print(L)
        elif s == '8':
            age_dg_print(L)

main()

   
