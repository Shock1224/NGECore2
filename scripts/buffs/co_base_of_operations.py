import sys

def setup(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'expertise_innate_protection_all', 1000)
	core.skillModService.addSkillMod(actor, 'expertise_critical_niche_all', 5)	
	return
	
def removeBuff(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'expertise_innate_protection_all', 1000)
	core.skillModService.deductSkillMod(actor, 'expertise_critical_niche_all', 5)	
	return
	