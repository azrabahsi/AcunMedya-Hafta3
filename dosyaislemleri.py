dosya = open("dosya.txt", "w", encoding="utf-8") 
metin = input("Bir metin giriniz: ")  
dosya.write(metin + "\n")  
dosya.close()  

dosya = open("dosya.txt", "r", encoding="utf-8") 
dosya_icerik = dosya.read()  
print("\nDosyanın içeriği:")
print(dosya_icerik)  
dosya.close()  


dosya = open("satir.txt", "a", encoding="utf-8") 
print("\n5 farklı satır giriniz:")

for i in range(5): 
    satir = input(f"{i+1}. satır: ")  
    dosya.write(satir + "\n") 

dosya.close()  

dosya = open("satir.txt", "r", encoding="utf-8") 
print("\nDosyadaki satırlar:")

for satir in dosya:  
    print(satir)  

dosya.close()  
