import sys
import os

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('..') + "/main_app")

from read_data_from_csv import read_data
from main_app.model import Mix_ratio_table as Mix
from main_app import db


def store(data):
    for row in data:
        new_mix = Mix(
            mix_period=row[0],
            mix_concrete_variety=row[1],
            mix_power_level=row[2],
            mix_impermeability_rating=row[3],
            mix_material_requirements=row[4],
            mix_limit_expansion_rate=row[5],
            mix_slump=row[6],
            mix_expansion=row[7],

            mix_cement_consumption=row[8],
            mix_special_fine_sand_dosage=row[9],
            mix_medium_sand_consumption=row[10],
            mix_coarse_sand_consumption=row[11],
            mix_small_stone_dosage=row[12],
            mix_big_stone_dosage=row[13],
            mix_water_reducing_agent_dosage=row[14],
            mix_fly_ash_dosage=row[15],
            mix_slag_powder_consumption=row[16],
            mix_limestone_powder_consumption=row[17],
            mix_expansion_agent_dosage=row[18],
            mix_water_consumption=row[19],
            mix_recycled_water_consumption=row[20],
            mix_apparent_density=row[21],

            mix_production_workshop=row[22],
            mix_main_workshop=row[23],
            mix_production_line=row[24],
            mix_pouring_method=row[25],
            mix_3d_intensity=row[26],
            mix_7d_intensity=row[27],
            mix_28d_strength=row[28],
            mix_60d_strength=row[29],

            # mix_cement_sample_number = row[],
            cement_breed_grade=row[30],
            cement_28d_compression=row[31],
            cement_supply_unit=row[32],

            # mix_reduce_water_agent_sample_number = row[],
            reduce_breed_grade=row[33],
            reduce_recommended_dosage=row[34],
            reduce_water_reduction_rate=row[35],
            reduce_gas_content=row[36],
            reduce_28d_compressive_strength_ratio=row[37],
            reduce_bleeding_rate_ratio=row[38],

            # mix_fly_ash_sample_number = row[],
            fly_sample_category=row[39],
            fly_breed_grade=row[40],
            fly_fineness=row[41],
            fly_water_demand_ratio=row[42],
            fly_loss_on_ignition=row[43],
            fly_activity_index=row[44],

            # mix_slag_powder_sample_number = row[],
            slag_breed_grade=row[45],
            slag_28d_activity_index=row[46],
            slag_supply_unit=row[47],

            # mix_limestone_powder_sample_number = row[],
            limestone_fineness=row[48],
            limestone_methylene_blue_value=row[49],
            limestone_28d_activity_index=row[50],

            # mix_expansion_agent_sample_number = row[],
            expansion_breed_grade=row[51],
            expansion_28d_compressive_strength=row[52],
            expansion_limit_expansion_rate=row[53]
        )
        db.session.add(new_mix)
        db.session.commit()


if __name__ == '__main__':
    data = read_data()
    store(data)
