# Determine if two rectangular objects are overlapping
def point_in_rect(point,rect):
	p_x = point[0]
	p_y = point[1]

	x = rect[0]
	y = rect[1]
	w = rect[2]
	h = rect[3]

	if x + w > p_x > x and y + h > p_y > y:
		return True
	else: return False

def overlap_rect_rect(rect1, rect2):
	x1 = rect1[0]
	y1 = rect1[1]
	w1 = rect1[2]
	h1 = rect1[3]

	x2 = rect2[0]
	y2 = rect2[1]
	w2 = rect2[2]
	h2 = rect2[3]

	# find the coordinates of the corners
	p11 = [x1, y1]
	p12 = [x1+w1, y1]
	p13 = [x1, y1+h1]
	p14 = [x1+w1, y1+h1]

	p21 = [x2, y2]
	p22 = [x2+w2, y2]
	p23 = [x2, y2+h2]
	p24 = [x2+w2, y2+h2]

	one_in_two = point_in_rect(p11,rect2) or point_in_rect(p12,rect2) or point_in_rect(p13,rect2) or point_in_rect(p14,rect2)
	two_in_one = point_in_rect(p21,rect1) or point_in_rect(p22,rect1) or point_in_rect(p23,rect1) or point_in_rect(p24,rect1)
	
	if one_in_two or two_in_one:
		return True
	else: return False