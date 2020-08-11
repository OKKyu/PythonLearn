#! python3
# -*- coding:utf-8 -*-

try:
    while True:  # なんらかの重い処理 (for だったり while だったり。。。)
        print("GYAAAAAA!!")# ここに、Ctrl-C で止めたい処理を書く
except KeyboardInterrupt:
    # Ctrl-C を捕まえた！
    print('interrupted!')
    # なにか特別な後片付けが必要ならここに書く
    sys.exit(0)