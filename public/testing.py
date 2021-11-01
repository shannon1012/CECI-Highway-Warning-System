import requests
import json
import re
import datetime
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/ioi",methods=['GET']) #即時路況
def ioi():
    Num=request.args.get('Num')
    outdata=[]

    r = requests.get(url='https://od.moi.gov.tw/MOI/v1/pbs')
    data= json.loads(r.content)
    index=1
    Noselect=str(Num)
    for i in data:
        regex = re.compile(r'國道(\d+-*\d*)號')
        match = regex.search(i['areaNm'])
        try: #國道路況        
            
            happentimes = i['happendate']+" " + i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00"#時間 
            happentime= datetime.datetime.strptime(happentimes,"%Y-%m-%d %H:%M:%S")
            #print(happentime)
            
            perisutime = datetime.datetime.now()-datetime.timedelta(hours=2) #兩小時內
            #print(perisutime)

            #print(datetime.datetime.now()) #現在時間
            if perisutime<happentime<datetime.datetime.now():
                #print(i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00")#時間 

                roadtype = i['roadtype'] #類型

                num = match.group(1) #國道號碼


                print(num)
    
                match = regex.search(i['comment'])

                comment = i['comment']
                
                if Noselect == "1":                                        
                    if num=="１":
                        outdata.append({"index":index,"num":1,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1
                if Noselect=="3":
                    if num == "３":
                        outdata.append({"index":index,"num":3,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1
                if Noselect=="2":
                    if num == "２":
                        outdata.append({"index":index,"num":2,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1
                if Noselect=="4":                
                    if num == "４":
                        outdata.append({"index":index,"num":4,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1
                if Noselect=="5":
                    if num == "５":
                        outdata.append({"index":index,"num":5,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1
                if Noselect=="6":
                    if num == "６":
                        outdata.append({"index":index,"num":6,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1
                if Noselect=="8":
                    if num == "８":
                        outdata.append({"index":index,"num":8,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1
                if Noselect=="10":
                    if num == "１０":
                        outdata.append({"index":index,"num":10,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                        index+=1

                if Noselect =="":
                    outdata.append({"index":index,"num":num,"happentime":i['happentime'].split(".")[0].split(":")[0]+":"+i['happentime'].split(".")[0].split(":")[1]+":00","roadtype":roadtype,"comment":comment,'longitude':i['y1'],'latitude':i['x1']})
                #outdata.append(out)
                
                
                #print()
        except:
            pass

    return jsonify({"content":outdata})
        


if __name__ == "__main__":
    app.debug = True
    app.run()