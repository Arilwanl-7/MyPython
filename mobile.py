#def OpenFile():
    #myFile = open('PhoneNumbers.txt')
    #MobileNumberList=myFile.readlines()
    #MobileNumberList=[line.strip() for line in MobileNumberList]
    #PhoneNumbers=[]
    #for i in MobileNumberList:
     #   PhoneNumbers.append(i[:5])

def MTN(X):
    MTN_Prefix = ['0703','0706','0803','0806','0810','0813','0814','0816','0903','0906','0913','0916','07025','07026','0704']
    New_NumberList = []
    for i in MTN_Prefix:
        for j in X:
            if i in j:
                New_NumberList.append(j)
    print("MTN: ",len(New_NumberList))

def Airtel(X):
    Airtel_Prefix = ['0701','0708','0802','0808','0812','0901','0902','0904','0907','0912']
    New_NumberList = []
    for i in Airtel_Prefix:
        for j in X:
            if i in j:
                New_NumberList.append(j)
    print("Airtel: ",len(New_NumberList))

def Globacom(X):
    Globacom_Prefix = ['0705','0805','0807','0811','0815','0905','0915']
    New_NumberList = []
    for i in Globacom_Prefix:
        for j in X:
            if i in j:
                New_NumberList.append(j)
    print("Globacom: ",len(New_NumberList))

def NineMobile(X):
    _9mobile_Prefix = ['0809','0817','0818','0909','0908']
    New_NumberList = []
    for i in _9mobile_Prefix:
        for j in X:
            if i in j:
                New_NumberList.append(j)
    print("9Mobile: ",len(New_NumberList))

def MTEL(X):
    MTEL_Prefix = ['0804']
    New_NumberList = []
    for i in MTEL_Prefix:
        for j in X:
            if i in j:
                New_NumberList.append(j)
    print("MTEL: ",len(New_NumberList))