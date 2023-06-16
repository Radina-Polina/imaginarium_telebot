def test(time):
    lst=[]
    for i in time:
        lst.append(i)
    if lst[0].isdigit==True and lst[1].isdigit==True and lst[2]==":" and lst[3].isdigit==True and lst[4].isdigit==True and lst[5]==":" and lst[6].isdigit==True and lst[7].isdigit==True and len(lst)==8:
        return True

if test("11:11:11")==True:
    print("сасать")