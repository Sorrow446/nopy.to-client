# 1st
import re
# 3rd
import requests
# own
from nopy.exceptions import *


class Client():

	def __init__(self, username=None, password=None):
		self.session = requests.Session()
		self.session.headers.update({
			'User-Agent': "nopy.to client (by Sorrow446)"})
		self.base = "https://data.nopy.to/"
		# self.is_auth = False
		# if username and password:
			# self.auth(username, password)

	# def auth(self, username, password):
		# data = {
			# 'user': username,
			# 'pass': password
		# }
		# data = self.make_call('login', data=data)
		# self.is_auth = True
		# return data

	def check_url(self, url):
		regex = r'^https://nopy.to/([a-zA-Z\d]{8})/([\w\-.]+)/?$'
		match = re.match(regex, url)
		if not match:
			raise InvalidURLError("Invalid URL.")
		return match.group(1), match.group(2)

	def make_call(self, endpoint, data=None, file=None):
		r = self.session.post(self.base + endpoint, data=data, files=file)
		if r.status_code != 200:
			raise BadResponseError(
				"The API returned a {}. Response: {}".format(r.status_code, r.text))
		resp = r.json()
		if resp['status'] != "ok":
			raise BadResponseError(
				"Error present in response. Message from API: {}".format(resp['msg']))
		return resp['msg']

	# Internal calling only.
	def get_file_url(self, code, id, request, session):
		data = {
			'code': code,
			'fid': id,
			'request': request,
			'session': session
		}
		resp = self.make_call('download', data=data)
		return resp['download']

	def get_file_meta(self, url):
		code, file = self.check_url(url)
		data = {
			'code': code,
			'file': file
		}
		resp = self.make_call('file', data=data)
		file_url = self.get_file_url(code, resp['fid'], resp['request'],
														resp['session'])
		resp['file_url'] = file_url
		return resp

	# def upload_file(self, path):
		# if not self.is_auth:
			# raise NotAuthenticatedError("Authentification required.")
		# file = {
			# 'file': open(path, 'rb')
		# }
		# resp = self.make_call('upload', file=file)
		# return resp
