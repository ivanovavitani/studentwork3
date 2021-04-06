import os
os.environ['PROJ_LIB'] = 'C:\anaconda\pkgs\proj-6.2.1-h9f7ef89_0\Library\share\proj'
os.environ['GDAL_DATA'] = 'C:\anaconda\pkgs\proj-6.2.1-h9f7ef89_0\Library\share'
import osr
import gdal
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

# Заполнение слоя с полигонами атрибутами
def poligons_creator(input_layer, X1, Y1, X2, Y2, X3, Y3, X4, Y4, address, district, fence, hours, school):
    feature = ogr.Feature(input_layer.GetLayerDefn())
    geom = ogr.Geometry(ogr.wkbLinearRing)
    geom.AddPoint(Y1, X1)
    geom.AddPoint(Y2, X2)
    geom.AddPoint(Y3, X3)
    geom.AddPoint(Y4, X4)
    poligon = ogr.Geometry(ogr.wkbPolygon)
    poligon.AddGeometry(geom)
    feature.SetGeometry(poligon)
    feature.SetField("school address", address)
    feature.SetField("district", district)
    feature.SetField("fence height", fence)
    feature.SetField("opening hours", hours)
    feature.SetField("school number", school)
    input_layer.CreateFeature(feature)
    feature.Destroy()

# Создание слоя shp с полигонами
def polygons_shp_creator():
    dir = 'C:\PythonWorks3'
    driver = ogr.GetDriverByName("ESRI Shapefile")
    ds = driver.CreateDataSource(dir + '\my_poligons.shp')
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    layer = ds.CreateLayer('Stadiums', srs, ogr.wkbPolygon)
    field_name = ogr.FieldDefn("address", ogr.OFTString)
    field_name.SetWidth(150)
    layer.CreateField(field_name)
    field_name = ogr.FieldDefn("district", ogr.OFTString)
    field_name.SetWidth(50)
    layer.CreateField(field_name)
    layer.CreateField(ogr.FieldDefn("fence", ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn("hours", ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn("school", ogr.OFTInteger))
    poligons_creator(layer, 59.958335, 30.225663, 59.958242, 30.226302, 59.958881, 30.226662, 59.958970, 30.226019, 'ul. Korablestroitelej, 42k2', 'Vasileostrovskij', 3, 13, 10)
    poligons_creator(layer, 59.998158, 30.214334, 59.998473, 30.214477, 59.998663, 30.213107, 59.998323, 30.212812, "Mebel'naya ul, 21, k3", 'Primorskij', 2, 14, 630)
    poligons_creator(layer, 59.985317, 30.208577, 59.985153, 30.209856, 59.984809, 30.209680, 59.984970, 30.208397, 'Primorskij prospekt, 143k3', 'Primorskij', 3, 24, 601)
    poligons_creator(layer, 59.997974, 30.339839, 59.998224, 30.340004, 59.998389, 30.338775, 59.998153, 30.338638, 'prospekt Parhomenko, 17', 'Vyborgskij', 3, 24, 117)
    poligons_creator(layer, 60.035214, 30.426668, 60.035089, 30.427305, 60.035711, 30.427791, 60.035838, 30.427156, 'prospekt Prosveshcheniya, 106k2', 'Kalininskij', 3, 12, 1175)
    poligons_creator(layer, 59.981227, 30.401205, 59.981375, 30.400586, 59.980781, 30.400031, 59.980629, 30.400646, 'Zamshina ulica, 58k2', 'Kalininskij', 3, 3, 186)
    poligons_creator(layer, 59.958233, 30.488378, 59.958362, 30.488880, 59.957856, 30.489442, 59.957714, 30.488940, 'Otechestvennaya ulica, 5', 'Krasnogvardejskij', 3, 24, 134)
    poligons_creator(layer, 59.939728, 30.474139, 59.940048, 30.473845, 59.939749, 30.472761, 59.939468, 30.473063, "Industrial'nyj prospekt, 10k2", 'Nevskij', 3, 11, 147)
    poligons_creator(layer, 59.860959, 30.343940, 59.860942, 30.343045, 59.860221, 30.343089, 59.860249, 30.344007, 'prospekt Kosmonavtov, 21k4', 'Moskovskij', 2, 12, 525)
    poligons_creator(layer, 59.843159, 30.270188, 59.842694, 30.271181, 59.842444, 30.270734, 59.842919, 30.269730, "ulica Podvodnika Kuz'mina, 52", 'Kirovskij', 3, 12, 539)

points_shp_creator()
polygons_shp_creator()