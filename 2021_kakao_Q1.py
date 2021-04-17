def solution(new_id):
    import re
    new_id_1 = new_id.lower()
    re_2=re.compile("[.]|[a-z0-9-_]")
    new_id_2 = "".join(re_2.findall(new_id_1))
    re_3 = re.compile("[.]+")
    new_id_3 = re_3.sub('.',new_id_2)
    if new_id_3[0] == '.' :
        new_id_4 = new_id_3[1:]
    else : new_id_4 = new_id_3
    if new_id_4 == "" :
        new_id_5 = "a"
    else : new_id_5 = new_id_4
    if len(new_id_5) >= 16 : 
        new_id_6 = new_id_5[:15]
    else : new_id_6 = new_id_5
    if new_id_6[-1] == "." : 
            new_id_6 = new_id_6[:-1]
    while len(new_id_6) <=2 : 
        new_id_6 = new_id_6 + new_id_6[-1]
    new_id_7 = new_id_6   
    answer = new_id_7
    return answer