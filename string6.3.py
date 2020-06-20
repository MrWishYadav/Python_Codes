text = "X-DSPAM-Confidence:    0.8475";
code = text.find('0')
bcode = text[code:]
dcode = float(bcode)
print(dcode)
