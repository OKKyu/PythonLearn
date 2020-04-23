#! python3
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

#値の退避
f = open("./inputsam.txt", "r")
input_line = f.readlines()
N, S, T = input_line[0].split(' ')
N = int(N)
S = int(S)
T = int(T)
ab = []
for i in range(1,N+1):
    ai,bi = input_line[i].split(' ')
    ab.append([int(ai),int(bi)])
    
#組み合わせ判定
isSuccessPlanNum = 0
#日数*ダイエットするしない　の数だけパターンを試す
for ptnNum in range(0, 2**N):
    #右１桁目から順に１日目、２日目、・・・
    # '1'：ダイエットする '0'：ダイエットしない
    ptnStr = str(bin(ptnNum)).replace('0b','').rjust(N,'0')

    #パターンを試す
    #計算後の体重
    calcedWeight = S
    for j in range(0,N):
        if ptnStr[(j+1) * -1] == '0':
            #ダイエットしないの場合加算する
            calcedWeight = calcedWeight + int(ab[j][1])
        else:
            #ダイエットするの場合減算する
            calcedWeight = calcedWeight - int(ab[j][0])
        if calcedWeight > T:
            #上限オーバーの場合は失敗なので、当該パターンの計算を中断する
            break
        elif calcedWeight <= T and j == N -1:
            #上限オーバーせず最終日まで計算出来た場合、上手くいった計画数をカウントアップする
            isSuccessPlanNum += 1
    
print(isSuccessPlanNum)
