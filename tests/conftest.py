import os
import sys

# 1. Find the absolute path of the 'tests' directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level to the absolute root of the 'Quan-6G' repository
root_dir = os.path.abspath(os.path.join(current_dir, ".."))

# 3. Force-inject the root repository path into Python's search paths
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
