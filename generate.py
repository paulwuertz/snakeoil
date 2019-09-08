import jinja2, yaml, os
import subprocess, textwrap

kartoj = yaml.safe_load(open("kartoj.yaml").read())   # listo de kartoj
kartoj = [k for k in kartoj for i in range(k["kvanto"])] # adpatas la liston por kvanto de karto
pagxoj = [kartoj[i:i+9] for i in range(0, len(kartoj), 9)] #disigas la kartaro en pagxojn po de 9 kartoj

for i, pagxo in enumerate(pagxoj):
    template_str = open("templates/kartoj_sxablono.svg").read()
    t = jinja2.Template(template_str)
    kartoj_offsets = zip(pagxo, [
                        (0, -99), (61, -99), (122, -99), (183, -99),
                        (0, 0),   (61, 0),   (122, 0),   (183, 0),
                    ])
    r = t.render(kartoj_offsets=kartoj_offsets)
    open('svg/{}.svg'.format(i), "w").write(r)
    subprocess.check_output(['inkscape','-z', '--export-dpi', '300', 'svg/{}.svg'.format(i), '-e', 'img/{}.png'.format(i)])
subprocess.check_output(['convert', 'img/[0-9]*.png', 'ludo.pdf'])
