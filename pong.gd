extends Node2D

var window_size: Vector2i
var centre: Vector2i

func _ready():
	window_size = get_viewport_rect().size

	centre = window_size / 2

	for child in get_children():
		child.position = centre

	# Ball
	$Ball.serve(centre)


func _process(delta):
	for pallete in $Players.get_children():
		pallete.move(0, window_size.y, delta)
	$Ball.move(delta)
	
	if 0 > $Ball.position.y or $Ball.position.y > window_size.y:
		$Ball.bounce(Vector2i.UP)
	if 0 > $Ball.position.x or $Ball.position.x > window_size.x:
		$Ball.serve(centre)
