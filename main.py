import folium
import json

starting_location = [65, 100]
map = folium.Map(
    location=starting_location,
    zoom_start=4,
    tiles='Stamen Toner'
)

state_boundaries_group = folium.FeatureGroup(name="Государственная граница РФ")
admin_L2_json = json.load(open("admin_level_2.geojson", "r", encoding="utf8"))
state_boundaries_group.add_child(folium.GeoJson(data=admin_L2_json))

federal_district_boundaries_group = folium.FeatureGroup(
    name="Границы федеральных округов")
admin_L3_json = json.load(open("admin_level_3.geojson", "r", encoding="utf8"))
federal_district_boundaries_group.add_child(folium.GeoJson(data=admin_L3_json))

federal_subject_boundaries_group = folium.FeatureGroup(
    name="Границы субъектов федерации")
admin_L4_json = json.load(open("admin_level_4.geojson", "r", encoding="utf8"))
federal_subject_boundaries_group.add_child(folium.GeoJson(data=admin_L4_json))

municipal_associations_boundaries_group = folium.FeatureGroup(
    name="Границы объединений муниципальных районов")
admin_L5_json = json.load(open("admin_level_5.geojson", "r", encoding="utf8"))
municipal_associations_boundaries_group.add_child(folium.GeoJson(data=admin_L5_json))

municipal_districts_boundaries_group = folium.FeatureGroup(
    name="Границы муниципальных районов субъектов федерации")
admin_L6_json = json.load(open("admin_level_6.geojson", "r", encoding="utf8"))
municipal_districts_boundaries_group.add_child(folium.GeoJson(data=admin_L6_json))

map.add_child(state_boundaries_group)
map.add_child(federal_district_boundaries_group)
map.add_child(federal_subject_boundaries_group)
map.add_child(municipal_associations_boundaries_group)
map.add_child(municipal_districts_boundaries_group)
map.add_child(folium.LayerControl())
map.save("russia_map.html")
