# Linux Log Analyzer

A Python-based security monitoring tool designed to analyze Linux SSH authentication logs, identify suspicious login activity, and detect potential brute-force attacks.

This project was developed as part of my independent study of Linux system administration, Python programming, and cybersecurity. It demonstrates how authentication logs can be processed to identify security threats and provide useful information for system administrators.

## 1. Project Overview

Linux systems generate authentication logs that record login attempts, including successful and failed SSH connections.

Manually reviewing these logs can be time-consuming, particularly when investigating repeated authentication failures or suspicious access attempts.

Linux Log Analyzer processes authentication logs to identify patterns that may indicate unauthorized access attempts.

The project focuses on:

* Analyzing SSH authentication logs.
* Identifying failed and successful login attempts.
* Detecting invalid username attempts.
* Tracking authentication activity by IP address and username.
* Detecting potential SSH brute-force attacks.
* Identifying successful logins following suspicious authentication activity.

## 2. Technologies Used

| Technology   | Purpose                                     |
| ------------ | ------------------------------------------- |
| Python 3     | Log parsing and security analysis           |
| Linux        | Development and testing environment         |
| Rocky Linux  | Linux operating system used for development |
| OpenSSH      | Source of SSH authentication logs           |
| Git & GitHub | Version control and project management      |
| VirtualBox   | Virtualized Linux testing environment       |

The project uses Python's standard library for log processing, timestamp handling, and authentication event analysis.

## 3. Features

### SSH Authentication Log Analysis

Processes Linux SSH authentication logs and extracts relevant information, including:

* Source IP addresses
* Usernames
* Authentication timestamps
* Failed login attempts
* Successful login attempts
* Invalid user attempts

### Failed Login Tracking

Counts failed SSH authentication attempts and groups them by IP address and username.

This helps identify which IP addresses are responsible for repeated authentication failures and which user accounts are being targeted.

### Invalid User Detection

Identifies login attempts involving usernames that do not exist on the system.

Repeated attempts involving invalid usernames may indicate automated username enumeration or brute-force activity.

### Brute-Force Attack Detection

Analyzes failed login timestamps to identify multiple authentication failures occurring within a defined time window.

The detection logic uses a sliding-window approach to identify repeated failed login attempts from the same source IP address.

### Successful Login Correlation

Tracks successful SSH authentication events and compares them with previously detected suspicious login activity.

This helps identify successful logins that occur after repeated authentication failures from the same IP address.

A successful login following suspicious activity is an event that warrants further investigation, but it does not automatically confirm that an account has been compromised.

## 4. How It Works

The analyzer follows a log-processing workflow:

1. Read SSH authentication logs.
2. Identify authentication events.
3. Extract IP addresses, usernames, and timestamps.
4. Count failed, successful, and invalid user login attempts.
5. Analyze failed login timestamps for potential brute-force activity.
6. Correlate successful logins with suspicious authentication activity.
7. Display the analysis results in the terminal.

## 5. Example Log Entries

The following examples illustrate the SSH authentication events analyzed by the project.

**Failed login:**

```text
Sep 07 10:15:21 server sshd[1234]: Failed password for root from 192.168.1.50 port 52231 ssh2
```

**Invalid user:**

```text
Sep 07 10:15:25 server sshd[1235]: Failed password for invalid user admin123 from 192.168.1.50 port 52232 ssh2
```

**Successful login:**

```text
Sep 07 10:16:02 server sshd[1236]: Accepted password for root from 192.168.1.50 port 52233 ssh2
```

## 6. Development Environment

The project is developed and tested in a virtualized Linux environment.

* Host environment: VirtualBox
* Guest operating system: Rocky Linux
* Programming language: Python 3.12
* Development tools: Linux terminal, Git, and GitHub

The virtualized environment allows authentication logs to be generated and analyzed without relying on production systems.

## 7. Security Considerations

This project is intended for educational purposes and defensive security monitoring.

Potential brute-force attacks are identified using authentication patterns rather than confirmed malicious intent.

Repeated login failures can also result from legitimate users entering incorrect credentials or automated services using outdated authentication information.

The analyzer's results should therefore be treated as indicators requiring further investigation.

## 8. Future Improvements

The following features are planned for future development:

* Implement the log analysis engine in Go to compare performance, readability, and maintainability with Python.
* Use Bash scripts to automate log collection and execution.
* Improve detection logic and reduce false positives.
* Add configurable detection thresholds and time windows.
* Support additional Linux authentication log formats.
* Introduce structured output formats for integration with external monitoring systems.
* Explore integration with security monitoring and visualization platforms such as Splunk.

## 9. Learning Objectives

This project provides practical experience in:

* Python programming and data structures.
* Linux system administration.
* SSH authentication and Linux logging.
* Timestamp processing and sliding-window algorithms.
* Security event correlation.
* Brute-force attack detection.
* Git-based version control.

The long-term objective is to develop a reusable security monitoring tool while improving my understanding of Linux infrastructure, automation, and cybersecurity.
