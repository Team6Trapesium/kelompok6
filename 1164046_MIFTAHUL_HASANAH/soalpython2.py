import shapefile					#kita akan  meng import modul shapefile dari pyshp
w=shapefile.Writer(shapeType=1)		#untuk membuat file shapefile baru
w.shapeType							#mengecek writer diset tipe nya sebagai point apa, line atau polygon, kalo () kosong berarti tidak diset
w.field("kolom1","C")				#kita membuat baris 1  dengan tipe character pada file dbf
w.field("kolom2","C")				#kita membuat baris 2 dengan tipe character pada file dbf
w.record("ngek","satu")				#isi dari baris pertama dan kolom 1=ngek, satu
w.record("ngok","dua")				#isi dari baris kedua dan kolom 2=ngok, dua
w.point(1,1)						#kita akan mengisi file shp dengan point atau titik, dimana x=1 dan y=1 untuk row 1
w.point(2,2)						#mengisi file shp dengan point atau titik, dimana x=2 dan y=2 untuk row 1
w.save("soal2")						#untuk melakukan simpan dengan nama soal1

		    			