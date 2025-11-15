PHASE 1 - Twilight Masterpatch (v1.17.0)

Files added:
 - common/traits/twilight_traits.txt
 - common/character_modifiers/everguard_modifiers.txt
 - common/awards/twilight_awards.txt
 - localisation/english/twilight_phase1_l_english.yml

Place DDS icons (optional for now):
 gfx/interface/icons/traits/trait_midnight_covenant.dds
 gfx/interface/icons/traits/trait_twilight_legionary.dds
 gfx/interface/icons/traits/trait_everguard_favored.dds
 gfx/interface/icons/awards/award_medal_01.dds .. award_medal_06.dds

Quick test:
 - Start CK3 with the mod enabled.
 - Open game console and type: "help" to confirm console works.
 - To test awarding an award manually (after you get character id):
    event twilight_legion.1010 <charid>   # (I will provide this event next)
 - To check trait addition manually in console:
    add_trait twilight_legion_trait_legionary <charid>

Notes:
 - These files are designed to NOT overwrite existing vanilla files; they are standalone.
 - If you already have files with same file-names in your mod, back them up first.
 - After you paste, say: "OK pasted — next" and I will send Phase 1 file #2 (Everguard safety usage & example event to grant modifier + the Twilight Legion membership sample event).
