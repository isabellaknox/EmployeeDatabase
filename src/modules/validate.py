def is_valid_badge_id(id):
	return True if id[0] == 'a' and len(id)==7 and id[1:].isnumeric() else False

def is_valid_name(name):
	return True if name.isalpha() else False
	
def is_valid_all(vals):
	return True if is_valid_name(vals[0]) and is_valid_name(vals[1]) and is_valid_badge_id(vals[2]) else False
