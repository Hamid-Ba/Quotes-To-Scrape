import requests

class Blog :
    def __init__(self,url) :
        self.url = url

    def __repr__(self) -> str:
        return "Blog Class Can Return Content Of a Html Page"

    def download_page(self,fileName):
        blog_page = requests.get(self.url)
        with open(fileName,'w') as blog_html :
            blog_html.writelines(blog_page.text)

    def get_content_page(self):
        blog_page = requests.get(self.url)
        return blog_page.text