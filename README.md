# loadstone
Simple library for building and manipulating cloud infrastructure.  I use this library as a starting point for other projects that require building public cloud infrax via API/SDK tools.  The underlying functions are abstracted from their respective libraries as much as possible for simple actions i.e. to create a IaaS VM instance for provider _X_, call the matching function array element: `createVM[X](params)`

![logo](island.jpg)

_TODO:_ pretty much everything

_Goals:_
- Get working with AWS, Azure, GCP, and OCI
- Create basic functions to provision IaaS services
- Enable peering within and between each provider
- Integrate with a visual editor (i.e. produce a single YAML/JSON ingest it here)
- Get some more advanced features working (like importing serverless compute code)
