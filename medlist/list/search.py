from whoosh.qparser import QueryParser
from whoosh import index
import settings


def search(query, field="*", limit=None, sortedby=None):

	query = unicode(query)
	
	ix = index.open_dir(settings.WHOOSH_INDEX)
	searcher = ix.searcher()

	parser = QueryParser(field, ix.schema)
	myquery = parser.parse(query)

	search = searcher.search(myquery, limit=None, sortedby=sortedby)

	results = []
	for result in search:
		results.append({key: value for key,value in result.items()})

	return results