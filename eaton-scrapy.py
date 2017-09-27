#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

import requests

import os

MAX_FILE_NAME = 120
DATE_FORMAT = 'en'  # Put 'fr' here if your dates fit the format '%d/%m/%Y'


# import xml.etree.ElementTree as ET

weebly = "https://eatonbatsonboatbuilding.wordpress.com"

class WeeblyScraper():

    def scrape(self, pages):

        images = ["https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/jean-and-anna-layout-the-rudder1.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/jean-and-anna-w-rudder1.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/shaft-in-forge.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/hot-bronze.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/bending-the-bronze.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/hinges.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/rudder-mounted.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/the-wheel.jpg", "https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/steering.jpg"]
        for i in images:
            self.download_image(i)
        # output = '<html><head><link rel="stylesheet" type="text/css" href="../styles.css"></head><body>'

        # for post_url in pages:
        #     url = urlopen(post_url)
        #     soup = BeautifulSoup(url.read(), 'html.parser')

        #     title = soup.findAll('title')
        #     title = title[0].get_text().encode('utf-8', 'ignore')

        #     print(title)

        #     date = soup.findAll('div', {'id': 'single-date'})

        #     if date:

        #         date = date[0].get_text().encode('utf-8', 'ignore').strip()
        #         date = datetime.datetime.strptime(date.decode('utf-8'), '%d/%m/%Y' if DATE_FORMAT == 'fr' else '%B %d, %Y').strftime('%Y-%m-%d')
        #     else:
        #         date = "page"

        #     for i in soup.find('div', {'id': 'content'}).findAll('img'):
        #         i['src'] = '../images/' + self.download_image(i['src']) 

        #         i.attrs = {key:value for key,value in i.attrs.items() 
        #                          if key in ['src', 'width', 'height']}

        #     content = soup.findAll('div', {'id': 'content'})
        #     content = content[0].prettify(formatter='html')

        #     # download_image
        #     # 


        #     url = post_url.replace(weebly, '')
                
        #     if url:
        #         filename = url.split('/')[-2]
        #     else: 
        #         filename = 'homepage'

        #     print("... writing " + date + '-' + filename + '.html')
        #     post_md = open('content/' + date + '-' + filename + '.html', 'w')
        #     post_md.write(content)
        #     post_md.close()

        #     output += content

        # output += "</body></html>"

        # print("... writing index.html")
        # post_md = open('content/index.html', 'w')
        # post_md.write(output)
        # post_md.close()


    def download_image(self, image_url):
        # https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0245.jpg
        image_arr = image_url.split('?')
        if image_arr:
            image_url = image_arr[0]   

        name = image_url.split('/')[-1]   


        if os.path.exists('images/' + name):
            print(" ... exists: " + image_url + " as " + name)
            return name
            
        print(" ... saving " + image_url + " as " + name)

        img_data = requests.get(image_url).content
        with open('images/' + name, 'wb') as handler:
            handler.write(img_data)

        return name




