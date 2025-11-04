import random

#じゃんけんの手
list=["グー","チョキ","パー"]

#プレイヤーの手
player = input("あなた：")

#リストから手を出す
com = random.choice(list)
print("相手:{}".format(com))

#プレイヤーと相手の手で勝敗を決める
#勝敗もプリント
if player == com:
    print("あいこです。")
elif player == "グー":
    if com == "チョキ":
        print("あなたの勝ち")
    elif com == "パー":
        print("あなたの負け")
elif player == "チョキ":
    if com == "グー":
        print("あなたの負け")
    elif com == "パー":
        print("あなたの勝ち")
elif player == "パー":
    if com == "グー":
        print("あなたの勝ち")
    elif com== "チョキ":
        print("あなたの負け")
