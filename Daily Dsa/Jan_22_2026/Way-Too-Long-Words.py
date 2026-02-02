def avr(s):
    if len(s) > 10:
        return s[0]+f"{len(s)-2}"+s[-1]
    return s


print(avr("word"))
print(avr("localization"))
print(avr("internationalization"))
print(avr("pneumonoultramicroscopicsilicovolcanoconiosis"))
