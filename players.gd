extends Node2D

const offset: int = 175

func _ready():
	$LeftPallette.position.x -= offset
	$RightPallette.position.x += offset
