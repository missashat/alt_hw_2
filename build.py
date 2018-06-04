# Concerts Attended
top_template = open('/home/aturman/Desktop/ALT_HW_2/templates/conc_att_top.html').read()
bottom_template = open('/home/aturman/Desktop/ALT_HW_2/templates/conc_att_bottom.html').read()

# Read in index HTML code
content = open('/home/aturman/Desktop/ALT_HW_2/content/conc_att.html').read()

# Combine template HTML code with content HTML code
conc_att_html = top_template + content + bottom_template
open('/home/aturman/Desktop/ALT_HW_2/docs/conc_att.html', 'w+').write(conc_att_html)

# Concerts Photos
top_template = open('/home/aturman/Desktop/ALT_HW_2/templates/conc_photos_top.html').read()
bottom_template = open('/home/aturman/Desktop/ALT_HW_2/templates/conc_photos_bottom.html').read()

# Read in index HTML code
content = open('/home/aturman/Desktop/ALT_HW_2/content/conc_photos.html').read()

# Combine template HTML code with content HTML code
conc_photos_html = top_template + content + bottom_template
open('/home/aturman/Desktop/ALT_HW_2/docs/conc_photos.html', 'w+').write(conc_photos_html)

# Concerts Videos
top_template = open('/home/aturman/Desktop/ALT_HW_2/templates/conc_vids_top.html').read()
bottom_template = open('/home/aturman/Desktop/ALT_HW_2/templates/conc_vids_bottom.html').read()

# Read in index HTML code
content = open('/home/aturman/Desktop/ALT_HW_2/content/conc_vids.html').read()

# Combine template HTML code with content HTML code
conc_vids_html = top_template + content + bottom_template
open('/home/aturman/Desktop/ALT_HW_2/docs/conc_vids.html', 'w+').write(conc_vids_html)

# Index
top_template = open('/home/aturman/Desktop/ALT_HW_2/templates/index_top.html').read()
bottom_template = open('/home/aturman/Desktop/ALT_HW_2/templates/index_bottom.html').read()

# Read in index HTML code
content = open('/home/aturman/Desktop/ALT_HW_2/content/index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('/home/aturman/Desktop/ALT_HW_2/docs/index.html', 'w+').write(index_html)
