a=int(input("Enter age for check categories of persion-- "))
if 0<a<=10:
    print("kid:")
elif 10<a<=20:
    print("Teen")
elif 20<a<=40:
    print("young")
elif 40<a<=60:
    print("Experinced")
elif 60<a<=100:
    print("senior citizen")
else:
    print("persion is no more")