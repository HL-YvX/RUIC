import string
import random
import os
import hashlib
import base64

chars = list(string.ascii_uppercase + string.digits)
split_indexes = [6, 11, 16, 25, 30]
frequency = int(input("请输入生成数量："))

# ✅ 生成原始 RUIC
def generate_raw_code():
    result = []
    for _ in range(26):
        result.append(random.choice(chars))
    for i in split_indexes:
        result.insert(i, "-")
    return "".join(result)

def ruic_hash_tail(ruic: str, segment_count: int = 5, hash_length: int = 16) -> str:
    """
    为给定的 RUIC 字符串生成并添加哈希校验段。

    参数:
    ruic (str): 原始的 RUIC 字符串，各段之间由连字符 '-' 分隔。
    segment_count (int, 可选): 用于生成哈希的 RUIC 段数，默认为 5。
    hash_length (int, 可选): 生成的哈希校验段的长度，默认为 16。

    返回:
    str: 包含新生成哈希校验段的 RUIC 字符串。
    """
    # 去除 RUIC 字符串两端的空白字符，并按连字符 '-' 分割成多个段
    parts = ruic.strip().split('-')
    # 拼接前 segment_count 个段，作为生成哈希的核心内容
    core = ''.join(parts[:segment_count])
    # 使用 SHA-256 算法对核心内容进行哈希计算，得到字节形式的摘要
    digest = hashlib.sha256(core.encode()).digest()
    # 对字节摘要进行 Base32 编码，转换为字符串，去除末尾的填充字符 '=' 并转为大写
    base32 = base64.b32encode(digest).decode().rstrip('=').upper()
    # 截取前 hash_length 个字符作为最终的哈希校验段
    hash_tail = base32[:hash_length]
    # 用新生成的哈希校验段替换原始 RUIC 的最后一段
    parts[-1] = hash_tail
    # 将各段用连字符 '-' 重新拼接成完整的 RUIC 字符串
    return '-'.join(parts)

# ✅ 批量生成带校验段的 RUIC
for _ in range(frequency):
    raw = generate_raw_code()
    final = ruic_hash_tail(raw)
    print(final)

os.system("pause")
