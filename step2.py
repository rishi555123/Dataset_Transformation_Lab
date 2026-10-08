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
l=[]

#Part D

for i in range(30):
    if game[i]<study[i]:
        if study[i]<chat[i]:
            if chat[i]<video[i]:
                l.append("video")
            else:
                l.append("chat")
        else:
            if study[i]<video[i]:
                l.append("video")
            else:
                l.append("study")
    else:
        if game[i]<chat[i]:
            if chat[i]<video[i]:
                l.append("video")
            else:
                l.append("chat")
        else:
            if game[i]<video[i]:
                l.append("video")
            else:
                l.append("game")
df['Winner']=l
print(df['Winner'])


game_share=(game/tot)*100
study_share=(study/tot)*100
chat_share=(chat/tot)*100
video_share=(video/tot)*100
print("Game Share")
print(game_share)
print("Video Share")
print(video_share)
print("Chat Share")
print(chat_share)
print("Video Share")
print(video_share)