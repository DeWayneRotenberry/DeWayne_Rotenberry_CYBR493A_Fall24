#!/bin/bash

# Track time and crack the password for lost_data1
echo "Cracking lost_data1..."
(time while read password; do 
  gpg --batch --passphrase "$password" -d lost_data1.gpg &>/dev/null && echo "Password for lost_data1: $password" && break 
done < password_list.txt) 2>&1 | tee lost_data1_time.txt

# Repeat similar steps for lost_data2 and lost_data3
