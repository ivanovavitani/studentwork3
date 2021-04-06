import osr
import ogr

# Заполнение слоя с точками атрибутами
def points_creator(input_layer, X, Y, district, address, pupils, floors, teachers):
    feature = ogr.Feature(input_layer.GetLayerDefn())
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(Y,X)
    feature.SetGeometry(point)
    feature.SetField("district", district)
    feature.SetField("address", address)
    feature.SetField("pupils", pupils)
    feature.SetField("floors", floors)
    feature.SetField("teachers", teachers)
    input_layer.CreateFeature(feature)
    feature.Destroy()

# Создание слоя shp с точками
def points_shp_creator():
    dir = 'C:\PythonWorks3'
    driver = ogr.GetDriverByName("ESRI Shapefile")
    ds = driver.CreateDataSource(dir + '\my_points.shp')
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    layer = ds.CreateLayer('Schools', srs, ogr.wkbPoint)
    field_name = ogr.FieldDefn("district", ogr.OFTString)
    field_name.SetWidth(50)
    layer.CreateField(field_name)
    field_name = ogr.FieldDefn("address", ogr.OFTString)
    field_name.SetWidth(100)
    layer.CreateField(field_name)
    layer.CreateField(ogr.FieldDefn("pupils", ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn("floors", ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn("teachers", ogr.OFTInteger))
    points_creator(layer, 60.021175, 30.379414, "Kalininskij", "ul. Akademika Konstantinova, 10, korp. 2", 1400, 2, 60)
    points_creator(layer, 59.955766, 30.472748, "Krasnogvardejskij", "Irinovskij prosp., 23, korp. 2", 800, 4, 54)
    points_creator(layer, 60.001847, 30.286718, "Primorskij", "Bogatyrskij prosp., 7, korp. 4", 1214, 2, 75)
    points_creator(layer, 59.971899, 30.311548, "Petrogradskij", "ul. Professora Popova, 25", 1140, 4, 61)
    points_creator(layer, 59.940308, 30.341651, "Central'nyj", "nab. reki Fontanki, 22", 915, 3, 58)
    points_creator(layer, 59.929912, 30.467991, "Nevskij", "ul. Latyshskih Strelkov, 9, korp. 3", 1024, 3, 60)
    points_creator(layer, 59.848917, 30.326369, "Moskovskij", "Altajskaya ul., 15", 956, 4, 53)
    points_creator(layer, 59.877138, 30.266479, "Kirovskij", "ul. Marshala Govorova, 9", 1243, 4, 64)
    points_creator(layer, 59.943811, 30.281927, "Vasileostrovskij", "Srednij prosp. Vasil'evskogo ostrova, 20", 876, 3, 52)
    points_creator(layer, 60.039321, 30.327426, "Vyborgskij", "prosp. Engel'sa, 115, korp. 2", 1342, 2, 64)

points_shp_creator()