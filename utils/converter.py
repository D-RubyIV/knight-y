def convert_to_number(s):
    if isinstance(s, str):
        s = s.strip().upper().replace(',', '')  # Loại bỏ dấu phẩy

        if s == 'LIKE' or s == '0'or s == '':
            return 0
        elif s.endswith('K'):
            return int(float(s[:-1]) * 1_000)
        elif s.endswith('M'):
            return int(float(s[:-1]) * 1_000_000)
        else:
            return int(float(s))  # Trường hợp còn lại là số bình thường

    return s  # Nếu đã là số thì giữ nguyên
data = [
    "7,122","104", "1.7K", "Like", "530K", "0", "89K", "459K", "147K", "19K", "1.1M",
    "242K", "0", "0", "1.1M", "83K", "187K", "33K", "122K", "1.4K", "57K", "0",
    "0", "2.1M", "633K", "2.1K", "194K", "0", "3.7K", "1.3K", "643", "0", "2.3K", "159K"
]

# Bỏ các phần tử không phải số như "Like"
cleaned_data = [convert_to_number(item) for item in data]

print(cleaned_data)