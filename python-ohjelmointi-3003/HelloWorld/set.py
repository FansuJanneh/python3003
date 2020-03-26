units = {"tank", "plane", "ship", "dog"}
print(units)

# Add lisää yhden arvon settiin
units.add("zeppelin")
print(units)

# Update lisää taulukollisen alkioita settiin
units.update(["helicopter", "juri"])
print(units)

# discard poistaa alkion setistä, heittämättä virhettä
units.discard("dog")
units.discard("dog")
print(units)

# remove poistaa alkion setistä. Jos poistettavaa arvoa ei ole, heitetään KeyError virhe
units.remove("tank")
#units.remove("tank")
print(units)
