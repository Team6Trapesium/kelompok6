import shapefile                                                            #import modul shapefile dari pyshp
w=shapefile.Writer()                                                        #untuk membuat file shapefile baru
w.shapeType                                                                 #mengecek writer diset tipe nya sebagai apa point, line atau polygon, kalo () kosong berarti tidak diset

w.field("kolom1","C")                                                       #membuat kolom 1 tipe character pada file dbf
w.field("kolom2","C")                                                       #membuat kolom 2 tipe character pada file dbf

w.record("ngek","satu")                                                     #isi dari baris pertama. kolom 1 yaitu ngek dan kolom 2 yaitu satu

w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE)      #mengisi file shp dengan garis, tetapi garis nya sudah ditentukan pada koordinat tertentu 
                                                                            #serta shape type di set sebagai polyline

w.save("soal7")                                                             #untuk melakukan save file shp dengan nama soal7