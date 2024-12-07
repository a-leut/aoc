DIGITS = [str(x) for x in range(10)]

def get_muls(s, care_about_conditions=False):
    # modes: nuttin, start_mul, first_num, second_num
    total = 0
    mode = 'nuttin'
    enabled_mode = 'do'
    n1 = ''
    n2 = ''
    for i in range(len(s)):
        if s[i] == ')':
            if i > 3 and s[i-3:i] == 'do(':
                enabled_mode = 'do'
            elif i > 6 and s[i-6:i] == 'don\'t(':
                enabled_mode = 'dont'
        if s[i] == '(' and i > 3 and s[i-3:i] == 'mul':
            mode = 'start_num'
        elif mode == 'start_num':
            if s[i] in DIGITS:
                n1 += s[i]
                if len(n1) > 3:
                    mode = 'nuttin'
                    n1 = ''
            elif s[i] == ',' and len(n1) > 0:
                mode = 'second_num'
            else:
                n1 = ''
                mode = 'nuttin'
        elif mode == 'second_num':
            if s[i] in DIGITS:
                n2 += s[i]
                if len(n2) > 3:
                    mode = 'nuttin'
                    n1 = ''
                    n2 = ''
            elif s[i] == ')' and len(n2) > 0:
                # we're just gonna be lazy here
                if not care_about_conditions:
                    total += int(n1) * int(n2)
                elif enabled_mode == 'do':
                    total += int(n1) * int(n2)
                mode = 'nuttin'
                n1 = ''
                n2 = ''
            else:
                mode = 'nuttin'
                n1 = ''
                n2 = ''
    return total

with open('input.txt', 'r') as f:
    mem = f.read()
    
print(get_muls(mem))
print(get_muls(mem, care_about_conditions=True))
