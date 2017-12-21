"""
Chain of responsibility Pattern.
When it's unknown which process(function) would deal with a request, use Chain of Responsibility to deliver the request until proper 
process receive it.
"""

class Event:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


class Widget:
	def __init__(self, parent=None):
		self.parent = parent

	# if a instance can't handle the event, it would pass the event to it's parent, finally use handle_default.
	def handle(self, event):
		handler = 'handle_{}'.format(event)
		if hasattr(self, handler):
			method = getattr(self, handler)
			method(event)
		elif self.parent:
			self.parent.handle(event)
		elif hasattr(self, 'handle_default'):
			self.handle_default(event)


# MainWindow is the end of chain, has handle_default method.
# if all the classes before can't handle the event, MainWindow would deal with it. 
class MainWindow(Widget):
	def handle_close(self, event):
		print('MainWindow: {}'.format(event))

	def handle_default(self, event):
		print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):
	def handle_paint(self, event):
		print('SendDialog: {}'.format(event))


class MsgText(Widget):
	def handle_down(self, event):
		print('MsgText: {}'.format(event))


def main():
	# msg ---> sd ---> mw
	mw = MainWindow()
	sd = SendDialog(mw)
	msg = MsgText(sd)

	for e in ('down', 'paint', 'unhandled', 'close'):
		evt = Event(e)
		print('\nSending event -{}- to MainWindow'.format(evt))
		mw.handle(evt)
		print('Sending event -{}- to SendDialog'.format(evt))
		sd.handle(evt)
		print('Sending event -{}- to MsgText'.format(evt))
		msg.handle(evt)


if __name__ == '__main__':
	main()