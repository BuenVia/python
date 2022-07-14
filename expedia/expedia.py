import json

filename = 'python/expedia/readable_response.json'
with open(filename) as f:
    all_hits_data = json.load(f)

all_hits = all_hits_data['hits']

hits = []
for each_hit in all_hits:
    hit = each_hit['hits']
    hits.append(hit)

print(hits['hits'])


# readable_file = 'python/expedia/readable_response.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)