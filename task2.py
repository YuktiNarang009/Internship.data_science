import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
reading and cleaning the file
'''

df=pd.read_csv("netflix_titles.csv")

# print(df.info())
# print(df.describe())

# print(df.head())
# print(df.isnull().sum())
# print(df.duplicated(subset="show_id").sum())

# print(df["director"].unique())
# print(df["cast"].unique())
# print(df["country"].unique())


# df["director"]=df["director"].fillna("Unknown")
# df["cast"]=df["cast"].fillna("Unknown")
# df["country"]=df["country"].fillna("Unknown")
# df["rating"]=df["rating"].fillna("Unknown")
# df["date_added"]=df["date_added"].fillna("Unknown")

# print(df.isnull().sum())


'''
Data Visualisation
'''

# print(df["release_year"].max())

'''
bar graph comparing number of movies and tv shows
'''

# plt.figure(figsize=(6,4))
# type_count=df["type"].value_counts()
# # print(type_count)
# plt.bar(type_count.index,type_count.values,color=["blue","orange"],label=["Movies","TV Shows"])
# plt.title("Movies VS TV Shows")
# plt.xlabel("Type")
# plt.ylabel("Count")
# plt.legend()
# plt.savefig("netflix_movie_vs_tvshow.jpeg",dpi=300)
# plt.show()


'''
pie chart for different rating
'''

# rating_count=df["rating"].value_counts()
# plt.pie(rating_count.values,labels=rating_count.index,autopct="%1.1f%%")
# plt.title("Percentage of content Rating")
# plt.tight_layout()
# plt.savefig("percentage_rating.jpeg",dpi=300)
# plt.show()


'''
creating histogram for movie duration
'''
# df_new=df[df["type"]=="Movie"].copy()
# df_new["new_duration"]=df_new["duration"].str.replace(" min"," ").astype(int)

# plt.hist(df_new["new_duration"],bins=15,color="grey",edgecolor="black")
# plt.title("Movie duration")
# plt.xlabel("duration")
# plt.ylabel("number of movies")
# plt.savefig("moviw_duration_.png",dpi=300)

plt.show()

'''
scatter plot showing release year vs number of shows
'''

# df_year=df[df["type"]=="TV Show"].copy()
# release_year_count=df_year["release_year"].value_counts()
# print(release_year_count)
# plt.scatter(release_year_count.index,release_year_count.values,marker="^",color="blue")
# plt.grid(True)
# plt.title("Shows every year")
# plt.xlabel("years")
# plt.ylabel("numbesr of show")
# plt.savefig("shows_every_year.png")
# plt.show()


'''
bar graph for 10 maximum netflix shows countries
'''
# country_count=df["country"].value_counts().head(10)
# #print(country_count)

# plt.barh(country_count.index,country_count.values)
# plt.title("Countries with maximum published movies")
# plt.xlabel("Country")
# plt.ylabel("Number of movies")
# plt.savefig("countries.png")
# plt.show()


'''
subplot-movie vs tv shows by year
'''
# df_newdata=df.groupby(["release_year","type"]).size().unstack().fillna(0)
# # print(df_newdata.isnull().sum())
# # print(df_newdata.index)
# fig,ax=plt.subplots(1,2,figsize=(6,4))
# ax[0].plot(df_newdata.index,df_newdata["Movie"],color="green")
# ax[0].set_title("Movies released per year")
# ax[0].set_xlabel("Year")
# ax[0].set_ylabel("Movies")
# ax[1].plot(df_newdata.index,df_newdata["TV Show"],color="purple")
# ax[1].set_title("TV Shows released per year")
# ax[1].set_xlabel("Year")
# ax[1].set_ylabel("TV Shows")
# plt.savefig("Movies_vs_tvshows_per_year.jpeg")
# plt.show()







