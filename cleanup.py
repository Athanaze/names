FILENAME = "fr/f.list"
s = set()

with open(FILENAME) as f:

    lines = f.readlines()
    
    for l in lines:
        s.add(l)

with open(FILENAME, "w") as f_clean:
    str_from_set = ""
    for e in s:
        str_from_set += e
    
    f_clean.write(str_from_set)