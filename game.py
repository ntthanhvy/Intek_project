import pyglet

from game import *

#set up path for resources
pyglet.resource.path = ['./game/game-graphic']
pyglet.resouce.reindex()

#set up score and lives
score = 0
lives = []

#set up game_state
state = [MAIN_MENU, PLAYING, GAME_OVER]
game_state = MAIN_MENU

#set up window.
main_menu = create_main_menu(main_menu_batch)
game_objects = crea

#set up image.
player_img = pyglet.resouce.image('player1.png')
enemy_img = pyglet.resouce.image('enemy.png')
goal_img = pyglet.resource.image('goal.png')
BG_img = pyglet.resource.image('BG.png')

#set up batch
main_menu_batch = pyglet.graphics.Batch() #for all menu options
# score_lives_menu_batch = pyglet.graphicx.Batch() #for lives and score label
object_batch = pyglet.graphics.Batch() #for all object inside game
lable_batch = pyget.graphics.Batch() #for all other label
game_over_batch = pyglet.graphics,Batch() #for game over screen

#set up srpite
def set_up_sprite(object, batch):
    return pyglet.sprite.Sprite(
        img=object,
        anchor_x='center', anchor_y='center',
        batch=batch
    )

player = set_up_sprite(player_img, object_batch)
enemy = set_up_sprite(enemy_img, object_batch)
goal_img = set_up_sprite(goal_img, object_batch)
BG = set_up_sprite(BG_img, main_menu_batch)

def create_main_menu(main_menu_batch):
    game_label = unit.create_label('ESCAPE', main_menu_batch)
    menu_label_text = ['PLAY', 'EXIT']
    return unit.create_label_text(menu_label_text, main_menu_batch)


def create_gameover_menu(game_over_batch):
    game_over_label = unit.create_label('GAME OVER!!', game_over_batch)
    score = unit.create_label_text('SCORE: ', score_lives_menu_batch,
                                    selected=True)
    game_over_menu = ['CONTINUE', 'EXIT']
    return (
        score,
        unit.create_label_text(game_over_menu, game_over_batch)
    )


def create_game_label(label_batch):
    '''create score and lives label'''
    score_label = pyglet.text.Label(
        text='SCORE: %d' % score,
        x=20, y=30,
        font_name='Syncopate',
        font_size=30,
        batch=label_batch
    )
    global lives

    for i in range(5):
        life_sprite = set_up_sprite(
            img=player_img,
            x=720 - i *10,
            y=585,
            batch=label_batch
        )
        life_sprite.scale = 0.5
        life_sprite.rotation = 230
        lives.append(life_sprite)

    return lives, score_label


def on_draw():
    window.clear()

    if game_state == MAIN_MENU:
        main_menu_batch.draw()

    elif game_state == PLAYING:
        object_batch.draw()
        label_batch.draw()

    elif game_state == GAME_OVER:
        object_batch.draw()
        game_over_batch.draw()


def update(dt):
    if game_state == MAIN_MENU:
        for obj in
