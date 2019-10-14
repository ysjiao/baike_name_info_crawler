class HtmlOutputer(object):

	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self, fout):
		# fout = open('output.html', 'w', encoding = 'utf-8')

		fout.write("<html>")
		fout.flush()
		fout.write("<body>")
		fout.flush()
		fout.write('<table border = "1">')
		fout.flush()

		fout.write("<tr><th>URL</th><th>Title</th><th>lemma-summary</th><th>basic-info cmn-clearfix</th></tr>")
		fout.flush()

		#Python默认编码ascii
		for data in self.datas:
			fout.write("<tr>")
			fout.flush()
			fout.write("<td>%s</td>" % data['url'])
			fout.flush()
			fout.write("<td>%s</td>" % data['title'])
			fout.flush()
			fout.write("<td>%s</td>" % data['lemma-summary'])
			fout.flush()
			fout.write("<td>%s</td>" % data['basic-info cmn-clearfix'])
			fout.flush()
			fout.write("</tr>")
			fout.flush()

		fout.write("</table>")
		fout.flush()
		fout.write("</body>")
		fout.flush()
		fout.write("</html>")
		fout.flush()
		# fout.close()