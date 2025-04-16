.py# Patient Monitoring System

This project demonstrates the Model Context Protocol (MCP) pattern in a healthcare setting. The system monitors patient vital signs and generates alerts when readings are outside normal ranges.

## Project Structure

The project follows the Model Context Protocol pattern:

- **Protocols**: Define interfaces for patient data operations, alerts, and storage
- **Models**: Implement core business logic for patient monitoring
- **Contexts**: Provide concrete implementations for data storage, patient data operations, and alert systems

## Components

- `protocols.py`: Defines the interfaces for the system
- `models.py`: Contains the core business logic and data structures
- `contexts.py`: Implements the concrete contexts
- `main.py`: Demonstrates usage of the system

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.main import main
main()
```

## Key Features

- Vital signs monitoring
- Alert generation for abnormal readings
- Separation of concerns using MCP
- Extensible design for different storage and alert mechanisms
