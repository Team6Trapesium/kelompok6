import shapefile		    #import modul shapefile dari pyshp
w=shapefile.Writer()	    #untuk membuat file shapefile baru
w.shapeType				    #mengecek writer diset tipe nya sebagai apa point, line atau polygon, kalo () kosong berarti tidak diset

w.field("kolom1","C")	    #membuat kolom 1 tipe character pada file dbf
w.field("kolom2","C")	    #membuat kolom 2 tipe character pada file dbf

w.record("ngek","satu")	    #isi dari baris pertama dan kolom 1=ngek, 2=satu
w.record("ngok","dua")	    #isi dari baris kedua dan kolom 1=ngok, 2=dua

w.point(1,1)			    #mengisi file shp dengan point atau titik, dimana x=1 dan y=1 untuk row 1
w.point(2,2)			    #mengisi file shp dengan point atau titik, dimana x=2 dan y=2 untuk row 1

w.save("soal1")			    #untuk melakukan save dengan nama soal1