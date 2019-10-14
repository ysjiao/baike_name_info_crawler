import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url, fout):
		success = True
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print('craw %d: %s' % (count, new_url))
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				# self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
				self.outputer.output_html(fout)

				if count == 100:
					break

				# count += 1
			except:
				print('craw failed')
				success = False

		self.outputer.output_html(fout)
		return success


def read_namelist(path) -> list:
	name_file = open(path, 'r', encoding='utf-8')
	name_list = []
	for line in name_file.readlines():
		name_list.append(line.split('\t')[0])
	return name_list


if __name__ == "__main__":
	name_list = read_namelist('hk_name.txt')
	fout = open('output.html', 'w', encoding = 'utf-8')
	unsuccess_file = open('unsuccess_name.txt', 'w', encoding='utf-8')
	for name in name_list:
		# name = '诸葛'
		root_url = f"https://baike.baidu.com/item/{name}"
		obj_spider = SpiderMain()
		success = obj_spider.craw(root_url, fout)
		if not success:
			unsuccess_file.write(name + '\n')
			unsuccess_file.flush()
	fout.close()
	unsuccess_file.close()