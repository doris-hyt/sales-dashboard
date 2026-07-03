import pandas as pd

#某縣市產業結構(圓餅圖、長條圖)
def top5_industry_region_method(df,city):
  top5_industry_region=df[df["地區別"]==city] #挑選地區別為選擇項目的列資料
  top5_industry_region=top5_industry_region.drop(columns=["總計","地區別"]).iloc[0]
  #將該列資料轉為Series型式
  top5_industry_region=top5_industry_region.sort_values(ascending=False).head(5)
  #排序資料並取出前5筆資料
  return top5_industry_region

#哪個縣市經濟規模最大--水平長條圖
def top5_cities_method(df):
  top5_cities=df.sort_values(by="總計",ascending=False).head(5)
  #挑選總計欄位的資料進行排序，並取出前五名資料
  return top5_cities
  
    
#各產業總營業額排名--top10長條圖
def top5_industry_method(df):
  #先將總計列資料拿掉總計那一格的資料，由剩下的各產業別資料進行比較
  data_csv_total=df[df["地區別"]=="總計"] #地區別欄位資料為總計的列資料
  top5_industry=(data_csv_total
                .drop(columns=["總計"])
                .iloc[0]
                )
                #要加iloc[0]變成Series型式，如果不使用資料型式為DataFrame，在後面sort_values需要指定欄位排序，所以先轉換
  top5_industry=top5_industry.apply(pd.to_numeric, errors="coerce")#將文字資料轉為數值
  top5_industry=top5_industry.sort_values(ascending=False).head(5) #取前五筆資料
  return top5_industry


#哪個縣市在哪個產業特別強
def top5_city_industry_method(df,industry):
    top5_city_industry=df.sort_values(by=industry,ascending=False).head(5)
    return top5_city_industry

