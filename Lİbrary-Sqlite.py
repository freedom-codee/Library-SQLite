import sqlite3 as sql
print("""
         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
        |                                   |
        |    STEM LİBRARY PROGRAM           |
        |                        2020       |
        |    Lang: python                   |
        |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|       
                  
                  
Seçenekler
-----------
1.Kitap Ekle
2.Kitap Sil
3.Kitap Ara
4.Veritabanı Ayarları(Yönetici)
""")
print('-'*30)
db = sql.connect("library1.db")
con = db.cursor()
# con.execute("CREATE TABLE IF NOT EXISTS kutuphane(kitap_adi TEXT,kitap_yazari TEXT,sayfa_sayisi INT,publish_date DATETIME,publish_home TEXT,kitap_turu TEXT,ISBN_no INT,kitap_ozeti TEXT)")
# if not exists dediğimiz için yeni bir sütn eklemeyiz çünkü daha önce tablo kurulu ondan muvelit alter ile yeni bir sütun ekledik.
# con.execute("ALTER TABLE kutuphane RENAME COLUMN Kitap Adi TO Kitap_Adi")
# con.execute("ALTER TABLE kutuphane ADD COLUMN point INT")


while True:
    a = input("Lütfen bir işlem seçin:")
    print("Çıkış için q  basın")
    if a == '1':
        print("Üst Menü için 0 tuslayın")
        print('---KİTAP EKLEME--')
        kitap_adi = input("Kitap Adı:")
        kitap_yazari = input("Kitap Yazarı:")
        publish_date = input("Yayınlanma Tarihi:")
        kitap_sayfasi = int(input("Kitap Sayfa Sayısı:"))
        kitap_turu = input("Kitap Türü:")
        kitap_barkod_no = input("Kitap ISN No(1254780TH069):")
        kitap_ozeti = input("Kitap Özeti:")
        print('*' * 50)
        print("""Girdiğiniz Bilgiler:\n
                Kitap Adı: {}\t\t\tKitap Yazarı: {}\n
                Kitap Sayfa Sayısı: {}\t\tKitap Türü: {}\n
                Yayınlanma Tarihi: {}\n
                Kitap Barkod No: {}\t\tKitap Özeti: {}\n\n""".format(kitap_adi,kitap_yazari,kitap_sayfasi,kitap_turu,publish_date,kitap_barkod_no,kitap_ozeti))
        save = input("Kitabı Kaydet(E) Hayır(H):")
        if save == 'H' or save == 'h':
            continue
        elif save == 'e' or save == 'E':
            con.execute("INSERT INTO kutuphane(kitap_adi,kitap_yazari,yayin_tar,kitap_sayfasi,kitap_turu,kitap_barkod_no,kitap_ozeti) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(kitap_adi,kitap_yazari,publish_date,kitap_sayfasi,kitap_turu,kitap_barkod_no,kitap_ozeti))
            db.commit()
            print('Kayıt işlemi başarılı')
        else:pass
    elif a == '2':
        print("""
            1.Kitap adı ve yazarı ile 
            2.Kitap Türü ile
        """)
        select = input("islem Sec:")
        if select == '1':
            query = input("Kitap Adı Gir:")
            author = input('Kitap Yazarını Gir:')
            con.execute("DELETE FROM kutuphane WHERE Kitap Adi= (?) and Yazar= (?)",(query,author))
            db.commit()
            print("{} adlı tüm kitaplar silindi".format(query))
        elif select == '2':
            query = input("Kitap Yazarını Gir: ")
            limit = input("Silme Limiti Gir\nVarsayılan olarak hepsini siler:")
            con.execute("DELETE FROM kutuphane WHERE TUR = '{}' LIMIT {}".format(query, limit))
            print("{} adlı yazarın kitapları silindi".format(query))
        else:pass
        #sayfa_sayisi 500 den küçük olanları sil
        # ve ya 2000 den sonra yayınlanan kitapları sil
        #yazara atil olan tüm kitapları sil
    elif a == '3':
        print("""
        Kitap Ara
        ----------
        
        1.Kitap adı ile 
        2.Kitap yazarı ile 
        3.Kitap türü ile 
        4.Genel Bilgiler
        """)
        S =input("İşlem Seç:")
        if S == '1':
            s1 = input("Kitap Adı Gir:")
            book = con.execute("SELECT * FROM kutuphane WHERE Kitap_adi = '{}'".format(s1)).fetchall()
            print("{} adındaki kitaplar -{}".format(s1,len(book)))
            for j in book:
                print('-' * 25)
                print("Id: {}\nAd: {}\nYazar: {}\nSayfa_Sayisi: {}\nTür: {}\nISBN: {}\nÖzet: {}\nYayin_tarihi: {}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7]))
                print('-'*25)
        elif S == '2':
            s2 = input("Kitap Yazarı Gir:")
            book2=con.execute("SELECT * FROM kutuphane WHERE Yazar = '{}'".format(s2)).fetchall()
            print("\n{} adlı yazarın kitapları ({})".format(s2, len(book2)))
            for j in book2:
                print('-' * 25)
                print("Id: {}\nAd: {}\nYazar: {}\nSayfa_Sayisi: {}\nTür: {}\nISBN: {}\nÖzet: {}\nYayin_tarihi: {}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7]))
        elif S == '3':
            s3 = input("Kitap Türü Gir:")
            book =con.execute("SELECT * FROM kutuphane WHERE TUR = '{}'".format(s3)).fetchall()
            print("\n{} türündeki kitaplar ({})".format(s3,len(book)))
            for j in book:
                print('-' * 25)
                print("Id: {}\nAd: {}\nYazar: {}\nSayfa_Sayisi: {}\nTür: {}\nISBN: {}\nÖzet: {}\n"
                      "Yayin_tarihi: {}".format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7]))
        elif S == '4':
            print("KÜTÜPHANE HAKKINDA GENEL İSTATİSTİKLER")
            Author = con.execute("SELECT DISTINCT trim(Yazar) FROM kutuphane").fetchall()
            total_book = con.execute("SELECT Kitap_adi FROM kutuphane").fetchall()
            turler = con.execute("SELECT DISTINCT TUR,COUNT(TUR) FROM kutuphane GROUP BY TUR").fetchall()
            print("**Toplam Yazarlar**: {}\n"
                  "**Toplam Kitaplar**: {}\n".format(len(Author),len(total_book)))
            for j in turler:
                print("{} ({})".format(j[0],j[1]))
            best_page = con.execute("SELECT SUM(sayfa_sayisi) FROM kutuphane").fetchone()
            print('**Kitaplarımız toplam {} sayfadır.**'.format(best_page[0]))
            print("Kitap başına düşen ortalama sayfa sayisi = {}".format(round(int(best_page[0])/int(len(Author)),2)))
            pmax = con.execute(
                "SELECT kitap_adi,sayfa_sayisi FROM kutuphane WHERE sayfa_sayisi = (SELECT MAX(sayfa_sayisi) FROM kutuphane)").fetchall()
            pmin = con.execute(
                "SELECT kitap_adi,sayfa_sayisi FROM kutuphane WHERE sayfa_sayisi = (SELECT MIN(sayfa_sayisi) FROM kutuphane)").fetchall()
            print("**Sayfa sayısı en fazla olan**: {}\n"
                  "**Sayfa sayısı en az olan**: {}".format(str(pmax).strip('([ ])'),str(pmin).strip('([ ])')))
            lim_aut = con.execute("SELECT * FROM kutuphane WHERE Yazar = 'Cahit Zarifoğlu' LIMIT 2").fetchall()
            print('\n')
            print("**Cahit Zarifoğlu 2 adet kitabı**\n"
                  "-------------------------------\n")
            for j1 in lim_aut:
                print("Ad: {}\tYazar: {}\tYayın Evi: {}\tTür: {}\tYayin Tarihi: {}\tSayfa: {}\tISBN: {}\n"
                      .format(j1[1],j1[2],j1[3],j1[4],j1[5],j1[6],j1[7]))
            # basim_ma = con.execute(
            #     "SELECT kitap_adi, Yazar,Yayin_tarihi FROM kutuphane WHERE Yayin_tarihi = (SELECT MAX(Yayin_tarihi) FROM kutuphane)").fetchall()
            basim_ = con.execute(
                "SELECT * FROM kutuphane WHERE Yayin_tarihi ORDER BY substr (Yayin_tarihi,5,9) || substr(Yayin_tarihi,3,5) || substr(Yayin_tarihi,0,2) DESC").fetchone()
            print("**Basım Tarihi yeni  olan kitabımız**\n"
                  "------------------------------------\n"
                  "Ad: {}\tYazar: {}\tYayın evi: {}\tTür: {}\tYayın Tarihi: {}\tSayfa: {}".format(basim_[1],basim_[2],
                                                                                                  basim_[3],basim_[4],
                                                                                                  basim_[5],basim_[6]))

            basim_1 = con.execute(
                "SELECT * FROM kutuphane WHERE Yayin_tarihi ORDER BY substr (Yayin_tarihi,5,9) || substr(Yayin_tarihi,3,5) || substr(Yayin_tarihi,0,2) ASC").fetchone()
            print("\n**Basım Tarihi eski olan kitabımız**\n"
                  "-----------------------------------\n"
                  "Ad: {}\tYazar: {}\tYayın evi: {}\tTür: {}\tYayın Tarihi: {}\tSayfa: {}".format( basim_1[1], basim_1[2],
                                                                                                  basim_1[3], basim_1[4],
                                                                                                  basim_1[5], basim_1[6]))

            # update = con.execute("UPDATE kutuphane SET Yazar = 'Anonim' WHERE Yazar = 'ANONİM'")
            # db.commit()
            yazarlar = con.execute("SELECT DISTINCT trim(Yazar),COUNT(Yazar) FROM kutuphane GROUP BY Yazar LIMIT 70").fetchall()
            # fetchmany(70) LIMIT İLE AYNI İŞELVİ GÖRMEKTEDİR.
            # fetchone ile de tek tek verileri alabiliriz.
            # upper(Yazar) şeklinde de kullanılabilir.
            # trim(Yazarlar) strip ile aynı görevi görmektedir.
            print("Yazar-Kitap Sayisi\n")
            counter = 0
            while counter<=70:
                print(yazarlar[counter])
                counter += 1


            adın_basi = con.execute("SELECT DISTINCT Yazar FROM kutuphane WHERE Yazar LIKE 'And%'").fetchall()
            # And ile küçük büyük ayrımı gözetmeksizin adının başında and olan büyün verileri getirir
            # dıstınct ile de aynı yazarlardan sadece bir tane getirir
            # aynı mantıkla sonunda ortasında şeklinde de veriler getirelebilir.
            print("Adının Başında And Olan Yazarlar:\n",adın_basi)





    elif a == 'Q' or a == 'q':
        quit()
    else:
        print("Geçerli bir işlem girin:")
        continue



 #----------------------- TOPLU GÖNDERME ---------------------------

# import pandas as pd
#
# df = pd.read_excel(r'C:\Users\tahay\Desktop\lib.xlsx')
# df.drop('Unnamed: 0',axis=1,inplace=True)
# df.columns = ['Kitap Adi','Yazar','Yayinevi','Tur']
#
# df.index[0]
# df.drop(df.index[0],axis=0,inplace= True)
#
# df.dropna(inplace = True)
#
# df['Kitap Adi']= pd.Series(df['Kitap Adi']).str.replace("'","",regex=True)
#
# con = sql.connect(r'C:\Users\tahay\Desktop\ML-MATH\library.db')
#
# counter = 0
# while counter<951: #951 is len dataframe
#     a =df['Kitap Adi'].iloc[counter] b =df['Yazar'].iloc[counter] ek olarak bu şekilde birkaç kolon seçip gönderebiliriz
#     counter += 1
#     con.execute("INSERT INTO kutuphane('kitap_adi') VALUES('{}')".format(a))
#     con.commit()

#---------------------JUPYTER NOTEBOOK-----------------------
# import pandas as pd
# import numpy as np
# import sqlite3 as sql
#
# df = pd.read_excel(r'C:\Users\tahay\Desktop\lib.xlsx')
# df.drop('Unnamed: 0',axis=1,inplace=True)
# df.columns = ['Kitap_adi','Yazar','Yayinevi','Tur']
#
# df.index[0]
# df.drop(df.index[0],axis=0,inplace= True)
#
# df.dropna(inplace = True)
#
# df['Kitap_adi']= pd.Series(df['Kitap_adi']).str.replace("'","",regex=True)
#
# sayfa_sayisi= np.random.randint(50,800,950)
# page_num = pd.DataFrame(sayfa_sayisi)
# page_num.columns= ['sayfa_sayisi']
#
# counter= 1
# liste = []
# while counter<951:
#     month = np.random.randint(1,12)
#     day = np.random.randint(1,31)
#     year = np.random.randint(1890,2019)
#     date = '{}.{}.{}'.format(day,month,year)
#     liste.append(date)
#     counter += 1
#
# df_date = pd.DataFrame(liste)
# df_date.columns = ['Yayin_tarihi']
# df_date.index= [np.arange(1,951)]
#
# yeni = df.merge(df_date,on=df.index,how='inner')
# yeni.drop('key_0',axis=1,inplace=True)
#
# lib  = yeni.merge(page_num,on=yeni.index,how='inner')
# lib.drop('key_0',axis=1,inplace= True)
#
# ısbn = np.random.randint(9000000000000,10000000000000,950,dtype='int64')
# ısbn = pd.DataFrame(ısbn)
# ısbn.columns = ['ISBN']
#
# lib1 = lib.merge(ısbn,on=lib.index,how = 'inner')
# lib1.drop('key_0',axis=1,inplace=True)
# lib1
#
# con = sql.connect(r'C:\Users\tahay\Desktop\ML-MATH\library1.db')
#
# lib1.to_sql('kutuphane',con=con)