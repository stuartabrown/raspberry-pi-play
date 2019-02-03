# import dateutil.parser
import untangle
# from datetime import datetime, timedelta
data = untangle.parse('sample.xml')
# book = data.book
# print (book)

# chapter = data.book.chapter
# print (chapter)

# print (data.book.chapter['id'])
# print (data.book.chapter[0].title.cdata.strip())
# print (data.book.chapter[1].title)

# title = data.book.chapter.title
# print (title)

COUNT = [0,1]
for TICK in COUNT:
  print(data.book.chapter[TICK])