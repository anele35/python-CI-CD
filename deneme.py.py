print("Hoşgeldin! Öncelikle sana hitap edebilmek için adını öğrenebilir miyim?")
isim=str(input())

print("Merhaba" + " " + isim + ". Hadi gel hesaplayalım!" )


maas=int(input("Aylık net maaşını rakamlar ile girer misin? Araya nokta koyma:"))
izin=int(input("Bu ay kaç gün izin yaptığını rakamlar ile girer misin?:"))

kalanmaas= float(maas - ((maas / 30) * izin))

sonuc = ("Bu ay kesintiden sonra kalan maaşın:" + " " + str(kalanmaas))
print (sonuc)
print (str(kalanmaas) "TL. Güle güle harca. Şimdilik kapanıyorum, iyi günler")
exit()
