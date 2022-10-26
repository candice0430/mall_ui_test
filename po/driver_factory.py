# -*- coding: UTF-8 -*-
from selenium import webdriver


class DriverFactory:

    """
        # singleton
        单例模式，保证全局只有一个driver
    """
    _instance = None
    _dirver = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_driver(cls,browers="Chrome"):
        if cls._dirver is None:
            cls._dirver = cls.create_driver(browers)
            # cls.logger.info("创建" + browers + "浏览器")
        return cls._dirver

    @classmethod
    def create_driver(cls,browers):
        # driver = None
        # if browers.lower() == "chrome":
        #     driver = webdriver.Chrome()
        # elif browers.lower() == "firfox":
        #     driver = webdriver.Chrome()
        # elif driver.lower() == "ie":
        #     driver = webdriver.Ie()
        # elif driver.lower() == "Safari":
        #     driver = webdriver.Safari()
        # else:
        #     print("您传入的参数browers异常")
        # return driver
        try:
            driver = getattr(webdriver,browers)()
        except Exception as e:
            driver = webdriver.Chrome()
        return driver