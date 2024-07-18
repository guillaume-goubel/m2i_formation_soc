import binascii

hexa_code = "504B030414000008000044B6B86E3F7BA8328127B8A9FC5A1FEE3F46921A0"
decoded_string = binascii.unhexlify(hexa_code).decode('utf-8')
print("Decoded String:", decoded_string)


