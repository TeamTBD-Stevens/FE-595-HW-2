yy = __import__("HW 2")
if __name__ == '__main__':
    url = 'http://3.95.249.159:8000/random_company'
    yy.web_Scraper(url, 50, 'companies data3.csv')