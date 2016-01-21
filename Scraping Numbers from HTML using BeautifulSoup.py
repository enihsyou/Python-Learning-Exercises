


# html = """<html><head>
# <title>Welcome to the comments assignment from www.pythonlearn.com</title>
# </head>
# <body>
# <h1>This file contains the actual data for your assignment - good luck!</h1>

# <table border="2">
# <tbody><tr>
# <td>Name</td><td>Comments</td>
# </tr>
# <tr><td>Wiktor</td><td><span class="comments">98</span></td></tr>
# <tr><td>Jackie</td><td><span class="comments">97</span></td></tr>
# <tr><td>Stella</td><td><span class="comments">95</span></td></tr>
# <tr><td>Malika</td><td><span class="comments">94</span></td></tr>
# <tr><td>Keeva</td><td><span class="comments">90</span></td></tr>
# <tr><td>Lexie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Clayton</td><td><span class="comments">87</span></td></tr>
# <tr><td>Mea</td><td><span class="comments">87</span></td></tr>
# <tr><td>Lotte</td><td><span class="comments">87</span></td></tr>
# <tr><td>Bob</td><td><span class="comments">82</span></td></tr>
# <tr><td>Josh</td><td><span class="comments">82</span></td></tr>
# <tr><td>Ege</td><td><span class="comments">82</span></td></tr>
# <tr><td>Zalfa</td><td><span class="comments">81</span></td></tr>
# <tr><td>Zahraa</td><td><span class="comments">80</span></td></tr>
# <tr><td>Clare</td><td><span class="comments">77</span></td></tr>
# <tr><td>Anaya</td><td><span class="comments">76</span></td></tr>
# <tr><td>Kit</td><td><span class="comments">73</span></td></tr>
# <tr><td>Oluwabukunmi</td><td><span class="comments">68</span></td></tr>
# <tr><td>Khaia</td><td><span class="comments">66</span></td></tr>
# <tr><td>Jordan</td><td><span class="comments">65</span></td></tr>
# <tr><td>Ajayraj</td><td><span class="comments">61</span></td></tr>
# <tr><td>Oriane</td><td><span class="comments">61</span></td></tr>
# <tr><td>Caidy</td><td><span class="comments">58</span></td></tr>
# <tr><td>Nihal</td><td><span class="comments">58</span></td></tr>
# <tr><td>Cormac</td><td><span class="comments">55</span></td></tr>
# <tr><td>Kale</td><td><span class="comments">55</span></td></tr>
# <tr><td>Leighann</td><td><span class="comments">51</span></td></tr>
# <tr><td>Zoubaeir</td><td><span class="comments">51</span></td></tr>
# <tr><td>Insiya</td><td><span class="comments">50</span></td></tr>
# <tr><td>Caelan</td><td><span class="comments">50</span></td></tr>
# <tr><td>Mati</td><td><span class="comments">49</span></td></tr>
# <tr><td>Lauri</td><td><span class="comments">48</span></td></tr>
# <tr><td>Kasra</td><td><span class="comments">48</span></td></tr>
# <tr><td>Sajid</td><td><span class="comments">48</span></td></tr>
# <tr><td>Collette</td><td><span class="comments">44</span></td></tr>
# <tr><td>Devayani</td><td><span class="comments">42</span></td></tr>
# <tr><td>Tess</td><td><span class="comments">42</span></td></tr>
# <tr><td>Emmylou</td><td><span class="comments">38</span></td></tr>
# <tr><td>Calley</td><td><span class="comments">36</span></td></tr>
# <tr><td>Sahar</td><td><span class="comments">34</span></td></tr>
# <tr><td>Yusef</td><td><span class="comments">26</span></td></tr>
# <tr><td>Luic</td><td><span class="comments">25</span></td></tr>
# <tr><td>Konar</td><td><span class="comments">22</span></td></tr>
# <tr><td>Sasha</td><td><span class="comments">19</span></td></tr>
# <tr><td>JJ</td><td><span class="comments">11</span></td></tr>
# <tr><td>Joeddy</td><td><span class="comments">8</span></td></tr>
# <tr><td>Jannah</td><td><span class="comments">8</span></td></tr>
# <tr><td>Tian</td><td><span class="comments">8</span></td></tr>
# <tr><td>Ebow</td><td><span class="comments">4</span></td></tr>
# <tr><td>Neelam</td><td><span class="comments">3</span></td></tr>
# </tbody></table>


# <div class="wsx_fade" style="pointer-events: none;"></div><div class="wsx_scroll" style="display: block; opacity: 0; pointer-events: none; top: 0px; height: 1623px;"><div class="wsx_scroll_bar" style="opacity: 0.6; border-radius: 3px; width: 6px; left: 19px; background-color: rgb(66, 119, 0);"></div></div></body></html>"""

import urllib.request as ur
from bs4 import BeautifulSoup
url = input('Enter: ')
# url = "http://python-data.dr-chuck.net/comments_42.html"
# url = "http://python-data.dr-chuck.net/comments_202174.html"

html = ur.urlopen(url)

soup = BeautifulSoup(html, "html.parser")
tag = soup.find_all('span')
count = 0
for item in tag:
    num = int(item.string)
    count = count + num

print(count)