extends Area2D

var heading: Vector2
var speed: int = 1000
var direction: int = 1

func serve(start):
	direction *= -1
	heading = Vector2.UP.rotated(PI * randfn(0.5, 0.25)) * direction
	position = start

func move(delta):
	global_position += speed * heading * delta

func _ready():
	serve(global_position)

func _process(delta):
	move(delta)
