import time
import stdiomask as sm

from selenium import webdriver



driver = webdriver.Chrome('/Users/odursun/Desktop/selenium/chromedriver')  

driver.get('https://enabiz.gov.tr/');
print("Sayfa açılıyor....")

time.sleep(5)

tcno = driver.find_element_by_id('username')

tcno.send_keys(sm.getpass('Tc kimliğinizi giriniz: '))

sifreniz = driver.find_element_by_id('Sifre')

sifreniz.send_keys(sm.getpass('Şifrenizi giriniz: '))

butongiris = driver.find_element_by_id('btnGiris')

butongiris.click()

time.sleep(5) # Let the user actually see something!

driver.get('https://enabiz.gov.tr/HastaBilgileri/Tahliller#Covid19Sonuc');
print("Sayfa açılıyor....")

pdf_linki = None

while pdf_linki == None:
    dil = input("Hangi dilde indirmek istiyorsunuz? [tr/en]: ")

    if dil == "tr":
        pdf_linki = driver.find_element_by_css_selector("#Covid19TahlilTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1)")
        pdf_linki.click()
    elif dil == "en":
        pdf_linki = driver.find_element_by_css_selector("#Covid19TahlilTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > a:nth-child(2)")
        pdf_linki.click()
    else:
        print("Hatalı bilgi girdiniz! Lütfen tekrar deneyin.")

print("Dosya indiriliyor....")
time.sleep(7)
driver.quit()
