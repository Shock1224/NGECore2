import sys
from services.housing import HouseTemplate
from engine.resources.scene import Point3D

def setup(core):
	houseTemplate = HouseTemplate("object/tangible/deed/player_house_deed/shared_corellia_house_medium_deed.iff", "object/building/player/shared_player_house_corellia_medium_style_01.iff", 2)
	
<<<<<<< HEAD
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(1, 2, 3))
	houseTemplate.addPlaceablePlanet("corellia")
=======
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(float(5.3),float(2.26),float(7.7)))
>>>>>>> upstream/master
	houseTemplate.addPlaceablePlanet("talus")
	houseTemplate.setDefaultItemLimit(200)
	core.housingService.addHousingTemplate(houseTemplate)
	return