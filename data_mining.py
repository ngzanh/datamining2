import pandas as pd
# Tải dữ liệu từ tệp CSV
df = pd.read_csv("student_dataset_100rows.csv")
#xu ly du lieu tuoi bi thieu
df['Tuoi'] = df['Tuoi'].replace(r'^\s*$', None, regex=True)
df['Tuoi'].fillna(df['Tuoi'].mode()[0], inplace=True)

#xu ly du lieu nhieu cua tuoi (180)
mode = df['Tuoi'].mode()[0]
df.loc[df['Tuoi'] >150, 'Tuoi'] = mode


#xu ly du lieu luong bi nhieu (-3)
median = df['Luong'].median()
df.loc[df['Luong'] <0, 'Luong'] = median

#xu ly du lieu khong nhat quan cua gioi tinh
mapping = {
'nam': 'Nam',
'male': 'Nam',
'm': 'Nam',
'nữ': 'Nữ',
'female': 'Nữ',
'f': 'Nữ',
'An Gian': 'An Giang',
'Hà Nộ': 'Hà Nội'
}
df['GioiTinh'] = df['GioiTinh'].str.lower().map(mapping)

#xu ly du lieu khong nhat quan cua thanh pho
mapp = {
'An Gian': 'An Giang',
'Hà Nộ': 'Hà Nội',
'HN': 'Hà Nội',
}
df['ThanhPho'] = df['ThanhPho'].str.lower().map(mapp)

#xu ly du lieu nhieu thieu cua sdt
df['SDT'] = df['SDT'].replace(r'^\s*$', None, regex=True)
df['SDT'] = df['SDT'].fillna("Unknown")

df.to_csv('du_lieu_da_lam_sach_student.csv', index=False)


import pandas as pd
# Tải dữ liệu từ tệp CSV
df = pd.read_csv("customer_data.csv")
# Xem vài dòng đầu
#print(df.head())
# Kiểm tra tổng số giá trị thiếu trong mỗi cột
#print(df.isnull().sum())
# Xóa các hàng chứa bất kỳ giá trị thiếu nào
#df_cleaned = df.dropna()
print(df.head()) # 5 dòng đầu
print(df.tail())
print(df.isnull().sum())
# Thay thế các giá trị tuoi thiếu bằng giá trị trung bình (mode) của cột đó
df['Tuoi'] = df['Tuoi'].replace(r'^\s*$', None, regex=True)
df['Tuoi'].fillna(df['Tuoi'].mode()[0], inplace=True)

#xu ly du lieu tuoi bi nhieu (200)
mode = df['Tuoi'].mode()[0]
df.loc[df['Tuoi'] ==200, 'Tuoi'] = mode


#xoa du lieu khong nhat quan cua cot Luong (8tr)
df['Luong'] = pd.to_numeric(df['Luong'], errors='coerce')
df.dropna(subset=['Luong'], inplace=True)

#xu ly luong nhieu bằng giá trị thống kê (mean/median)
median = df['Luong'].median()
df.loc[df['Luong'] <0, 'Luong'] = median

#xu ly du lieu ko nhat quat cua gioi tinh
mapping = {
'nam': 'Nam',
'male': 'Nam',
'm': 'Nam',
'nữ': 'Nữ',
'female': 'Nữ',
'f': 'Nữ'
}
df['Gioi tinh'] = df['Gioi tinh'].str.lower().map(mapping)

#xoa dong trung hoan toan
df.drop_duplicates(subset=['Tên KH','Luong','Gioi tinh'], inplace=True)

#xu ly du lieu nhieu thieu cua sdt
df['SDT'] = df['SDT'].replace(r'^\s*$', None, regex=True)
df['SDT'] = df['SDT'].fillna("Unknown")
df['SDT'] = df['SDT'].replace(0, None, regex=True)
df['SDT'] = df['SDT'].fillna("Unknown")

#xu ly du lieu ngoai lai
Q1 = df['Luong'].quantile(0.25)
Q3 = df['Luong'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['Luong'] < lower) | (df['Luong'] > upper)]
print(outliers)
#thay the du lieu ngoai lai luong =100
median = df['Luong'].median()
df.loc[df['Luong'] ==100, 'Luong'] = median

df.to_csv('du_lieu_da_lam_sach.csv', index=False)

import pandas as pd
df=pd.read_csv("student_scores_raw.csv")

#PHAN 1: LAM SACH DU LIEU

#1.1: du lieu bi thieu
#dem gia tri thieu
print ("tong gia tri thieu trong du lieu: ",df.isna().sum().sum())

