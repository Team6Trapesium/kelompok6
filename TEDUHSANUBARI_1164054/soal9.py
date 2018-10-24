import shapefile        #Modul shapefile yang di ambil dari pyshp
w=shapefile.Writer()    #Membuat shpfile baru
w.shapeType             #Mengecek point, line atau polygon, jika () berarti tidak

w.field("kolom1","C")   #Membuat baris 1 dengan tipe character file dbf.
w.field("kolom2","C")   #Membuat baris 2 dengan tipe character file dbf.

w.record("ngek","satu") #Isi dari kolom 1 dan baris 1
w.record("crot","dua")  #Isi dari kolom 2 dan baris 2
 
w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE)  #membuat bentuk vektor sesuai dengan titik sumbu x dan y yang telah di tentukan kemudian di sambungkan dengan garis tepi.
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE)  #membuat bentuk vektor sesuai dengan titik sumbu x dan y yang telah di tentukan kemudian di sambungkan dengan garis tepi.

w.save("soal9") #Melakukan save dengan nama soal9