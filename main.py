import string
import random

chars = list(string.ascii_uppercase + string.digits)
split_indexes = [6, 11, 16, 25]
frequency = int(input("请输入生成数量："))

def generate_code():
    result = []
    for _ in range(26):
        result.append(random.choice(chars))
    for i in split_indexes:
        result.insert(i, "-")
    return "".join(result)

# ✅ 生成多个（例如 5 个）
for _ in range(frequency):
    print(generate_code())