print("Ti lie % thieu: ",df.isna().mean().mean() * 100)

print("so gia tri thieu trong cot Age la",df['Age'].isna().sum())
print("so gia tri thieu trong cot Score_Math la",df['Score_Math'].isna().sum())
print("so gia tri thieu trong cot Score_Engish la",df['Score_English'].isna().sum())
print("so gia tri thieu trong cot Score_Physics la",df['Score_Physics'].isna().sum())
print("so gia tri thieu trong cot Attendance la",df['Attendance'].isna().sum())
print("so gia tri thieu trong cot Grade la",df['Grade'].isna().sum())
print("so gia tri thieu trong cot Income la",df['Income'].isna().sum())


#Thay the du lieu bi thieu o cot age bang gia tri median
df['Age'] = df['Age'].fillna(df['Age'].median())

#Thay the du lieu bi thieu o cot score_math bang mean
df['Score_Math'] = df['Score_Math'].fillna(df['Score_Math'].mean())

#Thay the du lieu bi thieu o cot score_English bang mean
df['Score_English'] = df['Score_English'].fillna(df['Score_English'].mean())


#cột Income: thay bằng mean theo nhóm City
df['Income'] = df['Income'].fillna(df.groupby('City')['Income'].transform('mean'))
    
#1.2: du lieu nhieu
noise_age = df[(df['Age'] < 17) | (df['Age'] > 25)]
print("Du lieu nhieu cua age:")
print(noise_age)


noise_sm = df[(df['Score_Math'] < 0) | (df['Score_Math'] > 10)]
print("Du lieu nhieu cua score_math:")
print(noise_sm)


noise_se = df[(df['Score_English'] < 0) | (df['Score_English'] > 10)]
print("Du lieu nhieu cua score_english:")
print(noise_se)


noise_sp = df[(df['Score_Physics'] < 0) | (df['Score_Physics'] > 10)]
print("Du lieu nhieu cua score_Physics:")
print(noise_sp)


noise_atten = df[(df['Attendance'] < 0) | (df['Attendance'] > 100)]
print("Du lieu nhieu cua Attendance:")
print(noise_atten)

#xoa hang co du lieu age <0 ||age>100 -> giu lai hang co age >=0 && age<=100
df = df[(df['Age'] >= 0) & (df['Age'] <= 100)]

#thay the score >100
median = df['Score_Math'].median()
df.loc[df['Score_Math']>10, 'Score_Math'] = median

median = df['Score_English'].median()
df.loc[df['Score_English']>10, 'Score_English'] = median

median = df['Score_Physics'].median()
df.loc[df['Score_Physics']>10, 'Score_Physics'] = median

#khong co du lieu nhieu o cot attendance


#Câu 1.3: Phát hiện và xử lý Outliers (1 điểm)
#a) Phát hiện ngoại lai bằng IQR (0.5 điểm)
Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df['Income'] < Q1 - 1.5*IQR) |
    (df['Income'] > Q3 + 1.5*IQR)
]
#phat hien ngoai lai
print("Ngoai lai cua income: ")
print(outliers)#['Income'])

#ve boxplot
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=df['Income'])
plt.title("Boxplot tien xu ly Income")
plt.show()

max=Q3 + 1.5*IQR
min=Q1 - 1.5*IQR

#xu li ngoai lai income
df.loc[df['Income']>max, 'Income'] = max
df.loc[df['Income']<min, 'Income'] = min

sns.boxplot(x=df['Income'])
plt.title("Boxplot sau xu ly Income")
plt.show()


#Câu 1.4: Xử lý Inconsistent Data

mapping_gt = {
    'Female': 'Nữ',
    'M': 'Nam',
    'm': 'Nam',
    'nu': 'Nữ',
    'F': 'Nữ',
    'NAM':'Nam',
    'male':'Nam',
    'Male':'Nam',
    'nam': 'Nam',
    'Ná»¯':'Nữ',
    'Nam':'Nam',
    'Nữ':'Nữ'
}

df['Gender'] = df['Gender'].map(mapping_gt)

#Grade: chuẩn hóa chữ hoa đầu (Good, Medium, Excellent, Weak)
df['Grade'] = df['Grade'].str.title()

#City: loại bỏ khoảng trắng thừa
df['City'] = df['City'].str.strip().str.title()

#Câu 1.5: Loại bỏ Duplicate Data
#Phat hien dong trung hoan toan
df_trung = df[df.duplicated()]
print("dong trung 100%:")
print(df_trung)



#phat hien dong trung StudentID
print("Trung StudentID: ")
print(df[df.duplicated(subset=["StudentID"], keep=False)])

