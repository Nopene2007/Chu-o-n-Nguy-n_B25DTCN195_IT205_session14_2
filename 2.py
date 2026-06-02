# phan tich loi
    # la bien toan cuc. Vi no nam ben ngoai tat ca cac ham
    # khi bien trong ham bi gan dau =, thi python se mac dinh no la bien cuc bo
    # khi la bien cuc bo, python se bo qua bien toan cuc ben ngoai, nhung trong bien chua duoc gan gia tri
    # khong loi

# sua loi
total_points = 100

def add_reward_points(current_total, points_earned):
    print("Đã cộng thêm", points_earned, "điểm.")
    return current_total + points_earned

total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)   