import shapefile                                    #import modul shapefile dari pyshp
w=shapefile.Writer()                                #untuk membuat file shapefile baru
w.shapeType                                         #mengecek writer diset tipe nya sebagai apa point, line atau polygon, kalo () kosong berarti tidak diset

w.field("kolom1","C")                               #membuat kolom 1 tipe character pada file dbf
w.field("kolom2","C")                               #membuat kolom 2 tipe character pada file dbf

w.record("ngek","satu")                             #isi dari baris pertama. kolom 1 yaitu ngek dan kolom 2 yaitu satu

w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])     #mengisi file shp dengan garis, tetapi garis nya sudah ditentukan pada koordinat tertentu

w.save("soal5")                                     #untuk melakukan save file shp dengan nama soal5