#Loại bỏ dữ liệu trùng lặp, giữ lại bản ghi đầu tiên
df= df.drop_duplicates()

#PHẦN 2: BIẾN ĐỔI DỮ LIỆU
#điểm trung binh 3 môn
df['Average_Score']=(df['Score_English']+df['Score_Math']+df['Score_Physics'])/3

#tổng số sv theo từng thành phố
df.groupby("City").size().reset_index(name="TongSoSinhVien")
print(df.groupby("City").size().reset_index(name="TongSoSinhVien"))

#Tính điểm trung bình theo từng Grade


df.to_csv('student_scores_final.csv',index=False)

def tinh_support_confidence_lift(mang, X, Y):
    n = len(mang)

    count_X = 0
    count_Y = 0
    count_XY = 0

    for t in mang:
        if X.issubset(t):
            count_X += 1
        if Y.issubset(t):
            count_Y += 1
        if X.union(Y).issubset(t):
            count_XY += 1

    support = count_XY / n

    if count_X!=0:
        confidence = count_XY/ (count_X )
    else :confidence=0

    if count_Y!=0:
        lift = confidence / (count_Y / n) 
    else:lift= 0

    return support, confidence, lift


# ===== NHẬP DỮ LIỆU =====
mang = []

n = int(input("Nhập số lượng giao dịch: "))

print("Nhập từng giao dịch (cách nhau bằng dấu phẩy, ví dụ: A,B,C)")
for i in range(n):
    items = input(f"Giao dịch {i+1}: ").split(",")
    mang.append(set(item.strip() for item in items))

# Nhập luật
rule = input("Nhập luật cần kiểm tra (ví dụ: A,B -> C): ")

left, right = rule.split("->")
X = set(item.strip() for item in left.split(","))
Y = set(item.strip() for item in right.split(","))

# ===== TÍNH TOÁN =====
support, confidence, lift = tinh_support_confidence_lift(mang, X, Y)

# ===== IN KẾT QUẢ =====
print("\nKẾT QUẢ:")
print("Support =", support)
print("Confidence =",confidence)
print("Lift =",lift)

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# --- BƯỚC 1: ĐỊNH NGHĨA CẤU TRÚC DỮ LIỆU ---
num_features = int(input("1. Bạn muốn có bao nhiêu cột đặc trưng (ví dụ: 3)? "))
feature_names = []
for i in range(num_features):
    name = input(f"   - Nhập tên cột thứ {i+1}: ")
    feature_names.append(name)

num_samples = int(input("\n2. Bạn muốn nhập bao nhiêu dòng dữ liệu mẫu để máy học? "))

X_train = []
y_train = []

print("\n--- BẮT ĐẦU NHẬP DỮ LIỆU MẪU ---")
for i in range(num_samples):
    print(f"Dòng thứ {i+1}:")
    row = []
    for j in range(num_features):
        val = float(input(f"   Nhập giá trị cho '{feature_names[j]}': "))
        row.append(val)
    X_train.append(row)
    label = input(f"   => Kết quả/Nhãn của dòng này là gì? ")
    y_train.append(label)

# Chuyển sang dạng mảng Numpy
X_train = np.array(X_train)
y_train = np.array(y_train)

# --- BƯỚC 2: HUẤN LUYỆN ---
# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Khởi tạo KNN (mặc định K=3 hoặc nhỏ hơn nếu dữ liệu ít)
k_value = min(3, num_samples)
knn = KNeighborsClassifier(n_neighbors=k_value)
knn.fit(X_train_scaled, y_train)

print("\n" + "="*30)
print("MÁY ĐÃ HỌC XONG DỮ LIỆU CỦA BẠN!")
print("="*30)

# --- BƯỚC 3: DỰ ĐOÁN DỮ LIỆU MỚI ---
while True:
    print("\n--- NHẬP DỮ LIỆU MỚI ĐỂ DỰ ĐOÁN ---")
    new_input = []
    for j in range(num_features):
        val = float(input(f"Nhập {feature_names[j]}: "))
        new_input.append(val)
    
    # Xử lý và dự đoán
    new_input_scaled = scaler.transform([new_input])
    prediction = knn.predict(new_input_scaled)
    
    print(f"\n>>> KẾT QUẢ DỰ ĐOÁN: {prediction[0]}")
    
    # Hỏi xem có muốn tiếp tục không
    tiep_tuc = input("\nBạn có muốn dự đoán tiếp không? (c/k): ")
    if tiep_tuc.lower() != 'c':
        break

print("Cảm ơn bạn đã sử dụng chương trình!")