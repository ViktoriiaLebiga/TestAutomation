import pytest
from selenium import webdriver


@pytest.yield_fixture(scope="session") #декоратор пайтеста для всей сессии чтобы открыть браузер
def driver(): #функция
   _driver = webdriver.Chrome("D:\kurs\drivers\chromedriver.exe")
   return _driver


@pytest.fixture(scope="session", autouse=True)   #чтобы закрыть браузер
def stop(request, driver):
   def fin():
       driver.quit()
   request.addfinalizer(fin) #request - текстура; addfinalizer - сделать в последнюю очередь
