import statistics


class StudentSystem:
    def __init__(self):
        prefill = input("是否需要预先填充示例数据?（1：是，2：否）: ")
        if prefill == '1':
            self.students = {
                '小红': {'年级': '一年级', '语文': 85, '数学': 90, '英语': 88},
                '小明': {'年级': '二年级', '语文': 92, '数学': 80, '英语': 76},
                '小蓝': {'年级': '一年级', '语文': 78, '数学': 88, '英语': 82},
                '小黄': {'年级': '三年级', '语文': 88, '数学': 75, '英语': 90}
            }
        else:
            self.students = {}

    def add_student(self):
        name = input("请输入学生的姓名：")
        if name in self.students:
            print("添加失败，同名学生已存在，请联系管理员。")
            return
        grade = input("请输入学生的年级：")
        chinese_score = float(input("请输入语文成绩："))
        math_score = float(input("请输入数学成绩："))
        english_score = float(input("请输入英语成绩："))
        self.students[name] = {'年级': grade, '语文': chinese_score, '数学': math_score, '英语': english_score}
        print("添加成功。")

    def search_student(self):
        while True:
            search_mode = input("请选择搜索模式（1：最高分，2：按名字搜索）：")
            if search_mode in ['1', '2']:
                break
            print("无效输入，请重新选择 1：最高分 或 2：按名字搜索。")

        if search_mode == '1':
            while True:
                subject = input("请选择科目（1：语文，2：数学，3：英语）：")
                subject_map = {'1': '语文', '2': '数学', '3': '英语'}
                if subject in subject_map.keys():
                    subject = subject_map[subject]
                    break
                print("无效输入，请选择 1：语文，2：数学，3：英语。")
            max_score = max(self.students.items(), key=lambda x: x[1][subject])
            print(f"{subject}最高分是：{max_score[0]}，分数是：{max_score[1][subject]}")
        elif search_mode == '2':
            name = input("请输入学生姓名：")
            if name in self.students:
                print(self.students[name])
            else:
                print("没有找到该学生。")

    def query_data(self):
        if not self.students:
            print("数据库里没有数据，请先添加学生信息。")
            return

        while True:
            query_mode = input("请选择查询数据（1：平均分，2：中位数，3：方差）：")
            query_map = {'1': '平均分', '2': '中位数', '3': '方差'}
            if query_mode in query_map.keys():
                query_mode = query_map[query_mode]
                break
            print("无效输入，请重新选择 1：平均分，2：中位数，3：方差。")

        for subject in ['语文', '数学', '英语']:
            if query_mode == '平均分':
                avg_score = statistics.mean([stu[subject] for stu in self.students.values()])
                print(f"{subject}的平均分是：{avg_score}")
            elif query_mode == '中位数':
                median_score = statistics.median([stu[subject] for stu in self.students.values()])
                print(f"{subject}的中位数是：{median_score}")
            elif query_mode == '方差':
                variance_score = statistics.variance([stu[subject] for stu in self.students.values()])
                print(f"{subject}的方差是：{variance_score}")


if __name__ == "__main__":
    system = StudentSystem()
    while True:
        action = input("请选择操作（1：添加学生，2：搜索学生，3：查询数据，4：退出）：")
        if action == '1':
            system.add_student()
        elif action == '2':
            system.search_student()
        elif action == '3':
            system.query_data()
        elif action == '4':
            print("退出系统。")
            break
        else:
            print("无效输入，请重新选择。")
