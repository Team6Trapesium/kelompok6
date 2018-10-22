import shapefile        #Modul shapefile yang di ambil dari pyshp
w=shapefile.Writer()    #Membuat shpfile baru
w.shapeType             #Mengecek point, line atau polygon, jika () berarti tidak

w.field("kolom1","C")   #Membuat baris 1 dengan tipe character file dbf.
w.field("kolom2","C")   #Membuat baris 2 dengan tipe character file dbf.

w.record("ngek","satu") #Isi dari kolom 1 dan baris 1 = ngek, 2 = 1

w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat garis sesuai titik koordinat yang ditentukan

w.save("soal5")          #Melakukan save dengan nama soal5