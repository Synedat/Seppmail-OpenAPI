// Setting Authentication Header vom Environment
pm.request.headers.upsert(
    {
    key: "X-SM-API-TOKEN",
    value: pm.environment.get("X-SM-API-TOKEN")
    }
);
pm.request.headers.upsert(
    {
    key: "X-SM-API-SECRET",
    value: pm.environment.get("X-SM-API-SECRET")
    }
);

//Define baseurl Variable from environment Variables
let server = pm.environment.get("server");
let port = pm.environment.get("port");
let version = pm.environment.get("version");
let baseUrl = server + ":" + port + "/" + version

pm.collectionVariables.set("baseUrl",baseUrl)
