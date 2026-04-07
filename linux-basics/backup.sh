#!/bin/bash
DATE=$(date +%Y-%m-%d)
BACKUP_DIR="/home/devops/backups"
SOURCE_DIR="/home/devops"
mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/backup-$DATE.tar.gz $SOURCE_DIR
find $BACKUP_DIR -name "backuo-*.tar.gz" -mtime +7 -delete
echo "Backup complete: backup-$DATE.tar.gz" >> $BACKUP_DIR/backup.log
