import io
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

	inFile_hin = sys.argv[1]
	out_file = sys.argv[2]

	print("Opening browser...")
	browser = webdriver.Firefox()
	browser.minimize_window()
	print("Opening link...")
	browser.get('https://translate.google.com/')
	
	print("Reading input file...")
	
	with open(inFile_hin,'r') as fin:
 		lines = fin.readlines()
		data = " ".join(str(x) for x in lines)
		english_input=unicode(data,"utf-8")
	
	print("Sending data to browser...")
	send_eng_inp = browser.find_element_by_id('source')
	send_eng_inp.send_keys(english_input)

	src_options = browser.find_element_by_class_name('sl-more.tlid-open-source-language-list')
	src_options.click()

	translate_from = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'sl_list-search-box')))
	translate_from.send_keys(inFile_hin + '\n')

	tgt_options = browser.find_element_by_class_name('tl-more.tlid-open-target-language-list')
	tgt_options.click()

	translate_to = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'tl_list-search-box')))
	translate_to.send_keys(out_file + '\n')

	print("Translating...")
	print("Fetching translated data...")
	time.sleep(1)

	hin_out = browser.find_element_by_xpath("//span[@class='tlid-translation translation']").text
	
	with io.open(out_file, "a", encoding="utf-8") as fout:
		fout.write(hin_out)

	print("Translated data stored in \"" + out_file + "\" file.")
	
	browser.close()

if __name__ == '__main__':
	main()