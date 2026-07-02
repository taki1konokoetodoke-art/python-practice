from datetime import date

birth_year = int(input("誕生年を入力してください: "))
birth_month = int(input("誕生月を入力してください: "))
birth_day = int(input("誕生日を入力してください: "))

today = date.today()
age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

print(f"今日は {today.year}年{today.month}月{today.day}日 です。")
print(f"あなたは {age} 歳です。")


