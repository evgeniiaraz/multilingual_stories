#!/bin/sh

git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/global-asp/global-asp \
;
cd global-asp
git sparse-checkout add $1

echo $1

python load_subspace.py --language $1