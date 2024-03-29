print("Hoşgeldin! Öncelikle sana hitap edebilmek için adını öğrenebilir miyim?")
isim=str(input())

print("Merhaba" + " " + isim + ". Demek bu ay izin yaptık:) Hadi gel hesaplayalım!" )


maas=int(input("Aylık net maaşını rakamlar ile girer misin?:"))
izin=int(input("Bu ay kaç gün izin yaptığını rakamlar ile girer misin?:"))

kalanmaas= float(maas - ((maas / 30) * izin))

sonuc = ("Bu ay kesintiden sonra kalan maaşın:" + " " + str(kalanmaas))
print (sonuc)
print ("Güle güle harcayın. Şimdilik kapanıyorum, iyi günler")
exit()