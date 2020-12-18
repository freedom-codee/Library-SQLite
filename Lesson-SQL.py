import sqlite3
con  = sqlite3.connect("database.db")
cursor = con.cursor()
 # fetchone ile de verileri tek tek alır ('taha','emhm','1254')
# fetchmany ile de istediğimiz kadar veri alıyrouz. fetchmany(10)
def create_databse():
    cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler(Username VARCHAR,Password VARCHAR)")
    con.commit()
    con.close()

def insert_values():
    a = input("username:")
    b = input("Password")

    cursor.execute("INSERT INTO bilgiler VALUES(?,?)",(a,b))
    con.commit()
    con.close()
    print("Veriler başarılı bir şekilde gönderildi.")


def select_values():
    cursor.execute("SELECT * FROM  bilgiler")
    rows = cursor.fetchall()
    for i in rows:
        print("K_adi:{}-- Şifre: {}".format(i[0],i[1]))

def delete_values():
    query = input("login username for delete:")
    cursor.execute("DELETE FROM bilgiler WHERE Username = (?) ",(query,))# girilen değer usernameni db bulup usernamin olduğu tüm satırı siler
    con.commit()
    con.close()
    print("Deleting completed.")

def alter_col():
    cursor.execute("ALTER TABLE bilgiler ADD yeni_col INT") # sonra columns ekleme işlemi yapıldı.

def distinct():
    cursor.execute("SELECT DISTINCT * FROM  bilgiler") # aynı olan verilerden sadece bir tane getirdi. DISTINCT İLE
    rows = cursor.fetchall()
    for i in rows:
        print("K_adi:{}-- Şifre: {}".format(i[0], i[1]))

def order_by():
    cursor.execute("SELECT DISTINCT * FROM bilgiler ORDER BY Username ASC") # asc ile A-Z şekline kullanıcı adlarını sıraladı ve distinct ile aynılardan bir tane aldı.
    rows = cursor.fetchall()
    for i in rows:
        print("K_adi:{}-- Şifre: {}".format(i[0], i[1]))

def where_list():
    cursor.execute("SELECT DISTINCT * FROM bilgiler WHERE maas >1000") # maas 100 den büyük olanları sıraladı.
    rows = cursor.fetchall()
    for i in rows:
        print("K_adi:{}-- Şifre: {}".format(i[0], i[1]))
def update():
    cursor.execute("UPDATE data SET Password = 'asdfg' WHERE Username = 'taha'")# usernamei taha olanın parolasını değiştir dedik.
    con.commit() # update zamanında commit yapılmazsa değşiklik yapılmayacaktır.
    cursor.execute("SELECT * FROM  bilgiler")
    rows = cursor.fetchall()
    for i in rows:
        print("K_adi:{}-- Şifre: {}".format(i[0], i[1]))
def count():
    cursor.execute("SELECT COUNT(*) FROM bilgiler")
    rows = cursor.fetchall()
    print(rows)

def list_table():
    cursor.execute("SELECT name FROM sqlite_master WHERE type= 'table'") # table adını bize göstterdi.
    rows = cursor.fetchall()
    print(rows)


def rename_table_name():
    cursor.execute("ALTER TABLE bilgiler RENAME TO data")

def primary():
    cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler(k_id INTEGER PRIMARY KEY AUTOINCREMENT,Username VARCHAR,Password VARCHAR)")
    # yukarıdai integer int sayı olmasını ve primary ile birincil anahtar ve auto ile de otomotik artmasını sağladık.
    # bu sayade k_id özgü keyler olacakç

def limit():
    cursor.execute("SELECT * FROM data WHERE Username= 'taha' AND Password = '123*şlok' LIMIT 1")
    # yukarıda data tablosundan Username'i taha olan ve şifresi 123*şlok olan kullanıcılardan LIMIT ile 1 tane çekmiş olduk
    rows = cursor.fetchall()
    print(rows)

def like():
    cursor.execute("SELECT * FROM data WHERE Username LIKE '%a' ORDER BY Username ASC") # isterek LIMIT ile burada da sınırlama yapabiliriz.
    # %a% içerisinde a olan  a% başında a olan %a sonunda a olan _aa% 2. ve 3. karakteri a olan verileri çeker.
    # ORDER BY ve diğer fonksiyonlarda burada kullanılabilir.
    # yukarıda daata tablosundan username'i a ile başlayan tüm verileri sıraladı.
    rows = cursor.fetchall()
    print(rows)
like()

                    #KÜMELEME FUNCS
# SELECT SUM(KOLON İSMİ) FROM TABLO ADİ
#
# AVG MAX MIN*