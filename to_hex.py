def rgb_to_hex(rgb, remove_alpha = True):
    hex_out = ""
    for channel in rgb:
        channel_hex = hex(channel)
        hex_out += channel_hex[2:len(channel_hex)]
    if remove_alpha:
        hex_out = hex_out[0:-2]
        hex_digit_length = len(hex_out)
        if hex_digit_length < 6:
            hex_out += "0" * (6 - hex_digit_length)
    return hex_out