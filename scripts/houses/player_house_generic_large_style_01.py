import sys
from services.housing import HouseTemplate
from engine.resources.scene import Point3D

def setup(core):
	houseTemplate = HouseTemplate("object/tangible/deed/player_house_deed/shared_generic_house_large_style_02_deed.iff", "object/building/player/shared_player_house_generic_large_style_02.iff", 2)
	
<<<<<<< HEAD
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(1, 2, 3))
=======
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(float(6), float(3), float(13.4)))
>>>>>>> upstream/master
	houseTemplate.addPlaceablePlanet("tatooine")
	houseTemplate.addPlaceablePlanet("corellia")
	houseTemplate.addPlaceablePlanet("naboo")
	houseTemplate.addPlaceablePlanet("talus")
	houseTemplate.addPlaceablePlanet("rori")
	houseTemplate.addPlaceablePlanet("dantooine")
	houseTemplate.addPlaceablePlanet("lok")
	houseTemplate.setDefaultItemLimit(500)
	
	core.housingService.addHousingTemplate(houseTemplate)
	return