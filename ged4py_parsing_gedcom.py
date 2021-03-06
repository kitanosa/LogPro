import sys
from ged4py.parser import GedcomReader
path = "/home/kitanosa/labs/logpro/roal.ged"
parser = GedcomReader(path)
spisok = []

def where_is_family(parent_id):#  ищу где наш husband - ребенок 
    # найти famc а потом сделать переменную для fam и внутри нее сохранить всех детей
    with GedcomReader(path, encoding="utf-8") as parser:
        for i, line in enumerate(parser.records0("INDI")):
            index_family_of_parent = line.sub_tag("FAMC")
            if line.xref_id == parent_id:
                if index_family_of_parent:# line.xref_id это считываемое со строки id при INDI, index_family_of_parent означает что в строке присутствует FAMC
                    index_family_of_parent = index_family_of_parent.xref_id
                    if index_family_of_parent not in spisok: # удаляем одинаковые id семей. Веди husb могли попасться браться
                        spisok.append(index_family_of_parent)
                        return search_brot_sist_of_parent(index_family_of_parent)
# сначала сделаем ir с инди и запишем в переменную id indi.

def search_brot_sist_of_parent(family_id):# делаем массив их этих детей
	list_brot_sist__of_parent = []
	with GedcomReader(path, encoding="utf-8") as parser:
		for i, indi in enumerate(parser.records0("FAM")):
			children = indi.sub_tags("CHIL")
			if indi.xref_id == family_id:
				for child in children: # тут мы сделали первый массив для
					print(f"{child}")
					if children.split()[2] != husband.xref_id: 
						list_brot_sist__of_parent.append(child.xref_id)
					else: return
				return down(list_brot_sist__of_parent)


def down(list_brot_sist__of_parent):# соединяем все. Нужно еще сделать проверку чтобы list_brot_sist__of_parent не был нулевым ОНА РАБОТАЕТ
	global list_double_brothers
	list_double_brothers = []
	with GedcomReader(path, encoding="utf-8") as parser:
		for parent in list_brot_sist__of_parent:
			for i, indi in enumerate(parser.records0("FAM")):
				Husb, Wife = indi.sub_tag("HUSB"), indi.sub_tag("WIFE") 
				children = indi.sub_tags("CHIL")
				if Husb:
					if parent == Husb.xref_id:
						for child in children:
							if child.sub_tag_value("SEX") == 'M':
								list_double_brothers.append(child.name.format())

				if Wife:
					if parent == Wife.xref_id:
						for child in children:
							if child.sub_tag_value("SEX") == 'M':
								list_double_brothers.append(child.name.format())
		
with GedcomReader(path, encoding="utf-8") as parser:
    for i, indi in enumerate(parser.records0("INDI")):
        father = indi.father
        if father: 
            print(f"father({father.name.format()}, {indi.name.format()})")

with GedcomReader(path, encoding="utf-8") as parser:
    for i, indi in enumerate(parser.records0("INDI")):
        mother = indi.mother
        if mother: 
            print(f"mother({mother.name.format()}, {indi.name.format()})")



with GedcomReader(path, encoding="utf-8") as parser:
	list_childs = []
	for i, fam in enumerate(parser.records0("FAM")):
		husband, wife = fam.sub_tag("HUSB"), fam.sub_tag("WIFE") 
		children = fam.sub_tags("CHIL")
		if husband:
			father_id = husband.xref_id
			where_is_family(father_id)# где father в качестве ребенка
		if wife: 
			wife_id = wife.xref_id
			where_is_family(wife_id)
		for child in children:
			if child.sub_tag_value("SEX") == 'M':
				list_childs.append(child.name.format())
		for i in list_childs:
			for j in list_double_brothers:
				if i!=j:
					print(f"двоюродные братья:({i}, {j})")
		list_childs = []
