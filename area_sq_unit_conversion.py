# This program converts square units.
m = input("Enter you measurement : ")
m = float(m)

cur_unit = input("Enter you Current Unit (km,me,cm,mm) : ")
tar_unit = input("Enter you Target Unit  (km,me,cm,mm) : ")

print(cur_unit)

# tar_unit = input("Enter target unit: ")

km_mm = 10 ** 12
me_mm = 10 ** 6
cm_mm = 10 ** 2

if cur_unit == 'km':
    print(km_mm)
    mmc = m * km_mm
elif cur_unit == 'me':
    print(me_mm)
    mmc = m * me_mm
elif cur_unit == 'cm':
    print(cm_mm)
    mmc = m * cm_mm
elif cur_unit == 'mm':
    print(cm_mm)
    mmc = m
else:
    print("Oppps... your current unit input is wrong")
print(f"The MM Conversion {mmc}")

if tar_unit == 'km':
    output = mmc / km_mm
elif tar_unit == 'me':
    output = mmc / me_mm
elif tar_unit == 'cm':
    output = mmc / cm_mm
elif tar_unit == 'mm':
    output = mmc
else:
    print("Oppps... your Target unit input is wrong")
print(f"The Result is  {output}")













