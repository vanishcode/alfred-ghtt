#!/usr/bin/python
# -  *  - coding:UTF-8 -  *  -
import spider

def main():
    query = u'{query}'.strip()

    if query in [u'hot', u'new']:
    	spider.index(query)

    else:
        spider.plate(query)

if __name__ == "__main__":
    main()