if __name__ == '__main__':

    data = """
    <urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2013/12/02/the-un-launch-party/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0228.jpg</image:loc><image:title>IMG_0228</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/fullboat.jpg</image:loc><image:title>Full+boat</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/clamps.jpg</image:loc><image:title>Clamps</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/workbench2.jpg</image:loc><image:title>Workbench+2</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0245.jpg</image:loc><image:title>IMG_0245</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0244.jpg</image:loc><image:title>IMG_0244</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0242.jpg</image:loc><image:title>IMG_0242</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0241.jpg</image:loc><image:title>IMG_0241</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0239.jpg</image:loc><image:title>IMG_0239</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/12/img_0238.jpg</image:loc><image:title>IMG_0238</image:title></image:image><lastmod>2013-12-14T01:53:09+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2013/07/16/summer-2013/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/cabin-top.jpg</image:loc><image:title>cabin top</image:title><image:caption>Deckhouse beams</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/mii-bob-going-under-after-deck.jpg</image:loc><image:title>MII Bob going under after deck</image:title><image:caption>Bob goes under the deck.</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/p1020353.jpg</image:loc><image:title>P1020353</image:title><image:caption>Wendy lays down adhesive. </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/p1020349.jpg</image:loc><image:title>P1020349</image:title><image:caption>Bulwark install.</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/mii-jonah-setting-cabin-frames.jpg</image:loc><image:title>MII Jonah setting cabin frames</image:title><image:caption>Deckhouse framing.</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/mii-cabin-looking-aft.jpg</image:loc><image:title>MII cabin looking aft</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/mii-samson-post-and-bowsprite.jpg</image:loc><image:title>MII Samson post and bowsprite</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/mii-dry-fit-forward-bulwork.jpg</image:loc><image:title>MII dry fit forward bulwork</image:title><image:caption>Starboard bulwark.</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/paintedboat-s2.jpg</image:loc><image:title>paintedboat-s</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2013/07/paintedboat-s1.jpg</image:loc><image:title>paintedboat-s</image:title></image:image><lastmod>2013-12-02T19:44:08+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2013/03/04/httpwww-bbc-co-uknewsmagazine-21596072/</loc><mobile:mobile/><lastmod>2013-03-09T00:02:42+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2013/02/14/portlights/</loc><mobile:mobile/><lastmod>2013-02-14T18:58:04+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2012/12/04/and-we-built-the-deck-too/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2012/12/xynole.jpg</image:loc><image:title>xynole</image:title><image:caption>Draping the fabric. </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2012/12/2nd-layer-at-the-stern.jpg</image:loc><image:title>2nd layer at the stern</image:title><image:caption>Wendy at the stern working on the first layer.</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2012/12/cleanup-below1.jpg</image:loc><image:title>cleanup below1</image:title><image:caption>Bob and Stacy clean up below.</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2012/12/installing-2nd-layer.jpg</image:loc><image:title>installing 2nd layer</image:title><image:caption>Jonah and Stacy work on the second layer of plywood at the bow. </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2012/12/prepping-deck-panel.jpg</image:loc><image:title>Prepping Deck Panel</image:title><image:caption>Prepping the deck panels for installation.</image:caption></image:image><lastmod>2013-02-14T18:22:15+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2012/12/04/kickstarter-victory/</loc><mobile:mobile/><lastmod>2012-12-04T01:18:45+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2012/10/13/kickstarter/</loc><mobile:mobile/><lastmod>2012-11-03T14:08:44+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2012/09/05/engine-install/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2012/09/img_9625.jpg</image:loc><image:title>Refurbished Pathfinder 55</image:title><image:caption>Refurbished Pathfinder 55</image:caption></image:image><lastmod>2013-07-16T17:42:51+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2012/09/29/disaster/</loc><mobile:mobile/><lastmod>2012-09-29T21:15:10+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2010/12/19/the-rudder/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/the-wheel.jpg</image:loc><image:title>OLYMPUS DIGITAL CAMERA</image:title><image:caption>the wheel</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/steering.jpg</image:loc><image:title>OLYMPUS DIGITAL CAMERA</image:title><image:caption>steering</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/shaft-in-forge.jpg</image:loc><image:title>shaft in forge</image:title><image:caption>heating up the bronze</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/rudder-mounted.jpg</image:loc><image:title>OLYMPUS DIGITAL CAMERA</image:title><image:caption>rudder hung</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/jean-and-anna-w-rudder1.jpg</image:loc><image:title>OLYMPUS DIGITAL CAMERA</image:title><image:caption>Anna and Jean with the rough cut rudder</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/jean-and-anna-layout-the-rudder1.jpg</image:loc><image:title>OLYMPUS DIGITAL CAMERA</image:title><image:caption>Anna and Jean layout the rudder onto the blank</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/hot-bronze.jpg</image:loc><image:title>hot bronze</image:title><image:caption>red hot bronze</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/hinges.jpg</image:loc><image:title>hinges</image:title><image:caption>bronze hinges are mounted onto the stern post with a 3/4" rod keeping the alignment</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/bending-the-bronze.jpg</image:loc><image:title>bending the bronze</image:title><image:caption>bending the bronze on the layout table</image:caption></image:image><lastmod>2011-01-14T10:45:53+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2008/08/20/keel-casting/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/tegolin-jeze.jpg</image:loc><image:title>tegolin-je,ze</image:title><image:caption>Jonah and Zach pull off the bow</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/tegolin-je02.jpg</image:loc><image:title>tegolin-je02</image:title><image:caption>scrap into the truck</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/tegolin03.jpg</image:loc><image:title>tegolin03</image:title><image:caption>the Tegolin</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/tegolin02.jpg</image:loc><image:title>tegolin02</image:title><image:caption>The rubble, with our lead in the middle</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/tegolin01.jpg</image:loc><image:title>tegolin01</image:title><image:caption>the stern comes off</image:caption></image:image><lastmod>2013-10-15T14:33:00+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2008/10/20/casting-the-keel/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/12/2009-ballast-keel-attached.jpg</image:loc><image:title>ballast keel in place</image:title><image:caption>The ballast keel bolted in place</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/dadcameraupload24dec08-019.jpg</image:loc><image:title>DadCameraUpload24dec08 019</image:title><image:caption>clearing the mold off of the lead</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/mold1.jpg</image:loc><image:title>mold</image:title><image:caption>the mold before the "sandbox" was built around it</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/leadtotub1.jpg</image:loc><image:title>leadtotub</image:title><image:caption>Alice, Jonah and Wendy move a large chunk of Tegolin lead into the crucible while Kate mans the hoist</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/keepcast-pour41.jpg</image:loc><image:title>keepcast-pour4</image:title><image:caption>molten lead flows into the mold</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/keepcast-pour31.jpg</image:loc><image:title>keepcast-pour3</image:title><image:caption>the mold is almost full</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/keepcast-pour21.jpg</image:loc><image:title>keepcast-pour2</image:title><image:caption>pouring lead</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/keepcast-burncrew1.jpg</image:loc><image:title>keepcast-burncrew</image:title><image:caption>the burn crew</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/keepcast-burn51.jpg</image:loc><image:title>keepcast-burn5</image:title><image:caption>starting the fires</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/keepcast-burn41.jpg</image:loc><image:title>keepcast-burn4</image:title><image:caption>melting lead</image:caption></image:image><lastmod>2010-09-20T16:51:39+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2008/04/20/hello-world/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/flip-rigging-er.jpg</image:loc><image:title>flip-rigging-er</image:title><image:caption>the hull before flipping</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/flip-pulling-jbe.jpg</image:loc><image:title>flip-pulling-jbe</image:title><image:caption>Jonah pulls</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/flip-onkeel.jpg</image:loc><image:title>flip-onkeel</image:title><image:caption>resting safely on her side</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/flip-done-jbeaahmger.jpg</image:loc><image:title>flip-done-jbe,aah,mg,er</image:title><image:caption>a beer on the "deck." may she never capsize again.</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/flip-blocks-jbe.jpg</image:loc><image:title>flip-blocks-jbe</image:title><image:caption>block and tackle at the keel</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/flip-45deg-mg.jpg</image:loc><image:title>flip-45deg-mg</image:title><image:caption>45 degrees</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/flip-15deg-mg.jpg</image:loc><image:title>flip-15deg-mg</image:title></image:image><lastmod>2013-07-31T16:10:07+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2008/08/05/framing-the-deck/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2008/08/010.jpg</image:loc><image:title>010</image:title><image:caption>framing at the bow, with a hatch opening framed out</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/misc-upload-24dec08-054.jpg</image:loc><image:title>Misc Upload 24dec08 054</image:title><image:caption>main cabin carlin</image:caption></image:image><lastmod>2010-10-26T21:30:46+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/2008/07/01/interior-fairing/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110035.jpg</image:loc><image:title>p6110035</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110027.jpg</image:loc><image:title>p6110027</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110020.jpg</image:loc><image:title>p6110020</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110018.jpg</image:loc><image:title>p6110018</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110017.jpg</image:loc><image:title>p6110017</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110016.jpg</image:loc><image:title>p6110016</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110013.jpg</image:loc><image:title>p6110013</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110010.jpg</image:loc><image:title>p6110010</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110009.jpg</image:loc><image:title>p6110009</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/p6110008.jpg</image:loc><image:title>p6110008</image:title></image:image><lastmod>2010-01-05T01:39:25+00:00</lastmod><changefreq>monthly</changefreq></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/jig/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/move-je-movingbbone-1-s.jpg</image:loc><image:title>move-je-movingbbone-1-S</image:title><image:caption>moving the assembled backbone to the flat bed</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/bbone-loweringkeel-s.jpg</image:loc><image:title>bbone-loweringkeel-S</image:title><image:caption>lowering the backbone into the molds</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/bbone-frontview-s.jpg</image:loc><image:title>bbone-frontview-S</image:title><image:caption>the jig with bilge stringers installed</image:caption></image:image><lastmod>2012-09-29T20:47:47+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/loft/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/lofting-jebe2-s.jpg</image:loc><image:title>lofting-je&amp;be2-S</image:title><image:caption>lofting the shear</image:caption></image:image><lastmod>2010-01-05T01:24:30+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/molds/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/molds-5-s1.jpg</image:loc><image:title>molds-5-S</image:title><image:caption>The No.5 Mold Awaiting the Lower Spall </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/molds-1-s2.jpg</image:loc><image:title>molds-1-S</image:title><image:caption>Marking a board at station No. 9. Note that pointers hold batten at 1" off lofting floor. </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/molds-1-s1.jpg</image:loc><image:title>molds-1-S</image:title><image:caption>Marking a board at station No. 9. Note that pointers hold batten at 1" off lofting floor. </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/molds-1-s.jpg</image:loc><image:title>molds-1-S</image:title><image:caption>Marking a board at station No. 9. Note that pointers hold batten at 1" off lofting floor. </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/molds-jerefbwb-7.jpg</image:loc><image:title>molds-je,re,fb,wb-7</image:title><image:caption>Jonah, Bob, Fred and Winifred and half of No. 7</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/molds-5-s.jpg</image:loc><image:title>molds-5-S</image:title><image:caption>The No.5 Mold Awaiting the Lower Spall </image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/molds-je-marking-board-s.jpg</image:loc><image:title>molds-je-marking board-S</image:title><image:caption>Jonah transfers the No. 7 Station line to a board </image:caption></image:image><lastmod>2010-01-05T01:19:29+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/preparation/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/model-iso-s2.jpg</image:loc><image:title>model-iso-S</image:title><image:caption>a strip planking on foam core mold model</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/model-iso-s1.jpg</image:loc><image:title>MII model - scrap pine and foam board</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/model-iso-s.jpg</image:loc><image:title>MII Model - scrap pine on foam board</image:title></image:image><lastmod>2010-10-28T01:30:17+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/planking/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-vernloverde-knotching.jpg</image:loc><image:title>planking-vernloverde-knotching</image:title><image:caption>Vern cuts weekholes into frames</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-transombevel.jpg</image:loc><image:title>planking-transombevel</image:title><image:caption>the transom is notched to recieve the planking</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-tent.jpg</image:loc><image:title>planking-tent</image:title><image:caption>almost done</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-resaw-s.jpg</image:loc><image:title>planking-resaw-S</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-kere-framebevel.jpg</image:loc><image:title>planking-ke,re-framebevel</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-je-rabbit2-s.jpg</image:loc><image:title>planking-je-rabbit2-S</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-je-garboard.jpg</image:loc><image:title>planking-je-garboard</image:title><image:caption>clamping down the garboard strake</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-je-clampinggarboard-s.jpg</image:loc><image:title>planking-je-clampinggarboard-S</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-jere-meeting-s.jpg</image:loc><image:title>planking-je,re-meeting-S</image:title></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/planking-jere-climbjig.jpg</image:loc><image:title>planking-je,re-climbjig</image:title></image:image><lastmod>2013-03-04T03:20:08+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/backbone/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/lamtest-press-s.jpg</image:loc><image:title>lamtest-press-S</image:title><image:caption>testing a frame sample</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/roofcollapse-s.jpg</image:loc><image:title>roofcollapse-S</image:title><image:caption>A girder fails...</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/stem-ze-bandsaw-s.jpg</image:loc><image:title>stem-ze-bandsaw-S</image:title><image:caption>Zach cutting out part of the stem</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/bbone-dryfit-05-06-06-450.jpg</image:loc><image:title>bbone-dryfit-(05-06-06)-450</image:title><image:caption>dry run of the backbone assembly</image:caption></image:image><lastmod>2010-01-05T01:09:30+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/frames/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/frames.jpg</image:loc><image:title>frames</image:title><image:caption>finished frames waiting final installation</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2010/01/jig3.jpg</image:loc><image:title>jig3</image:title><image:caption>the completed frames on the jig</image:caption></image:image><lastmod>2010-01-04T23:16:11+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com/about/</loc><mobile:mobile/><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/zachinsloop1.jpg</image:loc><image:title>zachinsloop</image:title><image:caption>Zach in a a Freindship Sloop model</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/wendyanne-m1.jpg</image:loc><image:title>wendyanne-M</image:title><image:caption>the Wendy Anne, our second boat</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/zachinsloop.jpg</image:loc><image:title>zachinsloop</image:title><image:caption>Zach in a Friendship Sloop model</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/wendyanne-m.jpg</image:loc><image:title>wendyanne-M</image:title><image:caption>the Wendy Anne, our second boat</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/malabarsailplan-s1.jpg</image:loc><image:title>malabarsailplan-S</image:title><image:caption>the Malabar II sailplan</image:caption></image:image><image:image><image:loc>https://eatonbatsonboatbuilding.files.wordpress.com/2009/12/malabarsailplan-s.jpg</image:loc><image:title>malabarsailplan-S</image:title><image:caption>the Malabar II sailplan</image:caption></image:image><lastmod>2013-08-24T06:19:17+00:00</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url><url><loc>https://eatonbatsonboatbuilding.wordpress.com</loc><changefreq>daily</changefreq><priority>1.0</priority><lastmod>2013-12-14T01:53:09+00:00</lastmod></url></urlset>
    """

    # tree = ET.fromstring(data) 

    # print([el for el in tree.findall('.//loc')])
    # 
    soup = BeautifulSoup(data, 'lxml')

    pages = [t.text for t in soup.find_all('loc')]

    WeeblyScraper().scrape(pages[::-1])

    sys.exit(0)
