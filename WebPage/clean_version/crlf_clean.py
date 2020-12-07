html= open('strategic_use.html', 'r').read()

html2 = html

first_pass = True
while html2.find("<p") > -1:
    p_start_index = html2.find("<p")
    p_end_index = html2.find("</p>",p_start_index)
    head , p_content, tail = html2[:p_start_index], html2[p_start_index:p_end_index], html2[p_end_index:]
    if (first_pass):
        new_html = head + p_content.replace("\n", "")
        first_pass = False
    else:
        new_html = new_html + head + p_content.replace("\n", "")
    html2 = html2[p_end_index:]
new_html = new_html + html2

html2 = new_html
first_pass = True

while html2.find("<li") > -1:
    p_start_index = html2.find("<li")
    p_end_index = html2.find("</li>",p_start_index)
    head , p_content, tail = html2[:p_start_index], html2[p_start_index:p_end_index], html2[p_end_index:]
    if (first_pass):
        new_html = head + p_content.replace("\n", "")
        first_pass = False
    else:
        new_html = new_html + head + p_content.replace("\n", "")
    html2 = html2[p_end_index:]
new_html = new_html + html2

html2 = new_html
first_pass = True

while html2.find("<a") > -1:
    p_start_index = html2.find("<a")
    p_end_index = html2.find("</a>",p_start_index)
    head , p_content, tail = html2[:p_start_index], html2[p_start_index:p_end_index], html2[p_end_index:]
    if (first_pass):
        new_html = head + p_content.replace("\n", "")
        first_pass = False
    else:
        new_html = new_html + head + p_content.replace("\n", "")
    html2 = html2[p_end_index:]
new_html = new_html + html2

html2 = new_html
first_pass = True

while html2.find("<h3") > -1:
    p_start_index = html2.find("<h3")
    p_end_index = html2.find("</h3>",p_start_index)
    head , p_content, tail = html2[:p_start_index], html2[p_start_index:p_end_index], html2[p_end_index:]
    if (first_pass):
        new_html = head + p_content.replace("\n", "")
        first_pass = False
    else:
        new_html = new_html + head + p_content.replace("\n", "")
    html2 = html2[p_end_index:]
new_html = new_html + html2

html2 = new_html
first_pass = True

while html2.find("<h4") > -1:
    p_start_index = html2.find("<h4")
    p_end_index = html2.find("</h4>",p_start_index)
    head , p_content, tail = html2[:p_start_index], html2[p_start_index:p_end_index], html2[p_end_index:]
    if (first_pass):
        new_html = head + p_content.replace("\n", "")
        first_pass = False
    else:
        new_html = new_html + head + p_content.replace("\n", "")
    html2 = html2[p_end_index:]
new_html = new_html + html2


html2 = new_html
first_pass = True

while html2.find("<h4") > -1:
    p_start_index = html2.find("<h4")
    p_end_index = html2.find("</h4>",p_start_index)
    head , p_content, tail = html2[:p_start_index], html2[p_start_index:p_end_index], html2[p_end_index:]
    if (first_pass):
        new_html = head + p_content.replace("\n", "")
        first_pass = False
    else:
        new_html = new_html + head + p_content.replace("\n", "")
    html2 = html2[p_end_index:]
new_html = new_html + html2

html = open('strategic_use.html', 'w')
html.write(new_html)
html.close()