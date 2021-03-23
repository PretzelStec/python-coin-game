import arcade

#game setup
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
MOVEMENT_SPEED = 5

# empty level template
# [
#     ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
#     ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
# ]


#levels setup
current_level = 0
your_times = []
LEVEL_COUNT = 4
LEVELS_MAX_COINS = [4, 1, 2, 7]
LEVELS_MAX_SECONDS = [15, 20, 30, 100]
LEVELS = [
        [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'c', ' ', ' ', ' ', ' ', ' ', 'w', 'c', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
            ['w', ' ', 'w', 'w', 'w', 'w', ' ', ' ', 'w', 'w'],
            ['w', ' ', ' ', 'w', 'c', 'w', ' ', 'w', 'w', 'w'],
            ['w', 'w', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'w'],
            ['w', 'c', 'w', 'w', 'w', 'w', ' ', 'w', 'w', 'w'],
            ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
        ],
        [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', ' ', ' ', ' ', 'w', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', 'w', 'w', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', 'p', 'w', ' ', 'w', ' ', ' ', 'w'],
            ['w', ' ', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'c', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
        ],
        [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', ' ', ' ', ' ', ' ', ' ', 'w', 'c', ' ', 'w'],
            ['w', ' ', 'w', 'w', 'w', ' ', 'w', 'w', ' ', 'w'],
            ['w', ' ', 'w', 'w', ' ', 'p', ' ', ' ', ' ', 'w'],
            ['w', ' ', ' ', ' ', 'w', ' ', 'w', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w', 'w'],
            ['w', ' ', ' ', ' ', 'w', ' ', 'w', ' ', ' ', 'w'],
            ['w', 'w', 'w', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', 'c', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
        ],
        [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'c', ' ', ' ', 'w', 'c', ' ', ' ', 'c', 'w'],
            ['w', ' ', ' ', ' ', ' ', 'w', ' ', ' ', 'w', 'w'],
            ['w', ' ', ' ', 'w', ' ', 'w', 'w', ' ', 'w', 'w'],
            ['w', ' ', 'c', 'w', ' ', 'w', ' ', ' ', 'c', 'w'],
            ['w', ' ', ' ', ' ', 'p', ' ', ' ', 'w', 'w', 'w'],
            ['w', ' ', ' ', 'w', ' ', 'w', ' ', ' ', ' ', 'w'],
            ['w', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', 'w'],
            ['w', 'c', ' ', ' ', ' ', ' ', 'w', 'c', 'w', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
        ]
]


class Level(arcade.View):
    """ Main application class. """

    def __init__(self, levelMatrix, maxScore):
        super().__init__()
        self.levelMatrix = levelMatrix
        self.max_score = maxScore
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here

        #set up the character and the wall sprites
        self.player_list = arcade.SpriteList()
        self.player_sight_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.total_time = 0.0
        
        self.score = 0

        #build wall
        self.build_level_from_matrix(self.levelMatrix, 0.75)
        

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.player_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_sight_list.draw()

        output = f"Score: {self.score} / {self.max_score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        timeleft = LEVELS_MAX_SECONDS[current_level]-int(self.total_time) % 60
        output = f"Time remaining: {timeleft}"
        if timeleft <= 5:
            arcade.draw_text(output, 10, 35, arcade.color.RED, 14)
        else:
            arcade.draw_text(output, 10, 35, arcade.color.WHITE, 14)

    def add_wall(self, x, y, scale : float = 1):
        wall = arcade.Sprite('./wallblock.png', 1 * scale)
        wall.center_x=x
        wall.center_y=y
        self.wall_list.append(wall)

    def add_player(self, x, y, scale : float = 1):
        self.playerSprite = arcade.Sprite('./smile.png', 0.05 * scale)
        self.playerSprite.center_x = x
        self.playerSprite.center_y = y
        self.player_list.append(self.playerSprite)

        self.player_sight = arcade.Sprite('./playerSight.png', 1 * scale)
        self.player_sight.center_x = x
        self.player_sight.center_y = y
        self.player_sight_list.append(self.player_sight)

    def add_coin(self, x, y, scale : float = 1):
        coin = arcade.Sprite('./coin.png', 0.5 * scale)
        coin.center_x = x
        coin.center_y = y
        self.coin_list.append(coin)

    def build_level_from_matrix(self, matrix, scale : float = 1):
        pos_y = 50 * scale
        pos_x = 50 * scale

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if(matrix[len(matrix)-x-1][y] == 'w'):
                    self.add_wall(pos_x, pos_y, scale)
                if(matrix[len(matrix)-x-1][y] == 'p'):
                    self.add_player(pos_x, pos_y, scale)
                if(matrix[len(matrix)-x-1][y] == 'c'):
                    self.add_coin(pos_x, pos_y, scale)
                pos_x += 100 * scale
            pos_x = 50 * scale
            pos_y += 100 * scale

        self.physics_engine = arcade.PhysicsEngineSimple(self.playerSprite, self.wall_list)
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.playerSprite.change_y = MOVEMENT_SPEED

        elif key == arcade.key.DOWN:
            self.playerSprite.change_y = -MOVEMENT_SPEED
 
        elif key == arcade.key.LEFT:
            self.playerSprite.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.playerSprite.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.playerSprite.change_y = 0
            self.player_sight.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.playerSprite.change_x = 0
            self.player_sight.change_x = 0

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        global current_level 
        self.total_time += delta_time

        if self.total_time >= LEVELS_MAX_SECONDS[current_level]:
            view = Failed()
            self.window.show_view(view)

        self.physics_engine.update()
        
        self.player_sight.center_x = self.playerSprite.center_x
        self.player_sight.center_y = self.playerSprite.center_y

        self.player_sight_list.update()
        self.coin_list.update()
        self.player_list.update()
        self.wall_list.update()

        hit_list = arcade.check_for_collision_with_list(self.playerSprite, self.coin_list)

        for x in hit_list:
            x.remove_from_sprite_lists()
            self.score += 1

        if self.score == self.max_score:
            your_times.append(self.total_time)
            if current_level < LEVEL_COUNT-1:
                current_level += 1
                view = Complete(self.total_time)
                self.window.show_view(view)
            else:
                current_level = 0
                view = Beat()
                self.window.show_view(view)



class Complete(arcade.View):
    """ Main application class. """

    def __init__(self, time : int = 0):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.message = 'Complete'
        self.time = int(time)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        status = self.message
        arcade.draw_text(status, 20, SCREEN_HEIGHT//2, arcade.color.WHITE, 40)
        arcade.draw_text('Click anywhere to start next level.', 20, SCREEN_HEIGHT//2-45, arcade.color.WHITE, 15)
        for x in range(len(your_times)):
            arcade.draw_text(f'Level {x+1} : {your_times[x]} seconds', 20, SCREEN_HEIGHT//2-(x+2)*45, arcade.color.WHITE, 15)
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = Level(LEVELS[current_level], LEVELS_MAX_COINS[current_level])
        game_view.setup()
        self.window.show_view(game_view)

class Failed(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_RED)
        self.message = 'Failed'

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        status = self.message
        arcade.draw_text(status, 20, SCREEN_HEIGHT//2, arcade.color.WHITE, 40)
        arcade.draw_text('Click anywhere to restart the level.', 20, SCREEN_HEIGHT//2-45, arcade.color.WHITE, 15)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = Level(LEVELS[current_level], LEVELS_MAX_COINS[current_level])
        game_view.setup()
        self.window.show_view(game_view)
        
class Beat(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        y_pos = SCREEN_HEIGHT-100
        arcade.draw_text('You Beat the Game!!!!', 20, y_pos, arcade.color.WHITE, 40)
        arcade.draw_text('Click anywhere to restart the game.', 20, y_pos-45, arcade.color.WHITE, 15)
        for x in range(len(your_times)):
            arcade.draw_text(f'Level {x+1} : {your_times[x]} seconds', 20, y_pos-(x+2)*45, arcade.color.WHITE, 15)
        arcade.draw_text(f'Total : {sum(your_times)} seconds', 20, y_pos-(len(your_times)+2)*45, arcade.color.WHITE, 15)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        global your_times
        your_times = []
        game_view = Level(LEVELS[current_level], LEVELS_MAX_COINS[current_level])
        game_view.setup()
        self.window.show_view(game_view)


def main():
    """ Main method """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    start_view = Level(LEVELS[current_level], LEVELS_MAX_COINS[current_level])
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()