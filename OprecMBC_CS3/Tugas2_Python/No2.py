total_belanja = int(input("Masukan total belanja anda\t : "))
member = str(input("Apakah anda termasuk member (yes/no) : "))

if(total_belanja>=500000 and total_belanja<=1000000):
    if(member=="yes" or member=="Yes" or member=="YES"):
        print("Selamat anda mendapatkan diskon 7%")
    else:
        print("Selamat anda mendapatkan diskon 2%")

elif(total_belanja>1000000):
    if(member=="yes" or member=="Yes" or member=="YES"):
        print("Selamat anda mendapatkan diskon 8%")
    else:
        print("Selamat anda mendapatkan diskon 3%")

else:
    if(member=="yes" or member=="Yes" or member=="YES"):
        print("Selamat anda mendapatkan diskon 5%")
    else:
        print("Maaf anda tidak mendapatkan diskon apapun")
        print("Nice Try!!!")