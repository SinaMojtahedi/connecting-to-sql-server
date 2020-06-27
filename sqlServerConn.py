import pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from GPUYayinAkisSatirLog")
    for row in cursor:
        print(f'column = {column}')
    print()

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'insert into GPUYayinAkisSatirLog(DosyaAdi,Saniye,Tarih,TanimaOrani,ProgramAdi) values(?,?,?,?,?);',
         ('0542_18_09.frd', 2531, 0.9945, 'Ari Maya')
    )
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'update GPUYayinAkisSatirLog set Saniye = ?, Tarih = ?, TanimaOrani = ?, ProgramAdi = ? where DosyaAdi = ?;',
        ('0542_18_11.frd', 2468, 0.88, 'Aslan')
    )
    conn.commit()
    read(conn)

def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        'delete from GPUYayinAkisSatirLog where DosyaAdi > 5'
    )
    conn.commit()
    read(conn)    

conn = pyodbc.connect(
    "Driver={SQL Server Native Driver};"
    "Server=x.x.x.x;"
    "Database=X;"
    "UID=X;"
    "PWD=X;"
    "Trusted_Connection=no;"
    
)


read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()