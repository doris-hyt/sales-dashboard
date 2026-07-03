import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from analysis import top5_industry_region_method,top5_cities_method,top5_industry_method,top5_city_industry_method
from data import import_csv 
from matplotlib import font_manager
# import os

font_path = "font/NotoSansCJKtc-Regular.otf"
# print(font_path)
# print(os.path.exists(font_path))
font_manager.fontManager.addfont(font_path)

plt.rcParams["font.family"] = font_manager.FontProperties(fname=font_path).get_name()
# plt.rcParams["font.family"]=["Microsoft JhengHei"] #
data_csv=pd.read_csv("./Business_Sales.csv",encoding="utf-8",header=2) #讀取csv資料
# st.title("產業結構分析")

data_column_final=import_csv(data_csv)
data_column_region=data_column_final[data_column_final["地區別"]!="總計"] #地區別欄位資料非為總計的列資料


page = st.sidebar.radio(
    "產業縣市結構分析功能",
    [
        "縣市產業別排名",
        "產業各縣市排名",
        "產業別銷售額排名",
        "縣市銷售額排名"
    ]
)

# city = st.sidebar.selectbox(
#     "選擇縣市(顯示縣市產業別排名版面)",
#     data_column_region["地區別"].unique()
# )

# industry = st.sidebar.selectbox(
#     "選擇產業(顯示於產業各縣市排名版面)",
#     data_column_final.drop(columns=["總計","地區別"]).columns
# )

# tab1, tab2, tab3, tab4 = st.tabs(["縣市產業別排名","產業各縣市排名" , "各產業別銷售額排名", "各縣市銷售額排名"])


#某縣市產業結構(圓餅圖)
# with tab1:
if page=="縣市產業別排名":
    city = st.sidebar.selectbox(
      "選擇縣市(顯示縣市產業別排名版面)",
      data_column_region["地區別"].unique()
    )
    #算出前5名產業別比重
    st.title(f"{city}前五大產業結構Top5")
    with st.spinner("正在繪製圖形..."):
      df_top5=top5_industry_region_method(data_column_final,city)
      labels=df_top5.index
      values=df_top5.values
      percent=values/values.sum()*100
      #建立圖例說明格式
      labels_percent=[
        f"{name}({p:.1f}%)"
        for name,p in zip(labels,percent)
      ]
      fig,ax=plt.subplots(figsize=(10,8))
      wedges, texts,=ax.pie(
        values,
        labels=None,
        startangle=90,
      )
      ax.legend(
        wedges,
        labels_percent,
        title="產業",
        loc="center left",
        bbox_to_anchor=(1,0.5)
      )
      ax.set_title("2026年3月",y=0.98)
      ax.axis("equal")
      plt.subplots_adjust(right=0.65,top=0.90)
      st.pyplot(fig)

#哪個縣市經濟規模最大--水平長條圖
# with tab2:
elif  page=="產業各縣市排名":
  industry = st.sidebar.selectbox(
    "選擇產業(顯示於產業各縣市排名版面)",
    data_column_final.drop(columns=["總計","地區別"]).columns
  )
  st.title(f"{industry}Top5縣市")
  with st.spinner("正在繪製圖形..."):
    fig,ax=plt.subplots(figsize=(8,8))
    df_top5_city=top5_city_industry_method(data_column_region,industry)
    bars=ax.bar(df_top5_city["地區別"],df_top5_city[industry])
    ax.bar_label(bars, fmt="%.0f", padding=3)
    ax.set_title("2026年3月(單位：新臺幣百萬元)") #圖表名稱
    ax.set_xlabel("地區別") #圖表x軸名稱
    ax.set_ylabel("營業額") #圖表y軸名稱
    plt.tight_layout()
    st.pyplot(fig)
  
#各產業總營業額排名--top5長條圖
# with tab3:
elif page=="產業別銷售額排名":
  st.title("Top5產業別總銷售額排名")
  with st.spinner("正在繪製圖形..."):
    fig,ax=plt.subplots(figsize=(8,8))
    bars=plt.barh(top5_industry_method(data_column_final).index.tolist(),top5_industry_method(data_column_final).values.tolist())
    ax.bar_label(bars, fmt="%.0f", padding=3)
    #y軸為前五名索引(產業別)，x軸為數值(營業額)  
    ax.invert_yaxis()
    ax.set_title("2026年3月(單位：新臺幣百萬元)") #圖表名稱
    ax.set_xlabel("總銷售額") #圖表x軸名稱
    ax.set_ylabel("產業別") #圖表y軸名稱
    plt.tight_layout()
    st.pyplot(fig)

#哪個縣市在哪個產業特別強
# with tab4:
elif page=="縣市銷售額排名":
  st.title("Top5縣市總銷售額排名")
  with st.spinner("正在繪製圖形..."):
  #挑選總計欄位的資料進行排序，並取出前五名資料
    fig,ax=plt.subplots(figsize=(8,8))
    bars=ax.barh(top5_cities_method(data_column_region)["地區別"],top5_cities_method(data_column_region)["總計"])
    ax.bar_label(bars, fmt="%.0f", padding=3)
    #y軸為前五名(地區別欄位資料)，x軸為數值(總計欄位資料)，barh為水平長條圖
    ax.invert_yaxis()
    ax.set_title("2026年3月(單位：新臺幣百萬元)") #圖表名稱
    ax.set_xlabel("總銷售額") #圖表x軸名稱
    ax.set_ylabel("地區別") #圖表y軸名稱
    plt.tight_layout()
    st.pyplot(fig)
    
