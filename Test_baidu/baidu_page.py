# -*-coding:utf-8-*-
import os
import configparser
from base import BasePage

# 获取配置文件参数
ele_ini = os.path.dirname(os.path.abspath(__file__)) + '\WebElement.ini'
f = configparser.ConfigParser()
f.read(ele_ini)
baidu_section = f.get("baidu", "queryBox_id")
baidu_option = f.get("baidu", "queryBtn_id")


class BaiduPage(BasePage):
	# 申明连接
	url = "https://www.baidu.com"

	"""
	百度page层，百度页面封装操作到的元素
	"""
	def search_input(self, search_key):
		self.by_id(baidu_section).send_keys(search_key)


	def search_button(self):
		self.by_id(baidu_option).click()
