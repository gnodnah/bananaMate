import sublime, sublime_plugin
import os
class BananaMateCleanCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		currentFileName = self.view.file_name()
		print("Current File name:"+currentFileName)
		baseDir = os.path.dirname(currentFileName)

		for sel in sels:
			str = self.view.substr(sel)
			path = baseDir + "/"
			strList = str.split('_')
			for value in strList:
				path = path + value + '/'
			if(not os.path.exists(path)):
				os.mkdir(path)
			sublime.active_window().open_file(path+"clean.json")	

class BananaMateCheckCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		currentFileName = self.view.file_name()
		print("Current File name:"+currentFileName)
		baseDir = os.path.dirname(currentFileName)

		for sel in sels:
			str = self.view.substr(sel)
			path = baseDir + "/"
			strList = str.split('_')
			for value in strList:
				path = path + value + '/'
			if(not os.path.exists(path)):
				os.mkdir(path)
			sublime.active_window().open_file(path+"check.json")				
			
class BananaMateInitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		currentFileName = self.view.file_name()
		print("Current File name:"+currentFileName)
		baseDir = os.path.dirname(currentFileName)

		for sel in sels:
			str = self.view.substr(sel)
			path = baseDir + "/"
			strList = str.split('_')
			for value in strList:
				path = path + value + '/'
			if(not os.path.exists(path)):
				os.mkdir(path)
			sublime.active_window().open_file(path+"init.json")	

class BananaMateGroovyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		currentFileName = self.view.file_name()
		print("Current File name:"+currentFileName)
		baseDir = os.path.dirname(currentFileName)

		for sel in sels:
			str = self.view.substr(sel)
			path = baseDir + "/"
			strList = str.split('_')
			for value in strList:
				path = path + value + '/'
			if(not os.path.exists(path)):
				os.mkdir(path)
			sublime.active_window().open_file(path+"invoke.groovy")

class BananaMateAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		currentFileName = self.view.file_name()
		print("Current File name:"+currentFileName)
		baseDir = os.path.dirname(currentFileName)

		for sel in sels:
			str = self.view.substr(sel)
			path = baseDir + "/"
			strList = str.split('_')
			for value in strList:
				path = path + value + '/'
			if(os.path.exists(path)):
				sublime.active_window().open_file(path+"invoke.groovy")
				sublime.active_window().open_file(path+"init.json")
				sublime.active_window().open_file(path+"clean.json")
				sublime.active_window().open_file(path+"check.json")
										