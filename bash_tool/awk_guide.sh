#!/usr/bin/env bash

# 求第四列的和
cat xx.txt | grep  "xxx" | awk -F '|' '{sum += $4};END{ print sum }'