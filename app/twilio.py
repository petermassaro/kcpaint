from twilio.rest import Client
from flask import current_app


class Twilio:

	def __init__(self, app=None):
		self.app = app
		if app is not None:
			self.init_app(app)
		else:
			self.client = None

	def init_app(self, app):
		self.app = app
		self.client = Client(
			self.app.config['TWILIO_ACCOUNT_SID'],
			self.app.config['TWILIO_AUTH_TOKEN']
			)


	def send(self, msg, recipientNumber):
		self.client.api.account.messages.create(
			to='+1{}'.format(recipientNumber),
				from_=self.app.config['TWILIO_NUMBER'],
				body=msg
				)