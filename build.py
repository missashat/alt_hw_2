# Concerts Attended
top_template = open('/templates/conc_att_top.html').read()
bottom_template = open('/templates/conc_att_bottom.html').read()

# Read in index HTML code
content = open('/content/conc_att.html').read()

# Combine template HTML code with content HTML code
conc_att_html = top_template + content + bottom_template
open('/docs/conc_att.html', 'w+').write(con_att_html)

# Concerts Photos
top_template = open('/templates/conc_photos_top.html').read()
bottom_template = open('/templates/conc_photos_bottom.html').read()

# Read in index HTML code
content = open('/content/conc_photos.html').read()

# Combine template HTML code with content HTML code
conc_photos_html = top_template + content + bottom_template
open('/docs/conc_photos.html', 'w+').write(con_photos_html)

# Concerts Videos
top_template = open('/templates/conc_vids_top.html').read()
bottom_template = open('/templates/conc_vids_bottom.html').read()

# Read in index HTML code
content = open('/content/conc_vids.html').read()

# Combine template HTML code with content HTML code
conc_vids_html = top_template + content + bottom_template
open('/docs/conc_vids.html', 'w+').write(con_vids_html)

# Index
top_template = open('/templates/index_top.html').read()
bottom_template = open('/templates/index_bottom.html').read()

# Read in index HTML code
content = open('/content/index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('/docs/index.html', 'w+').write(index_html)
