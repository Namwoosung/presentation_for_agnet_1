from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = (root / 'preview.html').read_text(encoding='utf-8')
palette = {
    '#070B15': '#E6EBF1',
    '#0B1020': '#F7F9FC',
    '#EFF4FF': '#17243B',
    '#9EACC8': '#52627A',
    '#33415D': '#C5CEDB',
    '#60A5FA': '#205DB5',
    '#B794F4': '#7041AA',
    '#34D399': '#08765A',
    '#FDBA74': '#9A570F',
    '#FB7185': '#BE3654',
    '#10182B': '#FFFFFF',
    '#11192D': '#F0EBF8',
    '#201B2B': '#FFF0F3',
    '#0D1526': '#EEF2F7',
}
result = re.sub(r'#[0-9A-Fa-f]{6}', lambda m: palette.get(m[0].upper(), m[0]), source)
result = result.replace('Seminar II · V2</title>', 'Seminar II · V2 Light</title>')
(root / 'preview2.html').write_text(result, encoding='utf-8')
print(root / 'preview2.html')
