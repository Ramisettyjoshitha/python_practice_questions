salary=int(input("enter your salary :"))
if salary <= 25000:
    print("no tax for your salary")
elif salary <= 50000:
    tax=salary*0.1
    final_salary= salary-tax
    print("the tax amount deducted is:",tax)
    print("the final salary after tax deduction of 10 %:",final_salary)
else:
    tax=salary*0.2
    final_salary=salary-tax
    print("the tax amount deducted is:",tax)
    print("the final salary afer tax deduction of 20%:",final_salary)
