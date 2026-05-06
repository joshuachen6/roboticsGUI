import pyglet
from src.gui.app import Application

if __name__ == '__main__':
    # Get the primary screen to calculate window size
    display = pyglet.canvas.Display().get_default_screen()
    
    # Calculate a nice window size (16:9 ratio, approx 75% of screen height)
    x_mult, y_mult = display.width / 16, display.height / 9
    mult = round(min(x_mult, y_mult) * 0.75)
    
    # Initialize the application
    app = Application(16 * mult, 9 * mult)

    # Schedule the update loop (at 60 FPS)
    pyglet.clock.schedule_interval(app.update, 1/60.0)
    
    # Start the pyglet app
    pyglet.app.run()
