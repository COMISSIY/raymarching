import pygame, math
pygame.init()

sc = pygame.display.set_mode((600, 400))
pos = [300, 200, 100]#here
pos2 = [200, 200, 0]
pos3 = [400, 200, 0]
offset = 200

clock = pygame.time.Clock()
rad = 200
depth = 500
step = 1

def find_dist(pos, obj):
	return math.sqrt((pos[0]-obj[0])**2 + (pos[1]-obj[1])**2 + (pos[2]-obj[2])**2)

pix = []
l2 = []
def circle(pos, rad, l):
	for y in range(pos[1]-rad, pos[1]+rad, step):
		for x in range(pos[0]-rad, pos[0]+rad, step):
			for z in range(0, depth, step):
				dist = find_dist(pos, (x, y, z))
				if dist < rad:
					l.append([x, y, z])
					break
	print(1)

def floor(l, height, step):
	for x in range(0, 600, step):
		for y in range(0, 400, step):
			for z in range(0, depth, step):
				dist = find_dist((x, 400-height, z), (x, y, z))
				if dist < rad:
					l.append([x, y, z])
					break


def draw(l, p):
	for i in l:
		l1 = find_dist((i[0], i[1], i[2]), (*p, offset))
		if l1 > 255:
			l1 = 255
		color = (255-l1, 255-l1, 255-l1)
		sc.set_at((i[0], i[1]), color)

def move(l, x, y):
	for i in l:
		i[0] += x
		i[1] += y


circle(pos, rad, pix)
print(len(l2))
while True:
	clock.tick(60)
	[exit() for i in pygame.event.get() if i.type == pygame.QUIT]
	sc.fill((0, 0, 0))
	p = pygame.mouse.get_pos()
	
	draw(pix, pygame.mouse.get_pos())
	l = []
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		offset += 10
		print(offset)
	if keys[pygame.K_DOWN]:
		offset -= 10
		print(offset)
	pygame.display.update()