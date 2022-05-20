import mobile
def ServiceProvider():
    myFile = open('PhoneNumbers.txt')
    MobileNumberList=myFile.readlines()
    MobileNumberList=[line.strip() for line in MobileNumberList]
    PhoneNumbers=[]
    for i in MobileNumberList:
        PhoneNumbers.append(i[:5])
    print('Service Provider Summary Report')
    print()
    mobile.MTN(PhoneNumbers)
    mobile.Airtel(PhoneNumbers)
    mobile.Globacom(PhoneNumbers)
    mobile.NineMobile(PhoneNumbers)
    mobile.MTEL(PhoneNumbers)
    print()


ServiceProvider()

