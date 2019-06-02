import sys

#input
#以下read()を使うと、pythonスクリプトが標準入力から値を渡された場合にそれを取得できる。
#標準入力から渡されていない場合は、input()と同様、キーボードからの入力を待ち受ける状態になる。
#ただinput()と異なり、ctrl + d されるまでは入力状態になる。
inp = sys.stdin.read()
sys.stdout.write("input result:" + str(inp) )

#if write bynally file, use below.
#sys.stdout.buffer.write(b'abc') 