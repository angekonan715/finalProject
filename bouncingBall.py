import pyray as pr

class Constant:
    # responsibility is  constant
    def __init__(self):
        self._SCREENWIDTH = 600
        self._SCREENHEIGHT = 400
        self.playerPosition_x = 250
        self.playerPosition_y = 380
        self.ballPosition_x = self._SCREENWIDTH/2
        self.ballPosition_y = self._SCREENHEIGHT/2
        self.ballSpeed_x = 5
        self.ballSpeed_y = 4
        self.ballRadius = 10
        self.pause = True
        self.framesCounter = 0

class Screen:
    # set my screen width and height and the ackground color
    def __init__(self):
        self.measure = Constant()
    
    
    def initWindow(self, SCREENWIDTH , SCREENHEIGHT, title):
        return pr.init_window(SCREENWIDTH, SCREENHEIGHT, title)
    
    def closeWindow(self):
        return pr.close_window()
    
    def beginDrawing(self):
        return pr.begin_drawing()
    
    def endDrawing(self):
        return pr.end_drawing()
    
    def clearBackground(self):
        return pr.clear_background(pr.GRAY)
    
    def drawCircle(self, x, y, r):
        return pr.draw_circle(x, y, r, pr.BLACK)
    
    def drawRectangle(self, rect_x, rect_y , L, l):
        return  pr.draw_rectangle(rect_x, rect_y, L, l, pr.RED)
        


class main(Constant):
    
    def __init__(self):
        self.screen = Screen()
        self._message = "Wecome To the Ball Bouncing Game"
        super().__init__()
         
    def playGame(self):
        self.screen.initWindow(self._SCREENWIDTH, self._SCREENHEIGHT , self._message)
        pr.set_target_fps(60)
        
        while not pr.window_should_close():
            if (pr.is_key_pressed(pr.KEY_SPACE)): 
                self.pause = False
            if not self.pause:
                self.ballPosition_x += self.ballSpeed_x
                self.ballPosition_y += self.ballSpeed_y
    
                if ((self.ballPosition_x >= (pr.get_screen_width() - self.ballRadius)) or (self.ballPosition_x <= self.ballRadius)):
                    self.ballSpeed_x *= -1
                if ((self.ballPosition_y >= (pr.get_screen_height()  - self.ballRadius)) or (self.ballPosition_y<= self.ballRadius)):
                    self.ballSpeed_y *= -1
            
                if ( pr.is_key_down(pr.KEY_A)):
                    self.playerPosition_x -= 10
                
                elif (pr.is_key_down(pr.KEY_D)) :
                    self.playerPosition_x += 10
    
            else:
                self.framesCounter +=1
    
    
            self.screen.beginDrawing()
            self.screen.clearBackground()
            self.screen.drawCircle(int(self.ballPosition_x) , int(self.ballPosition_y), self.ballRadius )
            self.screen.drawRectangle(self.playerPosition_x, self.playerPosition_y, 100, 10)
            if (self.pause and ((self.framesCounter/30)%2)):
                pr.draw_text("PAUSED", 350, 200, 30, pr.RED)
                pr.draw_fps(10, 10)
       
    
            self.screen.endDrawing()

        self.screen.closeWindow()

p = main()

p.playGame()