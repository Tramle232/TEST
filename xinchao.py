Diem = "2.5 3 4 5 9 10"
a= Diem.split()
# 1. Chuyển chuỗi thành danh sách số thực (thay thế cho toàn bộ vòng lặp for)
Diem_int = [float(x) for x in Diem.split()]

# 2. Tính điểm trung bình (hệ số 1, hệ số 2, hệ số 3)
a1, b1, c1, a2, b2, a3 = Diem_int
TB = round((a1 + b1 + c1 + (a2 + b2) * 2 + a3 * 3) / 10, 1)

print("Điểm trung bình:", TB)



######################
Diem = "2.5 3 4 5 9 10"
Diem_int = [0,0,0,0,0,0]

i = 0
tmp = ''
for x in Diem:
    if(x!=' '):
        tmp += x
    if(x ==' ' or  x == Diem[-1]):
        Diem_int[i] = float(tmp)
        print(Diem_int[i])
        i = i + 1
        tmp = ''

a1 = Diem_int[0]
b1 = Diem_int[1]
c1 = Diem_int[2] 
a2 = Diem_int[3] 
b2 = Diem_int[4]
a3 = Diem_int[5] 
TB = ((a1+b1+c1) + (a2+b2)*2 + a3*3)/10
TB = round(TB, 1)
print("Điểm trung bình: ", TB)








# Diem = [a1, b1, c1, a2, b2, a3]
# Diem = "2 3 4 5 9 10"
# a1 = int(Diem[0]) # "2" -> 2
# b1 = int(Diem[2]) # "3"
# c1 = int(Diem[4])
# a2 = int(Diem[6])
# b2 = int(Diem[8])
# a3 = int(Diem[10])

# TB = ((a1+b1+c1) + (a2+b2)*2 + a3*3)/10
# TB = round(TB, 1)
# print("Điểm trung bình: ", TB)