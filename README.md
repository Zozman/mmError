To Start:

`docker-compose up`

Error:

```
...
mindmeld_1  | Loading domain classifier
mindmeld_1  | Loading entity recognizer: domain='chat', intent='greeting'
mindmeld_1  | Loading entity recognizer: domain='assist', intent='is_live'
mindmeld_1  | No app configuration file found. Using default language and locale.
mindmeld_1  | No app configuration file found.
mindmeld_1  | No app configuration file found. Using default entity_resolution model configuration
mindmeld_1  | Loading role classifier: domain='assist', intent='is_live', entity_type='channel'
mindmeld_1  | error: Unable to connect to Elasticsearch: <urllib3.connection.HTTPConnection object at 0x7efe68869860>: Failed to establish a new connection: [Errno 111] Connection refused details: <urllib3.connection.HTTPConnection object at 0x7efe68869860>: Failed to establish a new connection: [Errno 111] Connection refused
mindmeld_1  | warning: Cannot connect to ES, so Entity Resolver is not loaded.
mindmeld_1  |  * Serving Flask app "mindmeld" (lazy loading)
mindmeld_1  |  * Environment: production
mindmeld_1  |    WARNING: This is a development server. Do not use it in a production deployment.
mindmeld_1  |    Use a production WSGI server instead.
mindmeld_1  |  * Debug mode: on
mindmeld_1  |  * Running on http://0.0.0.0:7150/ (Press CTRL+C to quit)
```
