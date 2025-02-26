print("Nhập các dòng văn bản (Nhập 'done' khi kết thúc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print('\nChuyển các dòng thành chữ in hoa và in ra màn hình')
for line in lines:
    print(line.upper())