print("What do you want to do?");
print("Want to transform currency from THB to US Dollar? Press 'a' ");
print("Want to transform currency from THB to Yen? Press 'b' ");
print("Want to transform currency from THB to Yuan? Press 'c'");
trans = input("What do you want to do? >>> ");
if trans == "a":
    baht = input("Insert your money(THB) : ");
    bahtCurrency = float(baht);
    """1 BAHT = 0.0031 US DOLLAR"""
    usdollarCurrency = bahtCurrency * 0.031;
    print(str(usdollarCurrency) + " US Dollar");
elif trans == "b":
    baht = input("Insert your money(THB) : ");
    bahtCurrency = float(baht);
    """1 BAHT = 3.45 YEN"""
    yenCurrency = bahtCurrency * 3.45;
    print(str(yenCurrency) + " Yen");
elif trans == "c":
     baht = input("Insert your money(THB) : ");
     bahtCurrency = float(baht);
     """1 BAHT = 0.2 YUAN"""
     yuanCurrency = bahtCurrency * 0.2;
     print(str(yuanCurrency) + " Yuan");
else:
    print("We don't know what you want to do, Bye.");