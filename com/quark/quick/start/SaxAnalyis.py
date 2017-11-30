# python sax 解析xml实例 movie.xml
import xml.sax  # 建议手动导入
import xml.dom.minidom  # 建议手动导入


# import xml  注意不能导这个包


# sax解析 xml文件
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用（从文件开头开始扫描）
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content




  # dom解析xml文件
def domAnalyis():
    # dom解析器打开文件
    domTree = xml.dom.minidom.parse("movie.xml")
    collection = domTree.documentElement
    if collection.hasAttribute('shelf'):
        print("root element:%s"%(collection.getAttribute("shelf")))
    #获取所有movie标签
    movies = collection.getElementsByTagName("movie")
    #打印每一个movie标签中的元素
    for movie in movies:
        print(movie.getAttribute("title"))
    type = movie.getElementsByTagName('type')[0]
    print("Type: %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print("Format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)


if (__name__ == "__main__"):
    # # 创建一个 XMLReader
    # parser = xml.sax.make_parser()
    # # turn off namepsaces
    # parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    #
    # # 重写 ContextHandler
    # Handler = MovieHandler()
    # parser.setContentHandler(Handler)
    # parser.parse("movie.xml")
    domAnalyis()
