import csv
import re

waijiaji_file = "csv表/外加剂质量台账列表.csv"
peihebi_file = "csv表/施工配合比相关数据.csv"
shuini_file = "csv表/水泥质检列表.csv"
shihuishi_file = "csv表/石灰石粉质量检测列表.csv"
kuangzhafen_file = "csv表/矿渣粉质量检测列表.csv"
fenmeihui_file = "csv表/粉煤灰质量检测列表.csv"
pengzhangji_file = "csv表/膨胀剂质量检测列表.csv"


def read_data():
    waijiaji = []
    with open(waijiaji_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # 读取第一行
        for row in csv_reader:
            new_row = []
            new_row.append(row[2])
            new_row.append(row[3])
            try:
                new_row.append(float(row[13]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[15]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[16]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[19]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[20]))
            except:
                new_row.append(-1)
            waijiaji.append(new_row)

    shuini = []
    with open(shuini_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # 读取第一行
        for row in csv_reader:
            new_row = []
            new_row.append(row[1])
            new_row.append(row[2])
            try:
                new_row.append(float(row[20]))
            except:
                new_row.append(-1)
            new_row.append(row[3])
            shuini.append(new_row)

    shihuishi = []
    with open(shihuishi_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # 读取第一行
        for row in csv_reader:
            new_row = []
            new_row.append(row[1])
            try:
                new_row.append(float(row[13]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[15]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[17]))
            except:
                new_row.append(-1)
            shihuishi.append(new_row)

    kuangzhafen = []
    with open(kuangzhafen_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # 读取第一行
        for row in csv_reader:
            new_row = []
            new_row.append(row[2])
            new_row.append(row[3])
            try:
                new_row.append(float(row[18]))
            except:
                new_row.append(-1)
            new_row.append(row[4])
            kuangzhafen.append(new_row)

    fenmeihui = []
    with open(fenmeihui_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # 读取第一行
        for row in csv_reader:
            new_row = []
            new_row.append(row[1])
            new_row.append(row[2])
            new_row.append(row[3])
            try:
                new_row.append(float(row[14]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[15]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[16]))
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[17]))
            except:
                new_row.append(-1)
            fenmeihui.append(new_row)

    pengzhangji = []
    with open(pengzhangji_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # 读取第一行
        for row in csv_reader:
            new_row = []
            new_row.append(row[1])
            new_row.append(row[2])
            try:
                new_row.append(float(row[17]))
            except:
                new_row.append(-1)
            new_row.append(-1)
            pengzhangji.append(new_row)

    all_data = []
    regex1 = re.compile("./([0-9]+)/.")
    regex2 = re.compile("(0\.[0-9]+)%")
    regex3 = re.compile("^0*(.+)")
    with open(peihebi_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # 读取第一行
        for row in csv_reader:
            new_row = []
            new_row.append(float(regex1.findall(row[10])[0]))  # yue
            new_row.append(row[51])  # 混凝土品种
            new_row.append(row[52])  # 强度等级
            new_row.append(row[53])  # 抗渗等级
            new_row.append(row[54])  # 材料要求
            reg = regex2.findall(row[55])  # 限制膨胀率
            if len(reg) != 0:
                new_row.append(float(reg[0]))
            else:
                new_row.append(-1)
            try:
                new_row.append(float(row[14]))  # 塌落度
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[15]))  # 扩展度
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[33]))  # 水泥用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[23]))  # 特细砂用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[49]))  # 中砂用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[35]))  # 粗砂用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[47]))  # 小石用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[27]))  # 大石用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[21]))  # 减水剂用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[41]))  # 粉煤灰用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[31]))  # 矿渣粉用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[25]))  # 石灰石粉用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[29]))  # 膨胀剂用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[43]) + float(row[37]))  # 水用量+回收水用量
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[16]))  # 表观密度
            except:
                new_row.append(-1)

            new_row.append(2)  # 生产车间
            new_row.append(3)  # 主供车间
            new_row.append(9)  # 生产线
            new_row.append(11)  # 浇注方式
            try:
                new_row.append(float(row[17]))  # 3d强度
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[18]))  # 7d强度
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[19]))  # 28d强度
            except:
                new_row.append(-1)
            try:
                new_row.append(float(row[20]))  # 60d强度
            except:
                new_row.append(-1)

            shuinihao = row[34]
            signal = 1
            for row1 in shuini:
                if shuinihao == regex3.findall(row1[0])[0]:
                    signal = 0
                    new_row += row1[1:]
                    break
            if signal == 1:
                new_row += ['', -1, '']

            waijiajihao = row[22]
            signal = 1
            for row1 in waijiaji:
                if waijiajihao == regex3.findall(row1[0])[0]:
                    signal = 0
                    new_row += row1[1:]
                    break
            if signal == 1:
                new_row += ['', -1, -1, -1, -1, -1]

            fenmeihuihao = row[42]
            signal = 1
            for row1 in fenmeihui:
                if fenmeihuihao == regex3.findall(row1[0])[0]:
                    signal = 0
                    new_row += row1[1:]
                    break
            if signal == 1:
                new_row += ['', '', -1, -1, -1, -1]

            kuangzhafenhao = row[32]
            signal = 1
            for row1 in kuangzhafen:
                if kuangzhafenhao == regex3.findall(row1[0])[0]:
                    signal = 0
                    new_row += row1[1:]
                    break
            if signal == 1:
                new_row += ['', -1, '']

            shihuishihao = row[26]
            signal = 1
            for row1 in shihuishi:
                if shihuishihao == regex3.findall(row1[0])[0]:
                    signal = 0
                    new_row += row1[1:]
                    break
            if signal == 1:
                new_row += [-1, -1, -1]

            pengzhangjihao = row[30]
            signal = 1
            for row1 in pengzhangji:
                if pengzhangjihao == regex3.findall(row1[0])[0]:
                    signal = 0
                    new_row += row1[1:]
                    break
            if signal == 1:
                new_row += ['', -1, -1]

            all_data.append(new_row)

    return all_data


if __name__ == '__main__':
    d = read_data()
