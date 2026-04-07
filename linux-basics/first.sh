#!/bin/bash
echo "== System Info ==="
echo "Hostname: $(hostname)"
echo "Date: $(date)"
echo "Uptime: $(uptime -p)"
echo "Disk usage:"
df -h
