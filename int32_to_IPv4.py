def int32_to_ip(int32):
    ip_v4 = ["", "", "", ""]
    int32 = bin(int32)[2:]
    int32 = "0"*(32 - len(int32)) + int32
    index = 0
    for x in range(len(ip_v4)):
        ip_v4[x] = str(int(int32[index:index+8], 2))
        index+=8
    return ".".join(ip_v4)