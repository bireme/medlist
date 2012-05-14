from whoosh.qparser import QueryParser
from whoosh.searching import Results
import whoosh
import settings


def search(query, field="list", limit=None, sortedby='medicine', type=None):

	query = unicode(query)

	ix = whoosh.index.open_dir(settings.WHOOSH_INDEX)
	searcher = ix.searcher()

	parser = whoosh.qparser.QueryParser(field, ix.schema)
	myquery = parser.parse(query)
	
	search = searcher.search(myquery, limit=None, sortedby=sortedby)

	results = []
	for result in search:
		if type == 'docnum':
			results.append(result.docnum)
		else:
			results.append({key: value for key,value in result.items()})

	return results