f = open("stock_data.txt","r")

stock_line = {

}
stock_condition = ["最新价","涨跌幅","换手率"]

columns = f.readline().strip().split(",")
print (columns)
for i in f :
    line = i.strip().split(",")
    stock_line[line[2]] = line
while True :
    Query_interface = input("请输入查询接口").strip()
    print(Query_interface)
    print(columns)
    for i in stock_line :
        if Query_interface in i:
            print (stock_line[i])
    if ">" in Query_interface :
        q_name,q_val = Query_interface.split(">")
        q_name = q_name.strip()
        q_val = float(q_val)
        print ("打印信息", q_name,q_val)
        print (columns.index(q_name))
        if q_name in stock_condition :
            q_name_index = columns.index(q_name)
            for s_name ,s_val in   stock_line.items():
                if float(s_val[q_name_index].strip("%")) > q_val:
                    print (stock_line[s_name])
    elif "< "  in Query_interface :
        q_name, q_val = Query_interface.split("<")
        q_name = q_name.strip()
        q_val = float(q_val)
        print("打印信息", q_name, q_val)
        print(columns.index(q_name))
        if q_name in stock_condition:
            q_name_index = columns.index(q_name)
            for s_name, s_val in stock_line.items():
                if float(s_val[q_name_index].strip("%")) > q_val:
                    print(stock_line[s_name])
    else:
        print ("格式错误请请重新输入")





