import pandas as pd

def import_csv(data_csv):
    data_csv=data_csv.drop(index=range(2)) #排除前3列資料
    data_csv=data_csv.reset_index(drop=True)  #重新編排索引
    data_csv = data_csv.iloc[:22] # 保留前面21筆資料
    data_csv.columns=(
      data_csv.columns
      .str.replace("　","",regex=False)
      .str.replace(" ","",regex=False)
      .str.replace("\n","",regex=False)
      .str.strip()
      )#取除欄位名稱空格、\n
    data_csv=data_csv.drop(columns=["Region","地區別.1","Region.1"]) #去除特定欄位資料
    data_csv=data_csv.map(lambda x:x.strip() if isinstance(x,str) else x)
    #將文字資料(地區別欄位)的全形、半形空格消除
    data_column_region=data_csv["地區別"]
    data_column_region=data_column_region.map(lambda x:x.replace("　","") if isinstance(x,str) else x)
    data_column_region=data_column_region.map(lambda x:x.replace(" ","") if isinstance(x,str) else x)
    #將資料的文字轉為數值型態
    data_column_total = data_csv.loc[:,data_csv.columns != "地區別"]
    data_column_total=data_column_total.replace(",","",regex=True)
    data_column_total=data_column_total.apply(pd.to_numeric,errors="coerce")
    #將文字資料及數值資料欄位合併
    data_column_final=pd.concat([data_column_total,data_column_region],axis=1)
    return data_column_final












  
    






