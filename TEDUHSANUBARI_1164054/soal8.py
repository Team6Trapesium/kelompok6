import shapefile 
w=shapefile.Writer() 
w.shapeType 

w.field("kolom1","C") 
w.field("kolom2","C")

w.record("ngek","satu") 

w.poly(parts=[[[1,3],[5,3],[1,2],[5,2], [1,3]]],shapeType=shapefile.POLYLINE)

w.save("soal8") 