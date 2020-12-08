import folium

starting_location = [65, 100]
map = folium.Map(
    location=starting_location,
    zoom_start=4,
    tiles='Stamen Toner'
)

map.save("russia_map.html")
