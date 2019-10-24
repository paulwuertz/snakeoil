import jinja2, yaml, os
import subprocess, textwrap

kartoj = yaml.safe_load(open("roloj.yaml").read())   # listo de kartoj
print(kartoj)
kartoj = [k for k in kartoj for i in range(k["kvanto"])] # adpatas la liston por kvanto de karto
pagxoj = [kartoj[i:i+9] for i in range(0, len(kartoj), 9)] #disigas la kartaro en pagxojn po de 9 kartoj

karto_x = 60.5
karto_y = 99
maldekstra_offset = 25
suba_offset = -5

for i, pagxo in enumerate(pagxoj):
    template_str = open("templates/roloj_sxablono.svg").read()
    t = jinja2.Template(template_str)
    kartoj_offsets = zip(pagxo, [
                        (maldekstra_offset, -(suba_offset + karto_y)),   (maldekstra_offset + karto_x, -(suba_offset + karto_y)),   (maldekstra_offset + 2*karto_x, -(suba_offset + karto_y)),   (maldekstra_offset + 3*karto_x, -(suba_offset + karto_y)),
                        (maldekstra_offset, -(suba_offset + 2*karto_y)), (maldekstra_offset + karto_x, -(suba_offset + 2*karto_y)), (maldekstra_offset + 2*karto_x, -(suba_offset + 2*karto_y)), (maldekstra_offset + 3*karto_x, -(suba_offset + 2*karto_y))
                    ])
    #kartoj_offsets = zip(pagxo, [
                        #(0, 0),   (60, 0),   (120, 0),   (180, 0),
                        #(0, -99.8), (60, -99.8), (120, -99.8), (180, -99.8)
                    #])
    r = t.render(kartoj_offsets=kartoj_offsets)
    open('svg/{}.svg'.format(i), "w").write(r)
    subprocess.check_output(['inkscape','-z', '--export-dpi', '300', 'svg/{}.svg'.format(i), '-e', 'img/{}.png'.format(i)])
subprocess.check_output(['convert', 'img/[0-9]*.png', 'rolo.pdf'])
