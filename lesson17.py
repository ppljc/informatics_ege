def fund_letters(ip, mask, letters: []):
    ip_split = str.split(ip)
    mask_split = str.split(mask)
    net_split = [0, 0, 0, 0]
    for a in range(0, 4):
        if mask_split[a] == 255:
            net_split[a] = ip_split[a]
        elif mask_split[a] == 0:
            net_split[a] = 0
        else:
            ip_bin = bin(ip_split[a])[2:]
            mask_bin = bin(mask_split[a])[2:]
            if len(ip_bin) != 8:
                ip_bin = ('0'*(8 - len(ip_bin))) + ip_bin
