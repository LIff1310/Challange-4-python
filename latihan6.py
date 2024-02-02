print("LATIHAN 6")
x = float(input("x = "))
y = float(input("y = "))

if x > 0 and y > 0:
    print("kuadran I")

elif x < 0 and y > 0:
    print("kuadran II")

elif x < 0 and y < 0:
    print("kuadran III")

elif x > 0 and y < 0:
    print("kuadran IV")

elif x == 0 and y == 0:
    print("berada di titik pusat")

else:
    print("koordinat tidak diketahui")