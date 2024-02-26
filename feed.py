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

linkPrefix = yamldata['link']

xmltree.SubElement(channelElement, 'title').text = yamldata['title']
xmltree.SubElement(channelElement, 'format').text = yamldata['format']
xmltree.SubElement(channelElement, 'subtitle').text = yamldata['subtitle']
xmltree.SubElement(channelElement, 'language').text = yamldata['language']
xmltree.SubElement(channelElement, 'itunes:author').text = yamldata['author']
xmltree.SubElement(channelElement, 'description').text = yamldata['description']
xmltree.SubElement(channelElement, 'itunes:image', {'href':linkPrefix + yamldata['image']}).text = yamldata['image']
xmltree.SubElement(channelElement, 'itunes:category', {'text': yamldata['category']}).text = yamldata['image']


for item in yamldata['item']:
    itemElement = xmltree.SubElement(channelElement,'item')
    xmltree.SubElement(itemElement,'title').text = item['title']
    xmltree.SubElement(itemElement,'itunes:author').text = yamldata['author']
    xmltree.SubElement(itemElement,'description').text = item['description']
    xmltree.SubElement(itemElement,'pubDate').text = item['published']
    xmltree.SubElement(itemElement,'file').text = item['file']
    xmltree.SubElement(itemElement,'itunes:duration').text = item['duration']
    xmltree.SubElement(itemElement,'length').text = item['length']


    enclosure = xmltree.SubElement(itemElement,'enclosure',{
        'url': linkPrefix + item['file'],
        'type': 'audio/mpeg',
        'length' : item['length']
    })




outputTree = xmltree.ElementTree(rssElement)
outputTree.write('podcast.xml',encoding='UTF-8',xml_declaration=True)

