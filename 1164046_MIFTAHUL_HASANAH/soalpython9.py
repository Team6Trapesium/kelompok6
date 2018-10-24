import shapefile									#kita akan  meng import modul shapefile dari pyshp
w=shapefile.Writer()								#untuk membuat file shapefile baru
w.shapeType											#mengecek writer diset tipe nya sebagai point apa, line atau polygon, kalo () kosong berarti tidak diset
w.field("kolom1","C")								#kita membuat baris 1  dengan tipe character pada file dbf
w.field("kolom2","C")								#kita membuat baris 2  dengan tipe character pada file dbf
w.record("ngek","satu")								#isi dari baris pertama dan kolom 1=ngek, satu
w.record("crot","dua")								#isi dari baris pertama dan kolom 1=crot, dua
w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], 			#digunakan untuk menghubungkan titik titik ,sehingga akan menjadi sebuah garis, yang mana garis garis tersebut terhubungsatu sama lainnya.dan membentuk sebuah bangun karena garis garis nya saling terhubung.
[1,3]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9],			#digunakan untuk menghubungkan titik titik ,sehingga akan menjadi sebuah garis, yang mana garis garis tersebut terhubungsatu sama lainnya.dan membentuk sebuah bangun karena garis garis nya saling terhubung.
[1,6]]],shapeType=shapefile.POLYLINE)
w.save("soal9")										#untuk melakukan simpan dengan nama soal9