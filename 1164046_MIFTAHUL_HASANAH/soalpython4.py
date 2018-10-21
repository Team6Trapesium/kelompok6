import shapefile 						#kita akan  meng import modul shapefile dari pyshp
w=shapefile.Writer(shapefile.POINTM) 	#untuk membuat file shapefile baru
w.shapeType 							#mengecek writer diset tipe nya sebagai point apa, line atau polygon, kalo () kosong berarti tidak diset
w.field("kolom1","C") 					#kita membuat baris 1  dengan tipe character pada file dbf
w.field("kolom2","C") 					#kita membuat baris 1  dengan tipe character pada file dbf
w.record("ngek","satu") 				#isi dari baris kedua dan kolom 2=ngek, dua
w.record("ngok","dua") 					#isi dari baris kedua dan kolom 2=ngek, dua
w.point(1,1) 							#kita akan mengisi file shp dengan point atau titik, dimana x=1 dan y=1 untuk row 1
w.point(2,2) 							#kita akan mengisi file shp dengan point atau titik, dimana x=1 dan y=1 untuk row 1
w.save("soal4") 						#untuk melakukan simpan dengan nama soal4