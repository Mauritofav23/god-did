mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . f f f f f f f . 
            . . . . . . . . f f f f f f f . 
            . . . . . . . . f . . . . . f . 
            . . . . . . . . f . . . . . f . 
            . f f f f f f f f . . . . . f . 
            . f . . . . . . . . . . . . f . 
            . f . . . . . . . . . . . . f . 
            . f f f . f f f f f f . f f f . 
            . . . f . f . . . . f . f . . . 
            . . . f . f . . . . f . f . . . 
            . . . f f f . . . . f f f . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
game.game_over(False)