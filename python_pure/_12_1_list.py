# Heterojen List
heterojen_data = ["Mehmet", 10, 30, 40, 50, 60, 70, 80, True,14.53]


# Homojen List
homojen_data = [20, 10, 30, 40, 50, 60, 70, 80, 90]
print(homojen_data)
print(type(homojen_data))

# Saymaya sıfırdan başlar
print(f"ilk eleman ==> {homojen_data[0]}")
print(f"ilk eleman ==> {homojen_data[-5]}")

print(f"son eleman ==> {homojen_data[4]}")
print(f"son eleman ==> {homojen_data[-1]}")
print(f"son eleman ==> {homojen_data[len(homojen_data) - 1]}")


print("## slicing ##############################################")
print(homojen_data[0:4])  # 0<=NUMBER<=4-1
print(homojen_data[:4])   # 0<=NUMBER<=4-1
print(homojen_data[1:4])  # 1<=NUMBER<=4-1
print(homojen_data[::3])  # 0 - 3 - 6 - 9
print(homojen_data[1::3]) # 1 - 4 - 7 - 10

