import shapefile        #Modul shapefile yang di ambil dari pyshp
w=shapefile.Writer()    #Membuat shpfile baru
w.shapeType             #Mengecek point, line atau polygon, jika () berarti tidak

w.field("kolom1","C")   #Membuat baris 1 dengan tipe character file dbf.
w.field("kolom2","C")   #Membuat baris 2 dengan tipe character file dbf.

w.record("ngek","satu") #Isi dari kolom 1 dan baris 1 = ngek, 2 = 1
w.record("ngok","dua")  #Isi dari kolom 2 dan baris 1 = ngek, 2 = 2

w.point(1,1)            #Isi file shp dengan point atau titik, dimana x=1 dan y=1 untuk row 1
w.point(2,2)            #Isi file shp dengan point atau titik, dimana x=2 dan y=2 untuk row 1

w.save("soal1")         #Melakukan save dengan nama soal1