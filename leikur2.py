#imports
import arcade

#consts
breidd = 1920
haed = 1080
nafn = "booga ooga"
#classes
class game(arcade.Window):
    def __init__(self, breidd, haed, nafn_leiks):
        super().__init__(breidd,haed,nafn_leiks,)
        self.bakgrunnur = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.geimskip = arcade.load_texture(":resources:images/space_shooter/playerShip1_orange.png")    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, breidd, haed, self.bakgrunnur)
        arcade.draw_scaled_texture_rectangle(breidd/2,haed/8, self.geimskip)
        
bozo = game(breidd,haed,nafn)
arcade.run()
