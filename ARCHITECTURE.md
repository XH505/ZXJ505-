# Za-System Architecture

## Overview
Za-System is a modular, production-ready platform for integrated media generation, streaming, and automation. It follows a service-oriented architecture (SOA) with autonomous, loosely-coupled services.

## Core Components

### 1. Core Layer (`core/`)
- **logger.py**: Unified logging system
  - Centralized log file management
  - Service-specific log streams
  - Configurable log levels

- **broker.py**: Message broker for inter-service communication
  - Redis-backed pub/sub (with memory fallback)
  - Async message handling
  - Thread-safe operations

- **service_base.py**: Base class for all services
  - Graceful shutdown handling
  - Error recovery loops
  - Signal management

### 2. Services Layer (`services/`)

#### Za-Brain (`za-brain/`)
- Terminal shell interface
- Command execution
- System control hub

#### Za-WhatsBridge (`za-whatsbridge/`)
- Messaging bridge
- Multi-platform notification support
- Message queue management

#### RTMP Streamer (`rtmp-streamer/`)
- Real-time media streaming
- FFmpeg integration
- Stream endpoint management

#### Logger Monitor (`logger-monitor/`)
- System health monitoring
- Log aggregation
- Performance metrics

#### File Manager (`file-manager/`)
- Directory structure management
- File organization
- Quota management

### 3. Daemon Layer (`daemon/`)
- **service_manager.py**: Orchestrates all services
  - Auto-start on system boot
  - Automatic restart on failure
  - Service health monitoring
  - Graceful shutdown

### 4. Configuration Layer (`config/`)
- **system.yaml**: Centralized configuration
  - Service settings
  - Logging configuration
  - Security parameters
  - Broker settings

## Data Flow

```
User Input
    ↓
Za-Brain (CLI/Shell)
    ↓
Message Broker (Redis/Memory)
    ↓
Services (Za-WhatsBridge, RTMP, etc.)
    ↓
Output/Logs/Streams
    ↓
Logger Monitor (Aggregation)
```

## Communication Patterns

### 1. Pub/Sub (Message Broker)
Services publish events to channels:
- `messages` - Message events
- `notifications` - System notifications
- `control` - Control commands
- Custom channels per service

### 2. Direct Logging
All services log to unified system:
- Log files: `logs/{service_name}.log`
- Real-time monitoring via logger-monitor
- Configurable retention policies

### 3. Shared Storage
- Media files: `media/`
- Configuration files: `config/`
- Log aggregation: `logs/`

## Service Lifecycle

```
┌─────────────────────────────────────────┐
│  Service Manager (daemon/service_manager.py)
└─────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────┐
│  Start All Services                      │
│  (from services/ directory)              │
└─────────────────────────────────────────┘
          ↓
     For Each Service:
          ↓
┌─────────────────────────────────────────┐
│  1. Load Config                          │
│  2. Initialize BaseService               │
│  3. Register Signal Handlers             │
│  4. Enter execute() Loop                 │
└─────────────────────────────────────────┘
          ↓
     Continuous Monitoring:
          ↓
    ┌─────────────────┐
    │ Service Running?│
    └─────────────────┘
      ↙ Yes      ↘ No
   Continue    Restart
```

## Error Handling & Recovery

1. **Service Crash**: Service Manager detects and restarts
2. **Message Broker Unavailable**: Falls back to in-memory queue
3. **Log File Issues**: Automatic directory creation
4. **Signal Handling**: Graceful shutdown on SIGTERM/SIGINT

## Scalability

- **Horizontal**: Add new services in `services/` directory
- **Vertical**: Increase resource allocation
- **Distributed**: Redis broker supports multiple instances
- **Load Balancing**: External LB in front of services

## Security Considerations

1. JWT authentication (configurable)
2. CORS configuration
3. Signal validation
4. File access control
5. Log sanitization

## Deployment

### Local Development
```bash
source venv/bin/activate
python3 main.py
```

### Docker
```bash
docker-compose up -d
```

### Production
- Use systemd service files
- Configure log rotation
- Set up monitoring/alerting
- Use environment-specific configs
- Enable authentication

## Future Enhancements

1. Kubernetes orchestration
2. Distributed tracing
3. Advanced monitoring dashboard
4. ML-based anomaly detection
5. Multi-region deployment
6. Service mesh integration