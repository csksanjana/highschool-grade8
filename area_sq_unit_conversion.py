measurement = input("Enter you measurement : ")
int(measurement)

cur_unit = input("Enter you Current Unit (km,me,mm) : ")

print(cur_unit)


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#tar_unit = input("Enter target unit: ")

km_mm = 10 ** 12
me_mm = 10 ** 6
cm_mm = 10 ** 2
mmc = 0
print(km_mm)
if cur_unit == 'km':
   mmc = measurement * km_mm
elif cur_unit == 'me':
    mmc = measurement * me_mm
elif cur_unit == 'cm':
    mmc = measurement * cm_mm
else:
    print("Oppps... your current unit input is wrong")
exit(0)
