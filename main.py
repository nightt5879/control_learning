# 成绩计算
# 总成绩计算
# def get_total_score(score_dict):
#     total_score = 0
#     for score in score_dict.values():
#         total_score += score
#     return total_score
# a = {'语文': 89, '数学': 92, '英语': 93, '物理': 90, '化学': 88, '生物': 85}
#
# print(get_total_score(a))

class School:
    def __init__(self, name, address, tel):
        self.name = name
        self.address = address
        self.tel = tel
        self.math = 0
        self.english = 0
        self.chinese = 0


    def score(self,chinese,math,english):
        self.math = math
        self.english = english
        self.chinese = chinese

    def get_total_score(self):
        total_score = self.chinese + self.math + self.english
        return total_score

a = School('小明', '北京市海淀区', '010-62752222')
a.score(90,80,70)
xm_score = a.get_total_score()
# 另一位同学
b = School('小红', '北京市海淀区', '010-62752222')
b.score(80,70,60)
xh_score = b.get_total_score()
print(a.name,'的成绩为：','语文：',a.chinese,'数学：',a.math,'英语：',a.english,'总分：',xm_score,sep='')
print(b.name,'的成绩为：','语文：',b.chinese,'数学：',b.math,'英语：',b.english,'总分：',xh_score,sep='')