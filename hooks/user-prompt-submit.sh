#!/bin/bash
# DEPRECATED: replaced by hooks/inject_memory.py
# The settings-template.json now runs python3 hooks/inject_memory.py directly.
# This file is kept only as a pointer. Delete it if you prefer a clean directory.
exec python3 "$(dirname "$0")/inject_memory.py"
