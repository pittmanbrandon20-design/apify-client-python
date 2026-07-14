import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "startUrls": [{"url": "https://example.com"}],
    "maxRequestsPerCrawl": 10,
    "pageFunction": """async function pageFunction(context) {
    const { request, log, jQuery } = context;
    log.info(`Processing ${request.url}`);
    return {
        url: request.url,
        title: jQuery('title').text(),
    };
}""",
}

run = client.actor("apify/web-scraper").call(run_input=run_input)

dataset_id = run.default_dataset_id
items = client.dataset(dataset_id).list_items().items

print(f"Run: {run.id} status={run.status} items={len(items)}")
for item in items[:3]:
    print(item)
