# Data Provider

A Python-based data provider application built with dependency injection and modular architecture. This project provides a flexible framework for data access and service communication with support for various data sources and external APIs.

## Features

- **Dependency Injection**: Built using `dependency-injector` for clean, testable architecture
- **Modular Design**: Organized into separate containers for different concerns (client, services, data providers, mappers)
- **HTTP Client**: Built-in service client for making HTTP requests to external APIs
- **Configuration Management**: YAML-based configuration with logging support
- **Type Safety**: Uses Python type hints for better code maintainability

## Project Structure

```
dataprovider/
├── app/
│   ├── client/              # HTTP client and communication logic
│   ├── configuration/       # Configuration management
│   ├── dataproviders/       # Data source implementations
│   ├── gateways/           # External service gateways
│   ├── mapper/             # Data mapping utilities
│   ├── models/             # Data models and service models
│   ├── services/           # Business logic services
│   └── containers.py       # Main dependency injection container
├── config.yml              # Application configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Prerequisites

- Python 3.13+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dataprovider
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The application uses `config.yml` for configuration. The default configuration includes:

- **Logging**: Console-based logging with configurable levels
- **Client Settings**: Base address and timeout configuration for HTTP requests

Example configuration:
```yaml
core:
  logging:
    version: 1
    formatters:
      formatter:
        format: "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
    handlers:
      console:
        class: "logging.StreamHandler"
        level: "INFO"
        formatter: "formatter"
        stream: "ext://sys.stderr"
    root:
      level: "INFO"
      handlers: ["console"]

client:
  settings:
    baseAddress: "http://localhost:8000"
    timeout: 30
```

## Usage

### Running the Application

```bash
python -m app
```

### Key Components

#### Service Client
The `ServiceClient` class provides HTTP communication capabilities:

```python
from app.client.communicator import ServiceClient
from app.models.servicemodels import Request, ServiceClientSettings

# Initialize client
settings = ServiceClientSettings("http://api.example.com", 30000)
client = ServiceClient(settings)

# Make requests
request = Request()
request.RequestModel = your_data
request.Headers = {"Content-Type": "application/json"}

response = client.POST("/api/endpoint", request)
```

#### Dependency Injection
The application uses dependency injection containers for managing dependencies:

```python
from app.containers import ApplicationContainer

# Initialize container
container = ApplicationContainer()
container.core.init_resources()
container.wire(modules=[__name__])

# Access services
service_client = container.Client.serviceClient()
```

## Development

### Adding New Data Providers
1. Create a new module in `app/dataproviders/`
2. Implement your data provider class
3. Register it in `app/dataproviders/containers.py`

### Adding New Services
1. Create service classes in `app/services/`
2. Register them in `app/services/containers.py`
3. Wire them in the main application container

### Configuration
- Modify `config.yml` for application settings
- Add new configuration sections as needed
- Update the configuration containers accordingly

## Dependencies

- `dependency-injector[yaml]`: Dependency injection framework with YAML support
- `discord.py`: Discord API wrapper (if Discord integration is needed)

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For questions or issues, please open an issue in the repository or contact the development team.