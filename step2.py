import numpy as np
import pandas as pd


# part A
df=pd.read_csv("day02_usage.csv")
game=df['Games'].to_numpy()
study=df['Study'].to_numpy()
chat=df['Chat'].to_numpy()
video=df['Video'].to_numpy()
print(len(df))


# Part B
tot=game+study+chat+video
avg=tot.mean()
print(tot.sum())
print(avg)


#Part C
diff=study-game
print(diff)

#Part D
game_share=(game/tot)*100
study_share=(study/tot)*100
chat_share=(chat/tot)*100
video_share=(video/tot)*100
print(game_share)
print(video_share)
print(chat_share)
print(video_share)