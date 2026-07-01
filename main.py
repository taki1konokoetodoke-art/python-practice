num1 = input("数値1を入力してください")
num2 = input("数値2を入力してください")

op = input("演算子を入力してください (+, -, *, /): ")

num1 = float(num1)
num2 = float(num2)

if op == "+":
    print = num1 + num2
elif op == "-":
    print = num1 - num2
elif op == "*":
    print = num1 * num2
elif op == "/":
    if num2 != 0:
        print = num1 / num2
    else:
        print("エラー: 0で割ることはできません。")
else:
    print("エラー: 無効な演算子です。")