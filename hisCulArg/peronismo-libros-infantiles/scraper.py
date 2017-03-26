# -*- coding: utf-8 -*-

'''
The purpose of this module is to download all the pages of Evita and Alelí,
children's schoolbooks written during the Peronism in Argentina from:
http://www.taringa.net/posts/imagenes/15396831/Evita-el-libro-de-primer-grado-completo.html
http://www.taringa.net/posts/imagenes/15495788/Peronismo-infantil-Libro-de-2do-grado.html
'''

import sys
import requests
from pattern import web

'''
for a given webpage scrape the sources of all images
(all src within img tags)
'''
def get_img_urls(url):
    page = requests.get(url).text.encode('UTF-8')
    dom = web.Element(page)
    imgs = dom('img')
    urls = []

    for img in imgs:
        try:
             urls.append(img.attrs['src'])
        except:
            print ("No src url available")

    return urls

'''
for an image url download and write image to file
'''
def write_img(url, id_name):
    data = requests.get(url).content
    file_name = "%d.jpg" % id_name

    with open(file_name, "wb") as f:
        f.write(data)


'''
main
'''
def main():
    urls = get_img_urls("http://www.taringa.net/posts/imagenes/15396831/Evita-el-libro-de-primer-grado-completo.html")
    #urls = get_img_urls("http://www.taringa.net/posts/imagenes/15495788/Peronismo-infantil-Libro-de-2do-grado.html")
    for i,u in enumerate(urls):
        write_img(u, i)

if __name__ == '__main__':
    status = main()
    sys.exit(status)
