from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector
import schedule
import time


def scrape():

    bbca = 'https://sesaham.com/emiten/BBCA'
    tlkm = 'https://sesaham.com/emiten/TLKM'
    icbp = 'https://sesaham.com/emiten/ICBP'
    asii = 'https://sesaham.com/emiten/ASII'
    untr = 'https://sesaham.com/emiten/UNTR'
    antm = 'https://sesaham.com/emiten/ANTM'
    ggrm = 'https://sesaham.com/emiten/GGRM'
    bbni = 'https://sesaham.com/emiten/BBNI'
    bbri = 'https://sesaham.com/emiten/BBRI'
    unvr = 'https://sesaham.com/emiten/UNVR'


    driver1 = webdriver.Chrome()
    driver2 = webdriver.Chrome()
    driver3 = webdriver.Chrome()
    driver4 = webdriver.Chrome()
    driver5 = webdriver.Chrome()
    driver6 = webdriver.Chrome()
    driver7 = webdriver.Chrome()
    driver8 = webdriver.Chrome()
    driver9 = webdriver.Chrome()
    driver10 = webdriver.Chrome()

    driver1.get(bbca)
    driver2.get(tlkm)
    driver3.get(icbp)
    driver4.get(asii)
    driver5.get(untr)
    driver6.get(antm)
    driver7.get(ggrm)
    driver8.get(bbni)
    driver9.get(bbri)
    driver10.get(unvr)

    bbca_per = driver1.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    bbca_npm = driver1.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    bbca_pbv = driver1.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    bbca_roe = driver1.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver1.close()

    tlkm_per = driver2.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    tlkm_npm = driver2.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    tlkm_pbv = driver2.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    tlkm_roe = driver2.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver2.close()

    icbp_per = driver3.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    icbp_npm = driver3.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    icbp_pbv = driver3.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    icbp_roe = driver3.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver3.close()

    asii_per = driver4.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    asii_npm = driver4.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    asii_pbv = driver4.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    asii_roe = driver4.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver4.close()

    untr_per = driver5.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    untr_npm = driver5.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    untr_pbv = driver5.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    untr_roe = driver5.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver5.close()

    antm_per = driver6.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    antm_npm = driver6.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    antm_pbv = driver6.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    antm_roe = driver6.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver6.close()

    ggrm_per = driver7.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    ggrm_npm = driver7.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    ggrm_pbv = driver7.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    ggrm_roe = driver7.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver7.close()

    bbni_per = driver8.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    bbni_npm = driver8.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    bbni_pbv = driver8.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    bbni_roe = driver8.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver8.close()

    bbri_per = driver9.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    bbri_npm = driver9.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    bbri_pbv = driver9.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    bbri_roe = driver9.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver9.close()

    unvr_per = driver10.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[1]/span[2]').text.replace('PER : ', '')
    unvr_npm = driver10.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[7]/div/ul/li[1]/span[2]').text.replace('NPM : ', '').replace('%', '')
    unvr_pbv = driver10.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[2]/span[2]').text.replace('PBV : ', '')
    unvr_roe = driver10.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[1]/div/div[6]/div/ul/li[3]/span[2]').text.replace('ROE : ', '')
    driver10.close()

    def update_tabel_evaluasi(nil, alt, kri):
        try :
            db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', port = '3307', database = 'db_spksaw')

            mycursor = db.cursor()

            sql = "UPDATE evaluasi SET nilai = %s WHERE id_alternatif = %s AND id_kriteria = %s AND created_at IS NULL"
            updateData = (nil, alt, kri)

            mycursor.execute(sql, updateData)

            db.commit()

            print(mycursor.rowcount, "record(s) affected")

        except mysql.connector.Error as error:
            print('gagal')
        finally:
            if db.is_connected():
                mycursor.close()
                db.close()
                print("MySQL connection is closed")

    update_tabel_evaluasi(bbca_per,1,1)
    update_tabel_evaluasi(bbca_npm,1,2)
    update_tabel_evaluasi(bbca_pbv,1,3)
    update_tabel_evaluasi(bbca_roe,1,4)
    update_tabel_evaluasi(tlkm_per,2,1)
    update_tabel_evaluasi(tlkm_npm,2,2)
    update_tabel_evaluasi(tlkm_pbv,2,3)
    update_tabel_evaluasi(tlkm_roe,2,4)
    update_tabel_evaluasi(icbp_per,3,1)
    update_tabel_evaluasi(icbp_npm,3,2)
    update_tabel_evaluasi(icbp_pbv,3,3)
    update_tabel_evaluasi(icbp_roe,3,4)
    update_tabel_evaluasi(asii_per,4,1)
    update_tabel_evaluasi(asii_npm,4,2)
    update_tabel_evaluasi(asii_pbv,4,3)
    update_tabel_evaluasi(asii_roe,4,4)
    update_tabel_evaluasi(untr_per,5,1)
    update_tabel_evaluasi(untr_npm,5,2)
    update_tabel_evaluasi(untr_pbv,5,3)
    update_tabel_evaluasi(untr_roe,5,4)
    update_tabel_evaluasi(antm_per,6,1)
    update_tabel_evaluasi(antm_npm,6,2)
    update_tabel_evaluasi(antm_pbv,6,3)
    update_tabel_evaluasi(antm_roe,6,4)
    update_tabel_evaluasi(ggrm_per,7,1)
    update_tabel_evaluasi(ggrm_npm,7,2)
    update_tabel_evaluasi(ggrm_pbv,7,3)
    update_tabel_evaluasi(ggrm_roe,7,4)
    update_tabel_evaluasi(bbni_per,8,1)
    update_tabel_evaluasi(bbni_npm,8,2)
    update_tabel_evaluasi(bbni_pbv,8,3)
    update_tabel_evaluasi(bbni_roe,8,4)
    update_tabel_evaluasi(bbri_per,9,1)
    update_tabel_evaluasi(bbri_npm,9,2)
    update_tabel_evaluasi(bbri_pbv,9,3)
    update_tabel_evaluasi(bbri_roe,9,4)
    update_tabel_evaluasi(unvr_per,10,1)
    update_tabel_evaluasi(unvr_npm,10,2)
    update_tabel_evaluasi(unvr_pbv,10,3)
    update_tabel_evaluasi(unvr_roe,10,4)

scrape()

schedule.every().hour.at(':05').do(scrape)

while True:
    schedule.run_pending()
    time.sleep(1)