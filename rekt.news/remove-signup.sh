#!/bin/bash

# rather than fight BS4 just snip it with a sed.

cd data/rekt.new
for i in *; do cd $i; sed 's/<div id="mc_embed_signup">.*//' extracted.html > data.html; mv -f data.html  extracted.html; cd ..; echo $i; done

