# Za-System 🚀

## Project Structure
The Za-System is organized in a modular fashion to facilitate ease of navigation and integration. The key components of the project are:

- **Mora**: The video generation module responsible for creating video assets dynamically.
- **Za-Brain**: A terminal shell that acts as the main control interface for the system.
- **Za-WhatsBridge**: A messaging component that allows for interactions across various messaging platforms.
- **RTMP Streaming**: This module handles real-time media streaming to broadcasting services.
- **Logging**: Provides detailed logging capabilities for monitoring and debugging.
- **Daemon Services**: Background services that ensure continual operation and management of the above components.

## Components
1. **Mora Video Generation**  
   - Supports various video formats and codecs.  
   - Features customizable templates for quick production-ready videos.

2. **Za-Brain Terminal Shell**  
   - Command-line interface to interact with the system.  
   - Supports script execution, real-time feedback, and monitoring.

3. **Za-WhatsBridge Messaging**  
   - Integrates with popular messaging platforms.  
   - Facilitates automated messaging and notification systems.

4. **RTMP Streaming**  
   - Capable of streaming to multiple platforms simultaneously.  
   - Supports adaptive bitrate streaming for optimal user experience.

5. **Logging**  
   - Centralized logging system capturing system events and errors.  
   - Configurable log levels (INFO, DEBUG, ERROR).

6. **Daemon Services**  
   - Automatically restarts services if they fail.  
   - Offers a web interface to monitor service health.

## Installation
To install Za-System, follow these steps:
1. Clone the repository:  
   `git clone https://github.com/XH505/ZXJ505-`
2. Navigate into the project directory:  
   `cd ZXJ505-`
3. Run the installation script:  
   `./install.sh`
   This script installs all necessary dependencies and configures the necessary environment variables.

## Usage Instructions
1. Start the Za-Brain terminal shell:  
   `./za-brain`
2. Generate a video using Mora:  
   `mora generate --template <template_name>`
3. Stream video via RTMP:  
   `rtmp-stream start --video <video_file>`
4. Send a message using Za-WhatsBridge:  
   `whatsapp send --message "Hello, World!"`
5. Monitor logs:  
   `tail -f /var/log/za-system.log`

## Contributing
Contributions are welcome. Please follow the repository's code style and add tests for new features. Use feature branches and open a pull request describing changes.

## License
Licensed under the Apache License 2.0. See LICENSE file in the repository for details.

## Contact
For support or questions open an issue or reach out via the Za-WhatsBridge channel.
