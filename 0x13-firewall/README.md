# Project: 0x13. Firewall

## Overview
This project focuses on configuring and managing a firewall using `ufw` (Uncomplicated Firewall) on a Linux server. The primary goal is to enhance network security by defining rules for incoming and outgoing traffic.

## What is a Firewall
A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. In this project, we utilize `ufw` to implement firewall rules and enhance the security of our servers.

## Warning
Containers on demand cannot be used for this project (Docker container limitation). It is crucial to exercise caution when configuring firewall rules to avoid unintended consequences.

## Table of Contents
1. [Tasks](#tasks)
   - [Task 0: Block all incoming traffic](#task-0-block-all-incoming-traffic)
   - [Task 1: Port Forwarding](#task-1-port-forwarding)

## Tasks

### Task 0: Block all incoming traffic
Let’s install the `ufw` firewall and set up a few rules on web-01.

**Requirements:**
- The requirements below must be applied to web-01.
- Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)

Task 1: Port Forwarding
Requirements:

Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.

