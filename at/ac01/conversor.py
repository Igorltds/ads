#python
def converte(simb):
    roman_dict = {'I': 1, "V": 5 ,'X':10 ,'L':50 ,'C':100 ,'D':50 ,'M':1000}
    f_num = 0
    try:
        for x in range(len(simb)-1,-1,-1):
            x_num = roman_dict[simb[x]]
            if 3*x_num < f_num: f_num = f_num-x_num
            else: f_num = f_num+x_num
        return f_num

    except: 
        if type(simb) == str:   return "input str invalid" 
        else:   return "input type error"

