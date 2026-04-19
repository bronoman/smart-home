This is a brief description of the skill file which allows Hermes Agent to perform a comprehensive healthcheck on an openHAB smarthome server.

# Prerequisites
1. You have an openHAB server running
2. You have created an API Key in OpenHAB which Hermes will use

# Outline of the Hermes skill file
## 1. Metadata (lines 1-12)
   - Version 1.2.0
   - Tags: OpenHAB, Smart Home, Monitoring, Health Check, Diagnostics, Logging
   - Prerequisites: OPENHAB_BASE_URL, OPENHAB_USERNAME, OPENHAB_PASSWORD

## 2. Quick Health Check (lines 19-64)
   - Bash script for basic connectivity test

## 3. Detailed Health Checks (lines 66-549)
   - Section 1: Full System Health Status (Python)
   - Section 2: Monitor Specific Thing Status (Bash)
   - Section 3: Advanced Diagnostics (Python) - Main comprehensive script
     - 🪟 Fibaro Shutters Check
     - 🌐 Gateway Status (Zigbee, Z-Wave, MQTT, Modbus ...)
       - Excludes test Z-Wave nodes 019 & 014
     - 🔋 Battery Levels (critical, low, inaccessible)
     - 📴 Offline & Uninitialized Things
     - 📋 OpenHAB Log Viewer (10-sec observation to find critical / recurring errors)

## 4. Cron Job Template (lines 551-573)
   - Hourly monitoring setup

## 5. Troubleshooting Guide (lines 575-584)
   - Common issues and solutions

## 6. Key Endpoints Reference (lines 586-593)

## 7. Best Practices (lines 595-602)

## 8. Integration with Hermes (lines 604-606)
