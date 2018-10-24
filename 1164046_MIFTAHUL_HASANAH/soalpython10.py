import shapefile    
w=shapefile.Writer()
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("mif","satu")
w.record("maf","dua")
w.record("muf","tiga")
w.record("mita","empat")
w.poly(parts=[[[2000,200],[2200,400],[2600,400],[2800,200],[2000,200]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[180,200],[220,300],[280,300],[320,200],[180,200]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[340,350],[380,450],[440,450],[480,350],[340,350]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[500,500],[540,600],[600,600],[640,500],[500,500]]],shapeType=shapefile.POLYLINE)
w.save("soal10")