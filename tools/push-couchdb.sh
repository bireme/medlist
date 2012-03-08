# 1- url do couchdb/banco
# 2- arquivo json

curl -d @${2} -X POST ${1}/_bulk_docs -H"Content-type: application/json"
