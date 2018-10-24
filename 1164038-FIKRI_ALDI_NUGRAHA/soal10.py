import shapefile                                                                              #import modul shapefile dari pyshp
w=shapefile.Writer()                                                                          #untuk membuat file shapefile baru
w.shapeType                                                                                   #mengecek writer diset tipe nya sebagai apa point, line atau polygon, kalo () kosong berarti tidak diset

w.field("nama_bangun","C")                                                                    #membuat kolom 1 tipe character pada file dbf
w.field("keterangan","C")                                                                     #membuat kolom 2 tipe character pada file dbf
w.field("posisi","C")                                                                         #membuat kolom 3 tipe character pada file dbf

w.record("kaka","trapesium1","kanan")                                                         #isi dari baris pertama. kolom 1 yaitu kaka, kolom 2 yaitu trapesium1, dan kolom 3 yaitu kanan
w.record("kiki","trapesium2","atas")                                                          #isi dari baris pertama. kolom 1 yaitu kiki, kolom 2 yaitu trapesium2, dan kolom 3 yaitu atas
w.record("kuku","trapesium3","kiri")                                                          #isi dari baris pertama. kolom 1 yaitu kuku, kolom 2 yaitu trapesium3, dan kolom 3 yaitu kiri

w.poly(parts=[[[1,1],[3,4], [7,4],[9,1],[1,1]]],shapeType=shapefile.POLYLINE)                 #mengisi file shp dengan garis, tetapi garis nya sudah ditentukan pada koordinat tertentu 
                                                                                              #serta shape type di set sebagai polyline, tapi karena titik awal dan akhir sama
                                                                                              #maka bentuk yang dibuat membentuk polygon bangun datar trapesium dengan posisi di kiri

w.poly(parts=[[[10,1],[12,4], [16,4],[18,1],[10,1]]],shapeType=shapefile.POLYLINE)            #mengisi file shp dengan garis, tetapi garis nya sudah ditentukan pada koordinat tertentu 
                                                                                              #serta shape type di set sebagai polyline, tapi karena titik awal dan akhir sama
                                                                                              #maka bentuk yang dibuat membentuk polygon bangun datar trapesium dengan posisi di atas

w.poly(parts=[[[5,6],[7,9], [11,9],[13,6],[5,6]]],shapeType=shapefile.POLYLINE)               #mengisi file shp dengan garis, tetapi garis nya sudah ditentukan pada koordinat tertentu 
                                                                                              #serta shape type di set sebagai polyline, tapi karena titik awal dan akhir sama
                                                                                              #maka bentuk yang dibuat membentuk polygon bangun datar trapesium dengan posisi di kanan

w.save("soal10")                                                                              #untuk melakukan save file shp dengan nama soal10