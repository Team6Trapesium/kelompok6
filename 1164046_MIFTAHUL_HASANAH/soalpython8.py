import shapefile							#kita akan  meng import modul shapefile dari pyshp
w=shapefile.Writer()						#untuk membuat file shapefile baru
w.shapeType									#mengecek writer diset tipe nya sebagai point apa, line atau polygon, kalo () kosong berarti tidak diset
w.field("kolom1","C")						#kita membuat baris 1  dengan tipe character pada file dbf
w.field("kolom2","C")						#kita membuat baris 2  dengan tipe character pada file dbf
w.record("ngek","satu")						#isi dari baris pertama dan kolom 1=ngek, satu
w.poly(parts=[[[1,3],[5,3],[1,2],[5,2],		#digunakan untuk menghubungkan titik titik ,sehingga akan menjadi sebuah garis.
[1,3]]],shapeType=shapefile.POLYLINE)
w.save("soal8")								#untuk melakukan simpan dengan nama soal8