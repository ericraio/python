"""
First we import kivy and check if the current installed version will be enough
for our application. If not, an exception will be automatically fired, and prevent 
your application to crash in runtime. You can read the documentation of kivy.require() function
for more information
"""
import kivy
kivy.require('1.3.0')

"""
We import the App class, to be able to subclass it, By subclassing this class, your own class
gains serveral features that we already developed for you to make sure it will be recognized
by Kivy.
"""
from kivy.app import App

# Next we import the Button class, to be able to create an instance of a button with a custom label
from kivy.uix.button import Button

"""
Then, we create out application class, based on the App clas. We extend the build() function to be
able to return an instance of Button. This instance will be used as the root of the widget truee
(because we returned it)
"""
class MyApp(App):
    def build(self):
        return Button(text='Hello Fucking World!')

# Finally, we call run() on our application instance to launch the kivy process with out 
# application inside
if __name__ == '__main__':
    MyApp().run()
