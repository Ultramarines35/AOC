j1 = open("j1.txt", "r").read().splitlines()
res = 0
for elem in j1:
    first_number = 0
    is_first_found = False
    final_number = 0
    is_final_number = False
    for c in elem:
        if c.isdigit() :
            if (not is_first_found) :
                first_number = int(c)
                is_first_found = True
            else:
                final_number = int(c)
                is_final_number = True
    if is_final_number == False:
        final_number = first_number
    res += first_number*10+final_number
print(res)    