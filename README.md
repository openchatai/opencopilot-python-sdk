# OpenSource Python SDK for OpenCopilot

Welcome to the open-source Python SDK for OpenCopilot! This SDK is designed to simplify the integration of OpenCopilot into Python applications, making it easier for developers to interact with OpenCopilot services and features.

## Usage

Here's a simple example of how to use the SDK to interact with OpenCopilot:

``` python
from client import OpenCopilotApi

open_copilot_client = OpenCopilotApi(
    base_url='http://localhost:xxx',
)

my_copilots = open_copilot_client.copilot.get_all()
```

## Documentation

For detailed information on how to use this SDK and a complete list of available functions and parameters, please refer to our [official documentation](https://docs.opencopilot.so/sdk/python/init-client).

## Contributing

We welcome contributions from the open-source community to improve and enhance this SDK.

---

**Note:** This SDK was generated with the help of a code generation tool. You can find the tool that helped generate this SDK at [Fern](https://buildwithfern.com). We would like to express our gratitude to the creators of Fern for their invaluable assistance in simplifying the development of this SDK.

If you have any questions, encounter issues, or want to contribute, please feel free to reach out to us on our [GitHub repository](https://github.com/openchatai/opencopilot-python-sdk).
