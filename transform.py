import pandas as pd
import os
import csv

def convert_date(text,year):
    nova_data = ""
    list = text.split("-")
    nova_data = list[0] + "-"
    if("Ene" in list[1]):
        nova_data += "01"
    elif("Feb" in list[1]):
        nova_data += "02"
    elif("Mar" in list[1]):
        nova_data += "03"
    elif("Abr" in list[1]):
        nova_data += "04"
    elif("May" in list[1]):
        nova_data += "05"
    elif("Jun" in list[1]):
        nova_data += "06"
    elif("Jul" in list[1]):
        nova_data += "07"
    elif("Ago" in list[1]):
        nova_data += "08"
    elif("Sep" in list[1]):
        nova_data += "09"
    elif("Oct" in list[1]):
        nova_data += "10"
    elif("Nov" in list[1]):
        nova_data += "11"
    elif("Dic" in list[1]):
        nova_data += "12"

    nova_data += "-" +  year
    return nova_data
            



fout = open('database', 'w')
print("pais,estado,cidade,data,tipo,valor",file=fout)#imprimindo header

for path in os.listdir(os.getcwd()+"/Downloads/"):
    if "lock" in path:
        continue
    print(os.getcwd()+"/Downloads/"+path)
    tortilla_prices = pd.read_html(os.getcwd()+"/Downloads/"+path)
    tortilla_prices[0].to_csv("arquivo.csv", index=False, header=False)
    with open("arquivo.csv", 'r') as file:
        pais="mexico"
        reader = csv.reader(file)
        for i,row in enumerate(reader):
            if(i==2):
                year = str(row[0]).replace("Año: ",'')
            if(i==4):
                if("tortillerías" in str(row[0]).lower()):
                    tipo = "tortillerías"
                else:
                    tipo = "autoservicios"
            if(i==5):
                date = row
                for j,data in enumerate(date):
                    if j < 2:
                        continue
                    date[j]=convert_date(data,year)

            if(i>6):
                if "Precio" in row[0]:
                    break
                estado = row[0]
                cidade = row[1]
                for j,value in enumerate(row):
                    if j>=2:
                        print(pais+","+estado+","+cidade+","+date[j]+","+tipo+","+value,file=fout)

fout.close()

