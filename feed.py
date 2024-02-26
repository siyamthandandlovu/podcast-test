import yaml
import xml.etree.ElementTree as xmltree

with open('feed.yaml','r') as file:
    yamldata = yaml.safe_load(file)
    rssElement = xmltree.Element('rss',
    {
    'version' : '2.0',
    'xmlns:itunes' : 'http://www.itunes.com/dtds/podcast-1.0.dtd', 
    'xmlns:content' : 'http://purl.org/rss/1.0/modules/content/'   
    })

channelElement = xmltree.SubElement(rssElement,'channel')

xmltree.SubElement(channelElement, 'title').text = yamldata['title']
xmltree.SubElement(channelElement, 'link').text = yamldata['link']
xmltree.SubElement(channelElement, 'lang').text = yamldata['lang']
xmltree.SubElement(channelElement, 'title').text = yamldata['title']
xmltree.SubElement(channelElement, 'title').text = yamldata['title']
xmltree.SubElement(channelElement, 'title').text = yamldata['title']
xmltree.SubElement(channelElement, 'title').text = yamldata['title']
xmltree.SubElement(channelElement, 'title').text = yamldata['title']

outputTree = xmltree.ElementTree(rssElement)
outputTree.write('podcast.xml',encoding='UTF-8',xml_declaration=True)

