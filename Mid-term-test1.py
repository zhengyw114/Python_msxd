# 要求：
#
# 读取 report.txt 文件中的成绩；
# 统计每名学生总成绩、计算平均并从高到低重新排名；
# 汇总每一科目的平均分和总平均分（见下表第一行）；
# 添加名次，替换60分以下的成绩为“不及格”；
# 将处理后的成绩另存为一个新文件。

title = ["名次","姓名","语文","数学","英语","物理","化学","生物","政治","历史","地理","总分","平均分"]
score = []
score_list = []
total = ["total",]
average = ["average",]
a = 0
t_score = 0
#读取文件
with open("report.txt", encoding = "utf-8") as f:
    for l in f.readlines():
        score.append(l.strip())
for i in range(0,len(score)):
    score_list.append(score[i].split())
#生成各学生总分平均分
for j in range(0,len(score_list)):
    for m in range(1,len(score_list[j])):
        score_list[j][m] = int(score_list[j][m])
        a += score_list[j][m]
    score_list[j].append(a)
    score_list[j].append(round(a/m,1))
    a = 0

    # print(score_list[j])
#排序
score_list = sorted(score_list,key=lambda x:x[len(x)-1], reverse=True)
#print(sr_list)
#添加平均分
score_list.insert(0, average)
#添加名次
for j in range(0,len(score_list)):
    score_list[j].insert(0,score_list.index(score_list[j]))
# print(score_list)

#生成学科平均分，总分
for m in range(2,len(score_list[j])):
    for j in range(1, len(score_list)):
        t_score += score_list[j][m]
    total.append(t_score)
    average.append(round(t_score/j,1))
    t_score = 0
    # print(total)
    # print(average)

#添加抬头
score_list.insert(0,title)
#更改“不及格”,想用列表解析没成功
for m in range(2,len(score_list[j])):
    for j in range(2, len(score_list)):
        if score_list[j][m] <60  :
            score_list[j][m] = "不及格"

for m in range(0,len(score_list)):
    for n in range(0,len(score_list[m])):
        score_list[m][n]=str(score_list[m][n])
    score_list[m]=",".join(score_list[m])
score_output="/n".join(score_list)

#存成新文件
with open("export.txt","w",encoding="utf-8") as f2:
    f2.write(score_output)


