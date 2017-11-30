baht = input("Insert your money(THB) : ");
bahtCurrency = float(baht);
usdollarCurrency = bahtCurrency * 0.031;
yenCurrency = bahtCurrency * 3.45;
yuanCurrency = bahtCurrency * 0.2;
print(str(usdollarCurrency) + " US Dollar");
print(str(yenCurrency) + " Yen");
print(str(yuanCurrency) + " Yuan");