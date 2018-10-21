import shapefile                           #import modul shapefile dari pyshp
w=shapefile.Writer(shapefile.POINTM)       #untuk membuat file shapefile baru dengan konstanta
w.shapeType                                #mengecek writer diset tipe nya sebagai apa point, line atau polygon

w.field("kolom1","C")                      #membuat kolom 1 tipe character pada file dbf
w.field("kolom2","C")                      #membuat kolom 2 tipe character pada file dbf

w.record("ngek","satu")                    #isi dari baris pertama. kolom 1 yaitu ngek dan kolom 2 yaitu satu
w.record("ngok","dua")                     #isi dari baris kedua. kolom 1 yaitu ngok dan kolom 2 yaitu dua

w.point(1,1)                               #mengisi file shp dengan point atau titik, dimana x=1 dan y=1 untuk row 1
w.point(2,2)                               #mengisi file shp dengan point atau titik, dimana x=2 dan y=2 untuk row 2

w.save("soal4")                            #untuk melakukan save file shp dengan nama soal4