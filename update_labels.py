#!/usr/bin/env python3

# Note: requires pyyaml package.
import os, glob, json, yaml, time
from datetime import datetime
from os.path import exists

# Variables.
data_file = 'labels.json'
output_dir = '_label_pages'
front_matter_pre = '---\nlayout: label\n'
front_matter_post = '---\n'
run_date = datetime.today().strftime('%Y-%m-%d %H:%M:00')

# Check for labels.json and fail if missing.
if not exists(data_file):
  print('Data file not found; ensure', data_file, 'is present and retry.')
  quit()

# Import json.
with open(data_file) as f:
  data = json.load(f)

if not data:
  print('No labels found in data; check', data_file, 'and retry.')
  quit()

# Clear out previous output files.
old_files = glob.glob(output_dir + '/*')
for f in old_files:
  os.remove(f)

# Iterate over label definitions; remove specific fields
# and create yaml files with Jekyll front matter.
for label in data:

  # Remove certain fields due to licensing constraints.
  del label['chemigation']
  del label['pollinators']

  key = ''.join(e for e in label['productName'] if e.isalnum())
  
  # Generate front matter.
  front_matter = 'title: "' + label['productName'] + '"\n'
  front_matter = front_matter + 'modified: ' + run_date + '\n'

  # Write file.
  filename = output_dir + '/' + key + '.md'
  f = open(filename, 'w')
  out_string = front_matter_pre + front_matter + yaml.dump(label, default_flow_style=False) +front_matter_post
  f.write(out_string)
  f.close()
  