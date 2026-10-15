"""insert_level_time_per_th

Revision ID: 586758cca3b5
Revises: 80edcbf85d16
Create Date: 2026-09-23 16:02:07.390947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '586758cca3b5'
down_revision: Union[str, Sequence[str], None] = '80edcbf85d16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


LEVELS_DATA = [
    ('cannon', 'Defenses', 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 17, 19, 20, 21, 21, 21, 21),
    ('archer_tower', 'Defenses', 2, 3, 4, 6, 7, 8, 10, 11, 13, 15, 17, 19, 20, 21, 21, 21, 21),
    ('mortar', 'Defenses', 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18),
    ('air_defense', 'Defenses', 0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
    ('wizard_tower', 'Defenses', 0, 0, 0, 2, 3, 4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 17, 17),
    ('air_sweeper', 'Defenses', 0, 0, 0, 0, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7),
    ('hidden_tesla', 'Defenses', 0, 0, 0, 0, 0, 3, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17),
    ('bomb_tower', 'Defenses', 0, 0, 0, 0, 0, 0, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13),
    ('x-bow', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13),
    ('inferno_tower', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 6, 7, 8, 9, 10, 11, 12),
    ('eagle_artillery', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7, 0, 0),
    ('scattershot', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7),
    ("builder's_hut", 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 6, 7, 8),
    ('monolith', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5),
    ('spell_tower', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 4, 4),
    ('multi-archer_tower', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4),
    ('ricochet_cannon', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4),
    ('firespitter', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3),
    ('multi-gear_tower', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3),
    ('inferno_artillery', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0),
    ('revenge_tower', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2),
    ('super_wizard_tower', 'Defenses', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2),
    ('bomb', 'Traps', 0, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14),
    ('spring_trap', 'Traps', 0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
    ('air_bomb', 'Traps', 0, 0, 0, 2, 2, 3, 3, 4, 4, 5, 6, 8, 9, 10, 11, 12, 13),
    ('giant_bomb', 'Traps', 0, 0, 0, 0, 2, 2, 3, 3, 4, 5, 5, 7, 8, 9, 10, 11, 12),
    ('seeking_air_mine', 'Traps', 0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8),
    ('skeleton_trap', 'Traps', 0, 0, 0, 0, 0, 0, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5),
    ('tornado_trap', 'Traps', 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3),
    ('giga_bomb', 'Traps', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4),
    ('army_camp', 'Army', 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 11, 11, 12, 12, 13, 14),
    ('barracks', 'Army', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 19),
    ('clan_castle', 'Army', 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
    ('laboratory', 'Army', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
    ('hero_hall', 'Army', 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    ('spell_factory', 'Army', 0, 0, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 9, 9, 9),
    ('dark_barracks', 'Army', 0, 0, 0, 0, 0, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13),
    ('dark_spell_factory', 'Army', 0, 0, 0, 0, 0, 0, 2, 4, 5, 5, 6, 6, 7, 8, 8, 8, 8),
    ('blacksmith', 'Army', 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10),
    ('workshop', 'Army', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 6, 7, 8, 9, 9),
    ('pet_house', 'Army', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 10, 11, 12),
    ('gold_mine', 'Resources', 4, 6, 8, 10, 10, 11, 12, 12, 13, 14, 15, 15, 16, 16, 17, 17, 17),
    ('elixir_collector', 'Resources', 4, 6, 8, 10, 10, 11, 12, 12, 13, 14, 15, 15, 16, 16, 17, 17, 17),
    ('gold_storage', 'Resources', 3, 6, 8, 9, 10, 11, 11, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    ('elixir_storage', 'Resources', 3, 6, 8, 9, 10, 11, 11, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    ('dark_elixir_drill', 'Resources', 0, 0, 0, 0, 0, 3, 3, 6, 7, 8, 9, 9, 10, 10, 11, 11, 11),
    ('dark_elixir_storage', 'Resources', 0, 0, 0, 0, 0, 2, 4, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13),
    ('helper_hut', 'Resources', 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    ('wall', 'Walls', 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    ('barbarian', 'Troops', 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13),
    ('archer', 'Troops', 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14),
    ('giant', 'Troops', 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14),
    ('goblin', 'Troops', 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 9, 9, 10),
    ('wall_breaker', 'Troops', 0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
    ('balloon', 'Troops', 0, 0, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10, 11, 12, 13),
    ('wizard', 'Troops', 0, 0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14),
    ('healer', 'Troops', 0, 0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 11),
    ('dragon', 'Troops', 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
    ('pekka', 'Troops', 0, 0, 0, 0, 0, 0, 3, 4, 6, 7, 8, 9, 9, 10, 11, 12, 13),
    ('baby_dragon', 'Troops', 0, 0, 0, 0, 0, 0, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    ('miner', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 6, 7, 8, 9, 10, 11, 12),
    ('electro_dragon', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7, 8, 9),
    ('yeti', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7, 8),
    ('dragon_rider', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 4, 5, 6),
    ('electro_titan', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 4, 5),
    ('root_rider', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 4),
    ('thrower', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4),
    ('meteor_golem', 'Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3),
    ('minion', 'Dark Troops', 0, 0, 0, 0, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
    ('hog_rider', 'Dark Troops', 0, 0, 0, 0, 0, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15),
    ('valkyrie', 'Dark Troops', 0, 0, 0, 0, 0, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12),
    ('golem', 'Dark Troops', 0, 0, 0, 0, 0, 0, 2, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15),
    ('witch', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8),
    ('lava_hound', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 6, 6, 7, 7, 8),
    ('bowler', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    ('ice_golem', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 5, 6, 7, 8, 9, 9),
    ('headhunter', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 4),
    ('apprentice_warden', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 4, 4, 4),
    ('druid', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6),
    ('furnace', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 4),
    ('ruin_witch', 'Dark Troops', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4),
    ('lightning_spell', 'Spells', 0, 0, 0, 4, 4, 4, 5, 6, 7, 8, 9, 9, 9, 10, 11, 12, 13),
    ('healing_spell', 'Spells', 0, 0, 0, 0, 3, 4, 5, 6, 7, 7, 7, 8, 8, 9, 10, 11, 12),
    ('rage_spell', 'Spells', 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7),
    ('poison_spell', 'Spells', 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    ('earthquake_spell', 'Spells', 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8),
    ('jump_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5),
    ('freeze_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 2, 5, 6, 7, 7, 7, 7, 7, 7, 8),
    ('haste_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 2, 4, 5, 5, 5, 5, 5, 5, 6, 7),
    ('skeleton_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 1, 3, 4, 6, 7, 7, 8, 8, 8, 8),
    ('clone_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 5, 6, 7, 8, 8, 8, 9),
    ('bat_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 5, 5, 6, 6, 7, 8),
    ('invisibility_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 4, 4, 4, 4, 4),
    ('overgrowth_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 3, 4, 4, 5),
    ('recall_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7),
    ('ice_block_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6),
    ('revive_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5),
    ('angry_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4),
    ('totem_spell', 'Spells', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4),
    ('wall_wrecker', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 5, 5, 6),
    ('battle_blimp', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 5, 5, 6),
    ('stone_slammer', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 5, 5, 6),
    ('siege_barracks', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 5, 5, 6),
    ('log_launcher', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 5, 5, 6),
    ('flame_flinger', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 5, 5, 5),
    ('battle_drill', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 5, 6),
    ('troop_launcher', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4),
    ('sky_wagon', 'Siege Machines', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4),
    ('barbarian_king', 'Heroes', 0, 0, 0, 0, 0, 10, 20, 30, 40, 50, 65, 75, 85, 90, 95, 100, 110),
    ('archer_queen', 'Heroes', 0, 0, 0, 0, 0, 0, 10, 30, 40, 50, 65, 75, 85, 90, 95, 100, 110),
    ('minion_prince', 'Heroes', 0, 0, 0, 0, 0, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95),
    ('grand_warden', 'Heroes', 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 50, 60, 65, 70, 75, 85),
    ('royal_champion', 'Heroes', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 30, 40, 45, 50, 55),
    ('dragon_duke', 'Heroes', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 15, 20, 25),
    ('lassi', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 15, 15, 15, 15),
    ('electro_owl', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 15, 15, 15),
    ('mighty_yak', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 15, 15, 15, 15),
    ('unicorn', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 15, 15),
    ('frosty', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 15, 15),
    ('diggy', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 15),
    ('poison_lizard', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 15, 15),
    ('phoenix', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10),
    ('spirit_fox', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10),
    ('angry_jelly', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10),
    ('sneezy', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10),
    ('greedy_raven', 'Pets', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10),
]

TIME_DATA = [
    ('town_hall', 'Resources', None, 10, 1800, 10800, 21600, 43200, 64800, 86400, 172800, 259200, 432000, 518400, 604800, 648000, 691200, 777600, 864000, 1036800, None, None, None),
    ('gold_mine', 'Resources', 5, 15, 60, 120, 300, 900, 1800, 3600, 5400, 7200, 10800, 14400, 18000, 21600, 36000, 86400, 172800, 172800, 259200, 345600, None),
    ('gold_storage', 'Resources', 10, 120, 300, 900, 1800, 3600, 7200, 10800, 14400, 18000, 21600, 43200, 64800, 86400, 172800, 259200, 345600, 432000, 1080000, None, None),
    ('elixir_collector', 'Resources', 5, 15, 60, 120, 300, 900, 1800, 3600, 5400, 7200, 10800, 14400, 18000, 21600, 36000, 86400, 172800, 172800, 259200, 345600, None),
    ('elixir_storage', 'Resources', 10, 120, 300, 900, 1800, 3600, 7200, 10800, 14400, 18000, 21600, 43200, 64800, 86400, 172800, 259200, 345600, 432000, 1080000, None, None),
    ('dark_elixir_drill', 'Resources', 14400, 21600, 43200, 64800, 86400, 129600, 151200, 172800, 216000, 259200, 518400, 259200, 345600, 432000, None, None, None, None, None, None, None),
    ('dark_elixir_storage', 'Resources', 28800, 57600, 86400, 129600, 144000, 172800, 259200, 302400, 345600, 388800, 432000, 604800, 1123200, None, None, None, None, None, None, None, None),
    ('helper_hut', 'Resources', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('cannon', 'Defenses', 5, 30, 120, 1200, 1800, 3600, 7200, 10800, 12600, 14400, 16200, 18000, 21600, 28800, 36000, 39600, 43200, 57600, 72000, 86400, 129600),
    ('archer_tower', 'Defenses', 15, 120, 1200, 3600, 5400, 7200, 10800, 14400, 18000, 21600, 25200, 28800, 36000, 39600, 43200, 57600, 72000, 86400, 108000, 129600, 172800),
    ('mortar', 'Defenses', 1800, 3600, 7200, 10800, 21600, 28800, 43200, 64800, 72000, 86400, 108000, 129600, 172800, 216000, 259200, 345600, 432000, 1080000, 345600, 518400, None),
    ('air_defense', 'Defenses', 3600, 7200, 21600, 43200, 64800, 86400, 172800, 216000, 259200, 345600, 388800, 432000, 518400, 561600, 604800, 1144800, 237600, 367200, None, None, None),
    ('wizard_tower', 'Defenses', 3600, 5400, 14400, 28800, 36000, 43200, 64800, 72000, 86400, 108000, 129600, 151200, 172800, 259200, 345600, 388800, 475200, None, None, None, None),
    ('air_sweeper', 'Defenses', 14400, 21600, 28800, 43200, 86400, 172800, 259200, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('hidden_tesla', 'Defenses', 7200, 10800, 14400, 21600, 43200, 86400, 108000, 129600, 151200, 172800, 216000, 259200, 302400, 345600, 432000, 604800, 1123200, 388800, 561600, None, None),
    ('bomb_tower', 'Defenses', 43200, 64800, 86400, 129600, 151200, 172800, 259200, 302400, 345600, 388800, 432000, 604800, 1123200, 216000, 345600, None, None, None, None, None, None),
    ('x-bow', 'Defenses', 43200, 86400, 172800, 216000, 259200, 302400, 345600, 388800, 432000, 475200, 518400, 691200, 1166400, 475200, 648000, None, None, None, None, None, None),
    ('inferno_tower', 'Defenses', 43200, 86400, 172800, 216000, 259200, 345600, 432000, 518400, 561600, 604800, 691200, 1166400, 432000, 604800, None, None, None, None, None, None, None),
    ('eagle_artillery', 'Defenses', 345600, 432000, 604800, 648000, 691200, 777600, 820800, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('scattershot', 'Defenses', 432000, 604800, 648000, 691200, 734400, 777600, 1296000, 432000, 604800, None, None, None, None, None, None, None, None, None, None, None, None),
    ("builder's_hut", 'Defenses', None, 172800, 259200, 345600, 432000, 475200, 604800, 1123200, 345600, 518400, None, None, None, None, None, None, None, None, None, None, None),
    ('spell_tower', 'Defenses', 604800, 691200, 734400, 864000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('monolith', 'Defenses', 604800, 691200, 777600, 950400, 1296000, 432000, 604800, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('ricochet_cannon', 'Defenses', 604800, 691200, 777600, 1166400, 518400, 604800, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('multi-archer_tower', 'Defenses', 604800, 691200, 777600, 1209600, 518400, 604800, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('firespitter', 'Defenses', 734400, 864000, 1296000, 561600, 648000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('multi-gear_tower', 'Defenses', 691200, 777600, 1209600, 518400, 604800, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('inferno_artillery', 'Defenses', None, 518400, 604800, 691200, 864000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('revenge_tower', 'Defenses', 1123205, 1209600, 604800, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('super_wizard_tower', 'Defenses', 1123200, 1209600, 518400, 604800, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('bomb', 'Traps', None, 60, 300, 2400, 3600, 7200, 10800, 14400, 21600, 43200, 64800, 86400, 172800, 691200, None, None, None, None, None, None, None),
    ('spring_trap', 'Traps', None, 3600, 7200, 10800, 14400, 21600, 28800, 43200, 64800, 86400, 172800, 259200, 950400, None, None, None, None, None, None, None, None),
    ('air_bomb', 'Traps', None, 1800, 3600, 14400, 28800, 43200, 50400, 57600, 86400, 129600, 172800, 259200, 777600, None, None, None, None, None, None, None, None),
    ('giant_bomb', 'Traps', None, 3600, 10800, 14400, 36000, 39600, 43200, 86400, 172800, 216000, 345600, 907200, None, None, None, None, None, None, None, None, None),
    ('seeking_air_mine', 'Traps', None, 21600, 86400, 129600, 172800, 259200, 432000, 993600, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('skeleton_trap', 'Traps', None, 18000, 28800, 43200, 604800, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('tornado_trap', 'Traps', None, 86400, 172800, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('giga_bomb', 'Traps', None, 345600, 432000, 1123200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('clan_castle', 'Army', None, 7200, 43200, 86400, 129600, 172800, 259200, 345600, 518400, 604800, 691200, 777600, 864000, 1209600, None, None, None, None, None, None, None),
    ('army_camp', 'Army', 60, 300, 1800, 7200, 21600, 43200, 172800, 259200, 302400, 345600, 432000, 518400, 648000, 1296000, None, None, None, None, None, None, None),
    ('barracks', 'Army', 10, 15, 120, 1800, 7200, 14400, 21600, 43200, 86400, 129600, 172800, 345600, 432000, 518400, 604800, 648000, 691200, 777600, 907200, None, None),
    ('laboratory', 'Army', 60, 1800, 7200, 14400, 28800, 57600, 86400, 151200, 237600, 345600, 518400, 604800, 691200, 777600, 864000, 1382400, None, None, None, None, None),
    ('spell_factory', 'Army', 21600, 43200, 86400, 172800, 259200, 432000, 604800, 691200, 777600, None, None, None, None, None, None, None, None, None, None, None, None),
    ('dark_barracks', 'Army', 28800, 86400, 129600, 172800, 216000, 259200, 432000, 518400, 604800, 648000, 691200, 777600, 864000, None, None, None, None, None, None, None, None),
    ('dark_spell_factory', 'Army', 21600, 43200, 172800, 259200, 432000, 518400, 604800, 864000, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('blacksmith', 'Army', 43200, 86400, 172800, 259200, 345600, 388800, 432000, 518400, 604800, 864000, None, None, None, None, None, None, None, None, None, None, None),
    ('workshop', 'Army', 172800, 259200, 302400, 345600, 432000, 475200, 518400, 604800, 1166400, None, None, None, None, None, None, None, None, None, None, None, None),
    ('pet_house', 'Army', 86400, 172800, 259200, 302400, 345600, 388800, 432000, 475200, 518400, 604800, 691200, 1166400, None, None, None, None, None, None, None, None, None),
    ('hero_hall', 'Army', 86400, 172800, 259200, 345600, 388800, 432000, 518400, 561600, 604800, 691200, 777600, 1166400, None, None, None, None, None, None, None, None, None),
    ('barbarian', 'Troops', None, 1800, 3600, 7200, 14400, 28800, 43200, 86400, 129600, 172800, 259200, 345600, 1080000, None, None, None, None, None, None, None, None),
    ('archer', 'Troops', None, 3600, 7200, 10800, 28800, 43200, 86400, 129600, 172800, 259200, 345600, 388800, 777600, 1166400, None, None, None, None, None, None, None),
    ('giant', 'Troops', None, 7200, 14400, 21600, 43200, 86400, 129600, 172800, 194400, 259200, 345600, 432000, 820800, 1166400, None, None, None, None, None, None, None),
    ('goblin', 'Troops', None, 7200, 10800, 21600, 43200, 86400, 129600, 194400, 432000, 1209600, None, None, None, None, None, None, None, None, None, None, None),
    ('wall_breaker', 'Troops', None, 10800, 14400, 43200, 57600, 86400, 129600, 216000, 259200, 432000, 475200, 518400, 864000, 1209600, None, None, None, None, None, None, None),
    ('balloon', 'Troops', None, 14400, 21600, 64800, 86400, 259200, 280800, 302400, 388800, 604800, 734400, 950400, 1274400, None, None, None, None, None, None, None, None),
    ('wizard', 'Troops', None, 14400, 18000, 43200, 64800, 129600, 172800, 194400, 216000, 302400, 475200, 604800, 907200, 1209600, None, None, None, None, None, None, None),
    ('healer', 'Troops', None, 43200, 86400, 172800, 259200, 388800, 561600, 604800, 626400, 950400, 1296000, None, None, None, None, None, None, None, None, None, None),
    ('dragon', 'Troops', None, 64800, 129600, 172800, 259200, 345600, 388800, 432000, 604800, 648000, 734400, 864000, 1296000, None, None, None, None, None, None, None, None),
    ('p.e.k.k.a', 'Troops', None, 43200, 64800, 86400, 129600, 172800, 259200, 302400, 345600, 475200, 604800, 864000, 1252800, None, None, None, None, None, None, None, None),
    ('baby_dragon', 'Troops', None, 86400, 129600, 172800, 237600, 259200, 345600, 518400, 604800, 626400, 864000, 1317600, None, None, None, None, None, None, None, None, None),
    ('miner', 'Troops', None, 86400, 172800, 194400, 216000, 259200, 345600, 518400, 561600, 604800, 820800, 1252800, None, None, None, None, None, None, None, None, None),
    ('electro_dragon', 'Troops', None, 345600, 388800, 604800, 691200, 734400, 777600, 864000, 1382400, None, None, None, None, None, None, None, None, None, None, None, None),
    ('yeti', 'Troops', None, 259200, 388800, 604800, 648000, 712800, 864000, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('dragon_rider', 'Troops', None, 518400, 691200, 777600, 885600, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('electro_titan', 'Troops', None, 691200, 777600, 950400, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('root_rider', 'Troops', None, 691200, 864000, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('thrower', 'Troops', None, 820800, 907200, 1296000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('meteor_golem', 'Troops', None, 1209600, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('minion', 'Dark Troops', None, 21600, 28800, 43200, 86400, 129600, 151200, 172800, 259200, 345600, 388800, 432000, 777600, 1209600, None, None, None, None, None, None, None),
    ('hog_rider', 'Dark Troops', None, 36000, 64800, 86400, 172800, 194400, 216000, 259200, 302400, 345600, 432000, 475200, 561600, 864000, 1252800, None, None, None, None, None, None),
    ('valkyrie', 'Dark Troops', None, 28800, 86400, 129600, 151200, 172800, 194400, 259200, 388800, 432000, 518400, 1209600, None, None, None, None, None, None, None, None, None),
    ('golem', 'Dark Troops', None, 57600, 129600, 172800, 194400, 216000, 237600, 259200, 302400, 345600, 432000, 475200, 518400, 864000, 1252800, None, None, None, None, None, None),
    ('witch', 'Dark Troops', None, 172800, 259200, 302400, 345600, 475200, 626400, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('lava_hound', 'Dark Troops', None, 172800, 216000, 259200, 345600, 604800, 691200, 1317600, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('bowler', 'Dark Troops', None, 172800, 216000, 259200, 345600, 518400, 604800, 648000, 864000, 1296000, None, None, None, None, None, None, None, None, None, None, None),
    ('ice_golem', 'Dark Troops', None, 172800, 216000, 280800, 345600, 561600, 648000, 691200, 914400, None, None, None, None, None, None, None, None, None, None, None, None),
    ('headhunter', 'Dark Troops', None, 432000, 604800, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('apprentice_warden', 'Dark Troops', None, 518400, 648000, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('druid', 'Dark Troops', None, 691200, 777600, 950400, 1036800, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('furnace', 'Dark Troops', None, 777600, 950400, 1296000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('ruin_witch', 'Dark Troops', None, 950400, 1036800, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('lightning_spell', 'Spells', None, 7200, 14400, 21600, 86400, 129600, 259200, 302400, 432000, 518400, 604800, 864000, 1209600, None, None, None, None, None, None, None, None),
    ('healing_spell', 'Spells', None, 10800, 21600, 43200, 86400, 129600, 259200, 432000, 561600, 604800, 907200, 1296000, None, None, None, None, None, None, None, None, None),
    ('rage_spell', 'Spells', None, 21600, 43200, 86400, 172800, 345600, 1209600, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('jump_spell', 'Spells', None, 86400, 172800, 345600, 432000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('freeze_spell', 'Spells', None, 86400, 129600, 172800, 216000, 302400, 432000, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('clone_spell', 'Spells', None, 86400, 172800, 194400, 216000, 345600, 432000, 604800, 1166400, None, None, None, None, None, None, None, None, None, None, None, None),
    ('invisibility_spell', 'Spells', None, 259200, 345600, 432000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('recall_spell', 'Spells', None, 604800, 648000, 691200, 777600, 950400, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('revive_spell', 'Spells', None, 604800, 691200, 993600, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('totem_spell', 'Spells', None, 1036800, 1209600, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('poison_spell', 'Dark Spells', None, 21600, 64800, 172800, 259200, 345600, 432000, 561600, 604800, 691200, 835200, 1252800, None, None, None, None, None, None, None, None, None),
    ('earthquake_spell', 'Dark Spells', None, 43200, 86400, 259200, 302400, 691200, 777600, 1166400, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('haste_spell', 'Dark Spells', None, 86400, 172800, 259200, 345600, 777600, 1080000, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('skeleton_spell', 'Dark Spells', None, 43200, 86400, 172800, 216000, 259200, 345600, 518400, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('bat_spell', 'Dark Spells', None, 64800, 129600, 194400, 345600, 604800, 734400, 1123200, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('overgrowth_spell', 'Dark Spells', None, 432000, 734400, 864000, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('ice_block_spell', 'Dark Spells', None, 864000, 950400, 1036800, 1209600, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('angry_spell', 'Dark Spells', None, 806400, 1036800, 1296000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('wall_wrecker', 'Siege Machines', None, 172800, 259200, 604800, 777600, 1166400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('battle_blimp', 'Siege Machines', None, 172800, 259200, 604800, 777600, 1166400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('stone_slammer', 'Siege Machines', None, 172800, 259200, 604800, 777600, 1166400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('siege_barracks', 'Siege Machines', None, 259200, 345600, 604800, 1036800, 1296000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('log_launcher', 'Siege Machines', None, 259200, 345600, 604800, 1036800, 1296000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('flame_flinger', 'Siege Machines', None, 259200, 345600, 604800, 1036800, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('battle_drill', 'Siege Machines', None, 345600, 432000, 691200, 777600, 1339200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('troop_launcher', 'Siege Machines', None, 518400, 777600, 777600, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('sky_wagon', 'Siege Machines', None, 864000, 1166400, 1382400, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
]

HERO_PET_DATA = [
    ('barbarian_king', 'Heroes', None, 7200, 14400, 28800, 36000, 43200, 50400, 57600, 64800, 72000, 79200, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 172800, 172800, 172800, 172800, 172800, 194400, 194400, 194400, 194400, 194400, 216000, 216000, 216000, 216000, 216000, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 432000, 432000, 432000, 432000, 432000, 518400, 518400, 518400, 518400, 518400, 604800, 604800, 604800, 604800, 604800, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200),
    ('archer_queen', 'Heroes', None, 7200, 14400, 28800, 36000, 43200, 50400, 57600, 64800, 72000, 79200, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 172800, 172800, 172800, 172800, 172800, 194400, 194400, 194400, 194400, 194400, 216000, 216000, 216000, 216000, 216000, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 432000, 432000, 432000, 432000, 432000, 518400, 518400, 518400, 518400, 518400, 604800, 604800, 604800, 604800, 604800, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200),
    ('minion_prince', 'Heroes', None, 7200, 14400, 28800, 36000, 43200, 50400, 57600, 64800, 72000, 79200, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 129600, 129600, 129600, 129600, 129600, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 194400, 194400, 194400, 194400, 194400, 259200, 259200, 259200, 259200, 259200, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 432000, 432000, 432000, 432000, 432000, 518400, 518400, 518400, 518400, 518400, 604800, 604800, 604800, 604800, 604800, 648000, 648000, 648000, 648000, 648000, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('grand_warden', 'Heroes', None, 7200, 14400, 28800, 36000, 43200, 50400, 57600, 64800, 72000, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 129600, 129600, 129600, 129600, 129600, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 172800, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 259200, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 345600, 518400, 518400, 518400, 518400, 518400, 604800, 604800, 604800, 604800, 648000, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('royal_champion', 'Heroes', None, 14400, 36000, 43200, 72000, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 86400, 129600, 129600, 129600, 129600, 129600, 172800, 172800, 172800, 172800, 172800, 259200, 259200, 259200, 259200, 259200, 345600, 345600, 345600, 345600, 345600, 432000, 432000, 432000, 432000, 432000, 432000, 518400, 561600, 604800, 648000, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('dragon_duke', 'Heroes', None, 21600, 43200, 86400, 86400, 172800, 172800, 172800, 259200, 259200, 345600, 432000, 432000, 518400, 518400, 604800, 604800, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('lassi', 'Pets', None, 86400, 129600, 172800, 216000, 259200, 302400, 345600, 388800, 432000, 475200, 518400, 561600, 604800, 648000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('electro_owl', 'Pets', None, 129600, 172800, 259200, 345600, 388800, 432000, 475200, 518400, 561600, 604800, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('mighty_yak', 'Pets', None, 86400, 129600, 172800, 216000, 259200, 302400, 345600, 388800, 432000, 475200, 518400, 561600, 604800, 648000, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('unicorn', 'Pets', None, 129600, 172800, 259200, 345600, 388800, 432000, 475200, 518400, 561600, 604800, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('frosty', 'Pets', None, 129600, 172800, 259200, 345600, 388800, 432000, 475200, 518400, 561600, 604800, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('diggy', 'Pets', None, 129600, 172800, 259200, 345600, 388800, 432000, 475200, 518400, 561600, 604800, 648000, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('poison_lizard', 'Pets', None, 86400, 129600, 172800, 216000, 259200, 302400, 345600, 388800, 432000, 518400, 604800, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('phoenix', 'Pets', None, 129600, 172800, 259200, 345600, 388800, 432000, 475200, 518400, 561600, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('spirit_fox', 'Pets', None, 259200, 345600, 432000, 475200, 518400, 561600, 604800, 648000, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('angry_jelly', 'Pets', None, 259200, 345600, 432000, 518400, 604800, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('sneezy', 'Pets', None, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
    ('greedy_raven', 'Pets', None, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, 691200, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None),
]

# th_level values that align 1:1 with LEVELS_DATA's value columns (th2..th18)
TH_LEVELS = list(range(2, 19))
# level values that align 1:1 with TIME_DATA's value columns
TIME_LEVELS = list(range(1, 22))
# level values that align 1:1 with HERO_PET_DATA's value columns (levels 1..110)
HP_LEVELS = list(range(1, 111))

# A few things use an inconsistent category between LEVELS_DATA and TIME_DATA
# in the source data (e.g. 'poison_spell' as 'Spells' vs 'Dark Spells').
# Normalize to the more specific category so `thing` + `category` line up
# across all three tables.
CATEGORY_OVERRIDES = {
    ('poison_spell', 'Spells'): 'Dark Spells',
    ('earthquake_spell', 'Spells'): 'Dark Spells',
    ('haste_spell', 'Spells'): 'Dark Spells',
    ('skeleton_spell', 'Spells'): 'Dark Spells',
    ('bat_spell', 'Spells'): 'Dark Spells',
    ('overgrowth_spell', 'Spells'): 'Dark Spells',
    ('ice_block_spell', 'Spells'): 'Dark Spells',
    ('angry_spell', 'Spells'): 'Dark Spells',
}


def _normalize_category(thing, category):
    return CATEGORY_OVERRIDES.get((thing, category), category)


def _unpivot_levels(data, levels):
    """(thing, category, v1, v2, ...) -> narrow dicts. Skips 0 (not yet unlocked)."""
    rows = []
    for entry in data:
        thing, category = entry[0], entry[1]
        category = _normalize_category(thing, category)
        for lvl, val in zip(levels, entry[2:]):
            if val is None or val == 0:
                continue
            rows.append({
                "thing": thing,
                "category": category,
                "th_level": lvl,
                "unlocked_level": val,
            })
    return rows


def _unpivot_times(data, levels):
    """(thing, category, v1, v2, ...) -> narrow dicts. Skips None (no such level)."""
    rows = []
    for entry in data:
        thing, category = entry[0], entry[1]
        category = _normalize_category(thing, category)
        for lvl, val in zip(levels, entry[2:]):
            if val is None:
                continue
            rows.append({
                "thing": thing,
                "category": category,
                "level": lvl,
                "upgrade_time_seconds": val,
            })
    return rows


def upgrade():
    levels_t = sa.table(
        "levels_per_th_home",
        sa.column("thing"), sa.column("category"),
        sa.column("th_level"), sa.column("unlocked_level"),
    )
    time_t = sa.table(
        "time_per_th_home",
        sa.column("thing"), sa.column("category"),
        sa.column("level"), sa.column("upgrade_time_seconds"),
    )
    hp_t = sa.table(
        "time_per_level_hero_pet",
        sa.column("thing"), sa.column("category"),
        sa.column("level"), sa.column("upgrade_time_seconds"),
    )

    levels_rows = _unpivot_levels(LEVELS_DATA, TH_LEVELS)
    time_rows = _unpivot_times(TIME_DATA, TIME_LEVELS)
    hp_rows = _unpivot_times(HERO_PET_DATA, HP_LEVELS)

    if levels_rows:
        op.bulk_insert(levels_t, levels_rows)
    if time_rows:
        op.bulk_insert(time_t, time_rows)
    if hp_rows:
        op.bulk_insert(hp_t, hp_rows)


def downgrade():
    bind = op.get_bind()

    levels_things = sorted({row[0] for row in LEVELS_DATA})
    time_things = sorted({row[0] for row in TIME_DATA})
    hp_things = sorted({row[0] for row in HERO_PET_DATA})

    bind.execute(
        sa.text("DELETE FROM levels_per_th_home WHERE thing IN :things")
        .bindparams(sa.bindparam("things", expanding=True)),
        {"things": levels_things},
    )
    bind.execute(
        sa.text("DELETE FROM time_per_th_home WHERE thing IN :things")
        .bindparams(sa.bindparam("things", expanding=True)),
        {"things": time_things},
    )
    bind.execute(
        sa.text("DELETE FROM time_per_level_hero_pet WHERE thing IN :things")
        .bindparams(sa.bindparam("things", expanding=True)),
        {"things": hp_things},
    )
