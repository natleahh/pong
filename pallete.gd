extends Area2D

class_name Pallette

enum ControlScheme {Left, Right}

@export var control_scheme: ControlScheme
@export var texture: CompressedTexture2D

var move_up: StringName
var move_down: StringName

const PALLETTE_SPEED: int = 80


func _ready():
	# Set rect of Sprite as collision Shape
	$Sprite2D.texture = texture
	var new_shape = RectangleShape2D.new()
	new_shape.extents = $Sprite2D.get_rect().size / 2
	$CollisionShape2D.set_shape(new_shape)

	# Set Control scheme
	match control_scheme:
		ControlScheme.Left:
			move_up = "left_move_up"
			move_down = "left_move_down"
		ControlScheme.Right:
			move_up = "right_move_up"
			move_down = "right_move_down"


func move(y_min: int, y_max: int, delta):
	"""Moves pallete """
	var direction = 0
	var shape_buffer = $CollisionShape2D.shape.get_size().y / 2

	if Input.is_action_pressed(move_up):
		direction -= 1
	if Input.is_action_pressed(move_down):
		direction += 1
	
	var new_height = (PALLETTE_SPEED * direction * delta) + global_position.y
	global_position.y = clamp(
		new_height, y_min + shape_buffer, y_max - shape_buffer
	)

func _on_area_entered(area):
	print(area.position)
	area.bounce(Vector2i.LEFT)
