'''
    已知信息：标准项目 1人80小时

        工时计算：
            输入：项目大小，人数
            输入：工时数量
        人力计算：
            输入：项目大小，工时数量
            输出：人数
    项目大小：project_size;人数：workers_number;工时数量：work_hours
'''
import time
def Work_Hours(project_size,workers_number):
    total_task = project_size * 80
    work_hours = total_task / workers_number
    return work_hours
def Workers_Number(project_size,work_hours):
    total_task = project_size * 80
    workers_number = total_task / work_hours
    return  workers_number

while True:
    print('********|工时计算器|*******')
    print('*\t\t1.工时计算\t\t*')
    print('*\t\t2.人力计算\t\t*')
    print('*注：标准项目 1人80小时\t\t*')
    print('*************************')
    choice = int(input('*计算方式：'))
    if choice == 1:
        while True:
            # 工时计算
            project_size = float(input('*工时计算|-项目大小：'))
            workers_number = int(input('*工时计算|-人数：'))
            if workers_number == 0:
                print('*[警告]人数不可为[0]，请重新输入。\n')
                continue
            else:
                result = Work_Hours(project_size=project_size,workers_number=workers_number)
                print(f'*所需工时数{result}')
            break
        break
    elif choice == 2:
        while True:
            # 人力计算
            project_size = float(input('*人力计算|-项目大小：'))
            work_hours = float(input('*工时计算|-工时数量：'))
            if work_hours == 0:
                print('*[警告]工时数不可为[0]，请重新输入。\n')
                continue
            else:
                result = Workers_Number(project_size=project_size,work_hours=work_hours)
                f_result = int(result)
                # 人数若是小数，则整数部分加1
                if result > f_result:
                    f_result += 1
                else:
                    f_result = result
                print(f'*所需人工数{f_result}')
                break
        break
    else:
        print('~暂无该选项，请重新输入。')
        i = 0
        while i<=2:
            time.sleep(1)
            print('.',end='')
            i+=1
        print('\n')
        continue
