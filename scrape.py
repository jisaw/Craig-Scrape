__author__ = "__JakeSawyer__"

import requests
from lxml import html

def load_queries():
	f = open("search.txt", "r")
	queries = f.read()
	return queries.lower().split('//')

def get_query_page(q):
	r = requests.get("https://desmoines.craigslist.org/search/sss?query=%s" % q)
	data = r.text
	return html.fromstring(data)

def get_data(tree):
	titles = tree.xpath("//a[@class='hdrlnk']/text()")
	price = tree.xpath("//span[@class='price']/text()")
	prices = []
	for i in range(len(price)):
		if i % 2 ==0:
			prices.append(price[i])
	times = tree.xpath("//time/@datetime")
	data = []
	for i in range(len(prices)):
		data.append([titles[i], prices[i], times[i]])
	return data

def print_data(data):
	for field in data:
		try:
			print("Title: %s\nPrice: %s\nDate Posted: %s\n\n" % (field[0], field[1], field[2]))
		except:
			print("ERROR")

def main():
	queries = load_queries()
	for q in queries:
		print(q.upper())
		print("*******************")
		print_data(get_data(get_query_page(q)))
		
if __name__ == "__main__":
	main()