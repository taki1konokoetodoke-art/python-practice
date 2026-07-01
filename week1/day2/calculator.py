num1 = float(input("数値1を入力してください: "))
num2 = float(input("数値2を入力してください: "))

op = input("演算子を入力してください (+, -, *, /): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("エラー: 0で割ることはできません。")
        raise SystemExit
    else:
        result = num1 / num2
else:
    print("エラー: 無効な演算子です。")
    raise SystemExit

print(f"結果: {result}")