""" module's name : base64
    Description of the first ISN test : Make minimalist functions to encode or decode base64 sentence.

    Creator : Eyyüb "Eyyub" SARI(eyyub.pangearaion@gmail.com)
    Teacher : Ms. El Fati
"""


BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyr0123456789+/" #0-63

def _ascii_to_hex(symbol):
    """ encode an ASCII symbol to an hex char """
    return symbol.encode("hex")

def _string_to_hex(sentence):
    """ convert a string to an hex list """
    return [ascii_to_hex(symbol) for symbol in sentence]

def _hex_to_bin(hex_list):
    """ convert a hex list to a bin list """
    return [bin(int(value, 16)) for value in hex_list]

def _split_bin6(bin_list):
    """ split bin_list to a bin list of which the len element is 6 """ 
    bin_str = ""
    for b in bin_list:
        bin_str += "0" * (8 - len(b[2:]) ) + b[2:] 
    bin6_list = [bin_str[i:i+6] for i in range(0, len(bin_str), 6)]
    if len(bin6_list[-1]) != 6:
        bin6_list[-1] += "=" * ((6 - len(bin6_list[-1]))/2)
    return bin6_list

def _bin_to_dec(bin6_list):
    """ convert bin6_list to a decimal list """
    dec_list = []
    for nb in bin6_list:
        if '=' in nb:
            dec_list.append(str(int(nb[:nb.find("=")] + nb.count("=") * 2 * "0", 2)) + nb[nb.find("="):])
        else:
            dec_list.append(str(int(nb, 2)))
    return dec_list

def _dec_to_base64(dec_list):
    """ convert dec_list to a base64 sentence """
    base64 = ""
    
    for i in dec_list:
            if '=' in i:
                base64 += BASE64_TABLE[int(i[:i.find("=")])] + i[i.find("="):]
            else:
                base64 += BASE64_TABLE[int(i)]
    return base64

def _base64_to_dec(sentence):
    """ convert a sentence to a decimal list """
    dec = []
    for symbol in sentence:
        if symbol == '=':
            dec[-1] = dec[-1] + symbol
        else:
            dec.append(str(BASE64_TABLE.find(symbol)))
    return dec

def _dec_to_bin(dec_list):
    """ convert dec_list to a bin list """
    bin_list = []
    for nb in dec_list:
        if '=' in nb:
            bin_list.append(str(bin(int(nb[:nb.find("=")])))[2:] + nb[nb.find("="):])
        else:
            bin_list.append(str(bin(int(nb)))[2:])
    bin_final_list = []
    for b in bin_list:
        if "=" in b:
            bin_final_list.append((6 - (len(b) - b.count("="))) * "0" + b)
        else:
            bin_final_list.append((6 - len(b)) * "0" + b)
            
    return bin_final_list

def _split_bin8(bin_list):
    """ split bin_list to a bin list of which the len element is 8 """
    bin8_str = "".join(bin_list)
    if "=" in bin8_str:
        nb_equal_sign = bin8_str.count("=")
        bin8_str = bin8_str[:len(bin8_str) - nb_equal_sign]
        bin8_str = bin8_str[:len(bin8_str) - nb_equal_sign * 2]
    bin8_list = [bin8_str[i:i+8] for i in range(0, len(bin8_str), 8)]
    return bin8_list

def _bin_to_hex(bin8_list):
    """ convert bin8_list to a hex list """
    return [str(hex(int(bin, 2)))[2:] for bin in bin8_list]

def _hex_to_ascii(value):
    """ convert an hex value to an ascii symbol """
    return chr(int(value, 16))

def _hex_list_to_string(hex_list):
    """ convert hex_list to a string """
    return "".join([hex_to_ascii(value) for value in hex_list])

def encode(sentence):
    """ encode sentence to base64 """
    return _dec_to_base64(_bin_to_dec(_split_bin6(_hex_to_bin(_string_to_hex(sentence)))))

def decode(string):
    """ decode base64 string to a sentence """
    return _hex_list_to_string(_bin_to_hex(_split_bin8(_dec_to_bin(_base64_to_dec(string)))))
