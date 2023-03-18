
# a = list(map(str,input().split(",")))
# id =[]
# ward=[]
# for i in a:
#     if(i.isdigit()):
#         id.append(i)
#     else:
#         ward.append(i)
# for i in ward:
#     if(i  ):
med = {
    "P":"Pediatrics",
    "O":"Orthopedics",
    "E":"ENT"
}
test =list(map(str,input().split(",")))
P = test.count('P')
O = test.count('O')
E = test.count('E')
if P>E and P>O:
    print(med['P'])
elif E>O:
    print(med['E'])
else:
    print(med['O'])