extends Area2D

const SERVE_VARIANCE: float = 0.125

var heading: Vector2
var speed: int = 80
var direction: int = 1

func serve(start):
	direction *= -1
	heading = Vector2.UP.rotated(PI * randfn(0.5 - SERVE_VARIANCE, 0.5 + SERVE_VARIANCE)) * direction
	global_position = start

func move(delta):
	global_position += speed * heading * delta

func bounce(normal):
	heading = heading.bounce(normal)