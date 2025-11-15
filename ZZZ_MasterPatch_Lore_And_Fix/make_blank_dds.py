from PIL import Image
import os

icons = [
 "gfx/interface/icons/regimenttypes/elven_swordguard_icon.dds",
 "gfx/interface/icons/regimenttypes/kessertine_crimson_eye.dds",
 "gfx/interface/icons/traits/midnight_mask.dds",
 "gfx/interface/icons/symbols/icon_arrow_down.dds",
 "gfx/interface/icons/message_feed/icon_tax_collector.dds",
 "gfx/interface/portraits/elf_hidden_placeholder.dds",
 "gfx/interface/shared/empty.dds",
 "gfx/interface/icons/tenets/tenet_beauty_is_divine.dds"
]

base = os.path.join("ZZZ_MasterPatch_Lore_And_Fix")
for icon in icons:
    path = os.path.join(base, icon)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img = Image.new("RGBA", (64,64), (0,0,0,0))
    img.save(path)
print("Blank DDS placeholders created.")
