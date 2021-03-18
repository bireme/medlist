from whoosh.qparser import QueryParser
from whoosh.searching import Results

from medlist import settings
import whoosh


def search(query, field="list", limit=None, filter_compare=None, sortedby='medicine', type=None):

	query = str(query)

	ix = whoosh.index.open_dir(settings.WHOOSH_INDEX)
	searcher = ix.searcher()

	parser = whoosh.qparser.QueryParser(field, ix.schema)
	myquery = parser.parse(query)

	if filter_compare:
		filter_compare = whoosh.query.Term("comparative_type", filter_compare)

	search = searcher.search(myquery, filter=filter_compare, limit=None, sortedby=sortedby)

	results = []
	for result in search:
		if type == 'docnum':
			results.append(result.docnum)
		else:
			current = {}
			for key,value in result.items():
				current[key] = value
			results.append(current)

	return results
