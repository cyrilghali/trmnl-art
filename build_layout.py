# Builds full.liquid: French captions for every work, and a note beside each portrait work.
from captions import NAMES, TITLES, NOTES

assert len(NAMES) == len(set(NAMES)) and set(NAMES) == set(TITLES), set(NAMES) ^ set(TITLES)
assert set(NOTES) <= set(NAMES), set(NOTES) - set(NAMES)
for v in list(TITLES.values()) + list(NOTES.values()):
    assert '"' not in v and "|" not in v, v

def nbsp(text):
    # French puts a space before ? ! : ; » and after «; a no-break space keeps the mark on the word's line.
    for a, z in ((" ?", "\u00a0?"), (" !", "\u00a0!"), (" :", "\u00a0:"), (" ;", "\u00a0;"), (" »", "\u00a0»"), ("« ", "«\u00a0")):
        text = text.replace(a, z)
    return text

TITLES = {k: nbsp(v) for k, v in TITLES.items()}
NOTES = {k: nbsp(v) for k, v in NOTES.items()}

cases = "\n".join(f'  {{% when "{k}" %}}{{% assign note = "{NOTES[k]}" %}}' for k in NAMES if k in NOTES)
out = f'''{{% assign names = "{",".join(NAMES)}" | split: "," %}}
{{% assign titles = "{"|".join(TITLES[k] for k in NAMES)}" | split: "|" %}}
{{% assign count = names | size %}}
{{% assign hour = "now" | date: "%s" | divided_by: 3600 %}}
{{% assign pick = hour | modulo: count %}}
{{% assign name = names[pick] %}}
{{% assign src = "https://raw.githubusercontent.com/cyrilghali/trmnl-art/main/img/" | append: name | append: ".jpg" %}}
{{% assign note = "" %}}
{{% case name %}}
{cases}
{{% endcase %}}
{{% if note != "" %}}
{{% assign credit = titles[pick] | split: " — " %}}
<div class="layout" style="padding: 0; flex-direction: row; align-items: stretch; justify-content: flex-start;">
  <img class="image-dither" src="{{{{ src }}}}" style="height: 100%; width: auto; flex: none;">
  <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 20px; padding: 0 36px;">
    <span class="label">{{{{ credit[0] }}}}</span>
    <span class="title title--large">{{{{ credit[1] }}}}</span>
    <p class="description" style="font-size: 19px; line-height: 1.45;">{{{{ note }}}}</p>
  </div>
</div>
{{% else %}}
<div class="layout" style="padding: 0;">
  <img class="image image-dither" src="{{{{ src }}}}" style="width: 100%; height: 100%; object-fit: contain;">
</div>
<div class="title_bar">
  <span class="title">{{{{ titles[pick] }}}}</span>
</div>
{{% endif %}}
'''
open("full.liquid", "w").write(out)
print(len(NAMES), "works,", len(NOTES), "notes,", len(out), "bytes")
