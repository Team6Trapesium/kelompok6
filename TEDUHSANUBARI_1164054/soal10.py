import shapefile        #Modul shapefile yang di ambil dari pyshp
w=shapefile.Writer()    #Membuat shpfile baru
w.shapeType             #Mengecek point, line atau polygon, jika () berarti tidak

w.field("kolom1","C")   #Membuat baris 1 dengan tipe character file dbf.
w.field("kolom2","C")   #Membuat baris 2 dengan tipe character file dbf.

w.record("trapesium","satu")    #Isi dari kolom 1 dan baris 1
w.record("trapesium","dua")     #Isi dari kolom 2 dan baris 2
w.record("trapesium","tiga")    #Isi dari kolom 3 dan baris 3
w.record("trapesium","empat")   #Isi dari kolom 4 dan baris 4
w.record("trapesium","lima")    #Isi dari kolom 5 dan baris 5

w.poly(parts=[[[2,8],[4,12],[8,12],[10,8], [2,8]]],shapeType=shapefile.POLYLINE)            #membuat bentuk vektor sesuai dengan titik sumbu x dan y yang telah di tentukan kemudian di sambungkan dengan garis tepi.
w.poly(parts=[[[-2,-8],[-4,-12],[-8,-12],[-10,-8], [-2,-8]]],shapeType=shapefile.POLYLINE)  #membuat bentuk vektor sesuai dengan titik sumbu x dan y yang telah di tentukan kemudian di sambungkan dengan garis tepi.
w.poly(parts=[[[-2,8],[-4,12],[-8,12],[-10,8], [-2,8]]],shapeType=shapefile.POLYLINE)       #membuat bentuk vektor sesuai dengan titik sumbu x dan y yang telah di tentukan kemudian di sambungkan dengan garis tepi.
w.poly(parts=[[[2,-8],[4,-12],[8,-12],[10,-8], [2,-8]]],shapeType=shapefile.POLYLINE)       #membuat bentuk vektor sesuai dengan titik sumbu x dan y yang telah di tentukan kemudian di sambungkan dengan garis tepi.
w.poly(parts=[[[8,14],[10,18],[14,18],[16,14], [8,14]]],shapeType=shapefile.POLYLINE)       #membuat bentuk vektor sesuai dengan titik sumbu x dan y yang telah di tentukan kemudian di sambungkan dengan garis tepi.

w.save("soal10") #Melakukan save dengan nama soal10