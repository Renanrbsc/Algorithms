import turtle as tt
from random import randint, sample

def draw():
	size = randint(30, 90)
	angles = (75,45,120,)
	angle = sample(angles, 1)[0]

	
	colors = [
		('#922B21', '#E6B0AA'), ('#76448A', '#D2B4DE'), ('#1F618D', '#AED6F1'), ('#515A5A', '#EAEDED'),
		('#148F77', '#D1F2EB'), ('#B7950B', '#F7DC6F'), ('#F39C12', '#FDEBD0'), ('#BA4A00', '#F6DDCC')]
	color = sample(colors, 1)[0]
	tt.color(color[0], color[1])
	tt.speed(5000)
	x_pos = randint(-500,500)
	y_pos = randint(-300,300)
	tt.pu()
	tt.setpos(x_pos, y_pos)
	start_position = tt.pos()
	tt.pd()
	
	tt.begin_fill()
	while True:
		tt.forward(size)
		tt.left(angle)
		if abs(tt.pos() - start_position) < 1:
			break
	tt.end_fill()
	
tt.circle(10)
for i in range(200):
	tt.pensize(i%5) #acrescenta tamanho na linha
	draw()
tt.done()