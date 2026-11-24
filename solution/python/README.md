# Python Socket Programming Laboratory (Experiment 17)

This directory contains standalone Python 3 socket implementations for transport and application layer protocols with zero external dependencies.

## Architecture

- **`servers.py`**: Unified entrypoint supporting interactive menu and command-line arguments.
- **`lab_root/`**: Document root directory for the HTTP and FTP servers containing `index.html`.

## Quick Start

### 1. Interactive CLI Mode
```bash
python3 servers.py
```

### 2. Direct Service Launch

```bash
# 1. Multi-Client TCP Chat Server (Port 5000)
python3 servers.py chat --port 5000

# 2. HTTP/1.1 Web Server (Port 8080)
python3 servers.py web --port 8080 --root lab_root

# 3. RFC 959 Interactive FTP Server (Port 2121)
python3 servers.py ftp --port 2121 --root lab_root
```

## Testing & Verification

- **Chat Client**: Connect multiple concurrent sessions via `nc 127.0.0.1 5000`
- **HTTP Client**: Test using `curl -i http://127.0.0.1:8080/index.html` or open in a web browser
- **FTP Client**: Connect with `nc 127.0.0.1 2121` and execute:
  ```text
  USER student
  PASS lab
  LIST
  RETR index.html
  QUIT
  ```
