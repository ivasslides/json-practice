#!/bin/bash

file="aviation.json"

jq -r '.[] | .receiptTime' "$file" | head -n 6
