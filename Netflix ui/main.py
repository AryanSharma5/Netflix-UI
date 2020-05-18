from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from util import DATA

class MyImage(ButtonBehavior, Image):
	pass

class MyCustomButton(MDFillRoundFlatButton, RectangularElevationBehavior):
	pass

class Netflix(MDApp):
	data = DATA
	def build(self):
		return Builder.load_file('main.kv')

	def change_screen(self, curr, ext = '.jpg'):
		short = self.root.ids
		if curr != 'contentScreen':
			short.screen_manager.current = 'contentScreen'
			short.secondaryImage.source = 'images/' + curr + ext
			short.title_content.text = self.data[curr]['title_content']['text']
			short.title_content.pos_hint = self.data[curr]['title_content']['pos_hint']
			short.description.text = self.data[curr]['description']
			short.year.text = self.data[curr]['year']
			short.country.text = self.data[curr]['country']
			short.length.text = self.data[curr]['length']
			for i, src in enumerate([short.src_1, short.src_2, short.src_3]):
				src.source = self.data[curr]['src'][i]
			self.root.ids.label = curr
			self.root.ids.screen_manager.transition.direction = 'right'
		else:
			self.root.ids.screen_manager.current = 'Home'
			self.root.ids.screen_manager.transition.direction = 'left'
		self.change_icon('heart-outline', True)

	def change_icon(self, name, reverse = False, rootOrigin = False):
		short = self.root.ids
		short.heart.icon = name
		if rootOrigin:
			short.heart.text_color = (1, 0, 0, 1)
		else:
			short.heart.text_color = (1, 1, 1, 1)

Netflix().run()