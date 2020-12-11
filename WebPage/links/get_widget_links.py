import pandas as pd

html= open('ran_hld_module.html', 'r').read()

html2 = html
df_links = pd.DataFrame({'SECTION':[],'LINK':[]})

while html2.find("class=\"a_link\"") > -1:
    link_st_in = html2.find("class=\"a_link\"")
    link_ed_in = html2.find("\">",link_st_in)
    link2= html2[link_st_in+21:link_ed_in]
    #print(link2)

    heading_st_in = html2.rfind("<h", 0, link_st_in)
    section_st_in = html2.find("</h>",heading_st_in)
    section_ed_in = html2.find("</h", heading_st_in)
    section = html2[heading_st_in+4:section_ed_in]
    #print(section)

    df_links = df_links.append({'SECTION': section,'LINK': link2}, ignore_index=True)
    html2 = html2[heading_st_in:link_st_in] + html2[link_ed_in:]
print(df_links)
df_links.to_csv(r'ran_hld_module.csv', index = False)