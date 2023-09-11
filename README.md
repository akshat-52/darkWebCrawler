# darkWebCrawler

## Abstract
Abstract
Dark web provides anonymity services as well as a perfect hide space for the illegal and criminal activities such as human trafficking, illegal information transactions, and drugs and firearms. Trying to build a tool to crawl the deep web using pre-existing open source libraries and modules and trying to use novel methods such as classifiers to get data more efficiently and accurately. At first the data is scraped from the URLs from Darkweb and based on that data URLs are listed out using various algorithms and the relevant data that is preprocessed and filtered is stored in a database.

## Introduction
The Dark web is a segment of the internet that provides encrypted online content that is not available on surface web, or regular search engines such as Google, Bing etc. The dark web can only be accessed with special privilege escalation or special browsers. <br>
The reason why it occupies over 70% of the WWW is the anonymity services that it provides to the users. When on the dark web, the user’s information is completely protected from the outside world. Since the encrypted online content is not indexed by conventional search engines, the information of any user who accesses the dark web is not stored. In other words, all users of the dark web are ‘anonymous’. <br>
In addition to playing a crucial role in ensuring the security of user information, the rise of technologies ensuring anonymity of users on the dark web has created the ideal environment for illicit and criminal activity such as leaking of illicit information and human trafficking etc. The structural complexity, and the weak legal constraints of the dark web have made it a new means of delivery for criminal activities. Consequently, in order to manage these criminals, dark web monitoring crawlers are designed to obtain and store information based on user activity and use it for data analysis. <br>
One such crawler is the TOR based web monitoring crawler.The Tor project forms the Tor network through relay nodes and various servers provided by volunteers around the world. The entire Tor network includes Onion Proxy (OP), OnionRouter (OR), directory servers, and various application servers. <br>
The proposed dark web crawler follows the principles of a general crawler combined with the keyword analysis algorithm, which is a modified version of the TF-IDF algorithm.It uses domain search modules and web crawling experiments for the analysis.

## Proposed Methodology
### High level design
Proposed TOR based Dark web monitoring crawler system is divided into three main parts
- Domain name Collection
- Web Page crawling and Storage
- Content Analysis and Display

### Scrapy framework Architecture
![image](https://github.com/akshat-52/darkWebCrawler/assets/76260302/162df76d-3f35-48a1-a4b3-15a1cf1a8edb)

### TOR Network Architecture
![image](https://github.com/akshat-52/darkWebCrawler/assets/76260302/9269aed4-a896-4724-98b5-ab4d8da51f3d)

